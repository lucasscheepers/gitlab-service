import os
import json
import requests
import logging
import time
from exceptions.project_notfound_exception import ProjectNotFoundE
from exceptions.issue_notfound_exception import IssueNotFoundE
from exceptions.tag_notfound_exception import TagNotFoundE
from exceptions.branch_notfound_exception import BranchNotFoundE

log = logging.getLogger("services/gitlab_service.py")


class GitLabService:
    def handle_request_mattermost(self, text):
        """Handles the requests to Mattermost"""
        headers = {'Content-Type': 'application/json', }
        values = '{"username": "gitlab", "text": "' + text + '"}'
        response = requests.post(f"{os.getenv('MATTERMOST_URL')}", headers=headers,
                                 data=values)
        log.info(f"RESPONSE FROM MATTERMOST: {response.text}")

    def handle_request_gitlab(self, url, params, header, request_type):
        """Handles the requests to GitLab"""
        gitlab_down = True
        response_body = None
        count = 0

        while gitlab_down:
            response = None

            if request_type == "POST":
                response = requests.post(url, data=params, headers=header)
            elif request_type == "PUT":
                response = requests.put(url, data=params, headers=header)
            elif request_type == "GET":
                response = requests.get(url, data=params, headers=header)
            elif request_type == "DOWN_SIMULATION":
                response = requests.get("http://httpstat.us/503") if count < 1 else \
                    requests.get("http://httpstat.us/200")
                log.info(f"RESPONSE: {json.loads(response.text)}")

            if response.status_code == 500 or response.status_code == 502 or response.status_code == 503:
                log.error(f"GitLab server is down. I'll try again in ten minutes")
                self.handle_request_mattermost(f"GitLab server is down. Tried to send the request: `{url}`, "
                                               f"but got HTTP response status code {response.status_code}. "
                                               "I'll try again in ten minutes")
                time.sleep(5)  # edit this to your own preferences
                count += 1  # for the simulation when the API is down
                continue
            else:
                gitlab_down = False

            response_body = json.loads(response.text)
            log.info(f"RESPONSE FROM GITLAB: {response_body}")
        return response_body

    def get_project_id(self, project_name):
        """Retrieves a project id from a specific project"""
        url = f"{os.getenv('GITLAB_URL')}/projects"
        header = {'PRIVATE-TOKEN': os.getenv('GITLAB_TOKEN')}
        params = {
            'membership': True,
            'search': project_name
        }

        response_body = self.handle_request_gitlab(url, params, header, "GET")

        try:
            ans = [d for d in response_body if d['name'] == project_name]
            project_id = ans[0]['id']
            log.info(f"Retrieved the project_id from the project '{project_name}': {project_id}")
            return project_id
        except IndexError:
            raise ProjectNotFoundE(project_name)

    def get_issue_id(self, project_id, title_issue):
        """Retrieves a issue id from a specific issue in a project"""
        url = f"{os.getenv('GITLAB_URL')}/projects/{project_id}/issues"
        header = {'PRIVATE-TOKEN': os.getenv('GITLAB_TOKEN')}
        params = {
            'search': title_issue,
            'state': 'opened'
        }

        response_body = self.handle_request_gitlab(url, params, header, "GET")

        log.info(f"GET ISSUES: {response_body}")

        try:
            ans = [d for d in response_body if d['title'] == title_issue]
            issue_id = ans[0]['iid']
            log.info(f"Retrieved the issue_id from the issue '{title_issue}': {issue_id}")
            return issue_id
        except IndexError:
            raise IssueNotFoundE(project_id, title_issue)

    def check_branch(self, project_id, branch):
        """Checks if branch exists"""
        url = f"{os.getenv('GITLAB_URL')}/projects/{project_id}/repository/branches/{branch}"
        header = {'PRIVATE-TOKEN': os.getenv('GITLAB_TOKEN')}

        response = requests.get(url, headers=header)
        response_body = json.loads(response.text)

        try:
            ans = response_body['name']
            log.info(f"Found the branch: {ans}")
            return ans
        except KeyError:
            raise BranchNotFoundE(project_id, branch)

    def create_mr(self, body):
        """Creates merge request in a Git project"""
        try:
            project_id = self.get_project_id(body['project_name'])
            self.check_branch(project_id, body['source_branch'])
            self.check_branch(project_id, body['target_branch'])

            url = f"{os.getenv('GITLAB_URL')}/projects/{project_id}/merge_requests"

            header = {'PRIVATE-TOKEN': os.getenv('GITLAB_TOKEN')}
            params = {
                'id': project_id,
                'title': body['title'],
                'source_branch': body['source_branch'],
                'target_branch': body['target_branch']
            }

            response_body = self.handle_request_gitlab(url, params, header, "POST")

            if "id" in response_body:
                self.handle_request_mattermost("The merge request was created successfully. "
                                               "Please look in GitLab channel for more details ")
                return response_body
            else:
                error = f"{response_body['message']}"[2:-6]
                log.error(f"Tried to create a merge request, but an error has occurred: {error.lower()}")
                self.handle_request_mattermost("Tried to create a merge request, but an error has occurred: "
                                               f"{error.lower()}")

                return error
        except ProjectNotFoundE as project_not_found_error:
            log.error("Tried to create a merge request, but an error has occurred: "
                      f"{str(project_not_found_error).lower()}")
            self.handle_request_mattermost("Tried to create a merge request, but an error has occurred: "
                                           f"{str(project_not_found_error).lower()}. "
                                           "Please specify a correct project name")

            return project_not_found_error
        except BranchNotFoundE as branch_not_found_error:
            log.error("Tried to create a merge request, but an error has occurred: "
                      f"{str(branch_not_found_error).lower()}")
            self.handle_request_mattermost("Tried to create a merge request, but an error has occurred: "
                                           f"{str(branch_not_found_error).lower()}. "
                                           "Please specify a correct branch name")

            return branch_not_found_error

    def create_r(self, body):
        """Rolls out a new release of the project"""
        try:
            project_id = self.get_project_id(body['project_name'])

            url = f"{os.getenv('GITLAB_URL')}/projects/{project_id}/releases"

            header = {'PRIVATE-TOKEN': os.getenv('GITLAB_TOKEN')}
            params = {
                'id': project_id,
                'tag_name': body['tag_name']
            }
            if body['title'] is not None:
                params['name'] = body['title']

            response_body = self.handle_request_gitlab(url, params, header, "POST")

            if "name" in response_body:
                self.handle_request_mattermost("The release rolled out successfully. "
                                               "Please look in GitLab channel for more details ")

                return response_body
            elif response_body['message'] == "Ref is not specified":
                raise TagNotFoundE(project_id, body['tag_name'])
            else:
                log.error(f"Tried to roll out a release, but an error has occurred: {response_body['message']}")
                self.handle_request_mattermost("Tried to roll out a release, but an error has occurred: "
                                               f"{response_body['message']}")

                return response_body['message']
        except ProjectNotFoundE as project_not_found_error:
            log.error("Tried to roll out a release, but an error has occurred: "
                      f"{str(project_not_found_error).lower()}")
            self.handle_request_mattermost("Tried to roll out a release, but an error has occurred: "
                                           f"{str(project_not_found_error).lower()}. "
                                           "Please specify a correct project name")

            return project_not_found_error
        except TagNotFoundE as tag_not_found_error:
            log.error("Tried to roll out a release, but an error has occurred: "
                      f"{str(tag_not_found_error).lower()}")
            self.handle_request_mattermost("Tried to roll out a release, but an error has occurred: "
                                           f"{str(tag_not_found_error).lower()}. "
                                           "Please specify a correct tag name")

            return tag_not_found_error

    def create_i(self, body):
        """Opens a new issue in the project"""
        try:
            project_id = self.get_project_id(body['project_name'])

            url = f"{os.getenv('GITLAB_URL')}/projects/{project_id}/issues"

            header = {'PRIVATE-TOKEN': os.getenv('GITLAB_TOKEN')}
            params = {
                'id': project_id,
                'title': body['title'],
                'description': body['description']
            }

            response_body = self.handle_request_gitlab(url, params, header, "POST")

            if "id" in response_body:
                self.handle_request_mattermost("The new issue was opened successfully. "
                                               "Please look in GitLab channel for more details ")

                return response_body
        except ProjectNotFoundE as project_not_found_error:
            log.error("Tried to open a new issue, but an error has occurred: "
                      f"{str(project_not_found_error).lower()}")
            self.handle_request_mattermost("Tried to open a new issue, but an error has occurred: "
                                           f"{str(project_not_found_error).lower()}. "
                                           "Please specify a correct project name")

            return project_not_found_error

    def close_i(self, body):
        """Closes a issue in the project"""
        try:
            project_id = self.get_project_id(body['project_name'])
            issue_id = self.get_issue_id(project_id, body['title'])

            url = f"{os.getenv('GITLAB_URL')}/projects/{project_id}/issues/{issue_id}"

            header = {'PRIVATE-TOKEN': os.getenv('GITLAB_TOKEN')}
            params = {
                'id': project_id,
                'issue_id': issue_id,
                'state_event': 'close'
            }

            response_body = self.handle_request_gitlab(url, params, header, "PUT")

            if "id" in response_body:
                self.handle_request_mattermost("The issue was closed successfully. "
                                               "Please look in GitLab channel for more details ")

                return response_body
        except ProjectNotFoundE as project_not_found_error:
            log.error("Tried to close the issue in a project, but an error has occurred: "
                      f"{str(project_not_found_error).lower()}")
            self.handle_request_mattermost("Tried to close the issue in a project, but an error has occurred: "
                                           f"{str(project_not_found_error).lower()}. "
                                           "Please specify a correct project name")

            return project_not_found_error
        except IssueNotFoundE as issue_not_found_error:
            log.error("Tried to close the issue in a project, but an error has occurred: "
                      f"{str(issue_not_found_error).lower()}")
            self.handle_request_mattermost("Tried to close the issue in a project, but an error has occurred: "
                                           f"{str(issue_not_found_error).lower()}. "
                                           "Please specify a correct issue title")

            return issue_not_found_error
