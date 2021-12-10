import pytest

from exceptions.branch_notfound_exception import BranchNotFoundE
from exceptions.issue_notfound_exception import IssueNotFoundE
from exceptions.project_notfound_exception import ProjectNotFoundE
from exceptions.tag_notfound_exception import TagNotFoundE
from services.gitlab_service import GitLabService
from unittest import mock
from datetime import datetime
from tests.unit_tests import utils
import os


class TestGitlabService:

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_gitlab_api_down(self, mock_requests_get, mock_request_post):
        self.service = GitLabService()

        mock_requests_get.side_effect = utils.get_responses_gitlab_api_down()
        mock_request_post.return_value = utils.get_response_mattermost()

        start = datetime.now()
        self.service.handle_request_gitlab("http://None", None, None, "DOWN_SIMULATION")

        end = datetime.now()

        assert (end - start).total_seconds() >= 5

    @mock.patch('services.gitlab_service.requests.get')
    def test_get_project_id(self, mock_request_get):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_project_id()

        actual_result = self.service.get_project_id("Mattermost-Coffeebot")

        assert actual_result == 31240995

    @mock.patch('services.gitlab_service.requests.get')
    def test_get_project_id_exception(self, mock_request_get):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_issue_or_project_id_exception()

        with pytest.raises(ProjectNotFoundE):
            self.service.get_project_id("unknown-project")

    @mock.patch('services.gitlab_service.requests.get')
    def test_get_issue_id(self, mock_request_get):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_issue_id()

        actual_result = self.service.get_issue_id(31240995, "API_ERROR")

        assert actual_result == 6

    @mock.patch('services.gitlab_service.requests.get')
    def test_get_issue_id_exception(self, mock_request_get):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_issue_or_project_id_exception()

        with pytest.raises(IssueNotFoundE):
            self.service.get_issue_id(31240995, "unkown_issue")

    @mock.patch('services.gitlab_service.requests.get')
    def test_check_branch(self, mock_request_get):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_check_branch()

        actual_result = self.service.check_branch(31240995, "master")

        assert actual_result == "master"

    @mock.patch('services.gitlab_service.requests.get')
    def test_check_branch_exception(self, mock_request_get):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_check_branch_exception()

        with pytest.raises(BranchNotFoundE):
            self.service.check_branch(31240995, "unkown_branch")

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_create_mr(self, mock_requests_get, mock_requests_post):
        self.service = GitLabService()

        mock_requests_get.side_effect = [utils.get_response_project_id(), utils.get_response_check_branch(),
                                         utils.get_response_check_branch()]
        mock_requests_post.side_effect = [utils.get_response_create_mr(), utils.get_response_mattermost()]

        body = {
            'event_type': 'create_mr',
            'project_name': "Mattermost-Coffeebot",
            'title': "Test",
            'source_branch': "master",
            'target_branch': "dev"
        }

        actual_result = self.service.create_mr(body)

        assert actual_result['project_id'] == 31240995
        assert actual_result['title'] == "Test"
        assert actual_result['target_branch'] == "dev"
        assert actual_result['source_branch'] == "master"

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    def test_create_mr_exception_project(self, mock_request_get, mock_request_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_issue_or_project_id_exception()
        mock_request_post.return_value = utils.get_response_mattermost()

        body = {
            'event_type': 'create_mr',
            'project_name': "unknown-project",
            'title': "Test",
            'source_branch': "master",
            'target_branch': "dev"
        }

        actual_result = self.service.create_mr(body)

        assert actual_result.message == ProjectNotFoundE('unknown-project').message

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    def test_create_mr_exception_branch(self, mock_request_get, mock_request_post):
        self.service = GitLabService()

        mock_request_get.side_effect = [utils.get_response_project_id(), utils.get_response_check_branch(),
                                        utils.get_response_check_branch_exception()]
        mock_request_post.return_value = utils.get_response_mattermost()

        body = {
            'event_type': 'create_mr',
            'project_name': "Mattermost-Coffeebot",
            'title': "Test",
            'source_branch': "master",
            'target_branch': "unknown-branch"
        }

        actual_result = self.service.create_mr(body)

        assert actual_result.message == BranchNotFoundE(31240995, 'unknown-branch').message

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    def test_create_mr_exception_already_exists(self, mock_request_get, mock_requests_post):
        self.service = GitLabService()

        mock_request_get.side_effect = [utils.get_response_project_id(), utils.get_response_check_branch(),
                                        utils.get_response_check_branch()]
        mock_requests_post.side_effect = [utils.get_response_mr_already_exists(), utils.get_response_mattermost()]

        body = {
            'event_type': 'create_mr',
            'project_name': "Mattermost-Coffeebot",
            'title': "Test",
            'source_branch': "master",
            'target_branch': "dev"
        }

        actual_result = self.service.create_mr(body)

        assert actual_result == "Another open merge request already exists for this source branch"

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_create_r(self, mock_request_get, mock_requests_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_project_id()
        mock_requests_post.side_effect = [utils.get_response_create_r(), utils.get_response_mattermost()]

        body = {
            'event_type': 'create_r',
            'project_name': "Mattermost-Coffeebot",
            'title': "Test",
            'tag_name': "v4.0",
        }

        actual_result = self.service.create_r(body)

        assert actual_result['name'] == "Test"
        assert actual_result['tag_name'] == "v4.0"

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_create_r_exception_tag(self, mock_request_get, mock_requests_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_project_id()
        mock_requests_post.side_effect = [utils.get_response_create_r_tagnotfound(), utils.get_response_mattermost()]

        body = {
            'event_type': 'create_r',
            'project_name': "Mattermost-Coffeebot",
            'title': "Test",
            'tag_name': "unknown-tag",
        }

        actual_result = self.service.create_r(body)

        assert actual_result.message == TagNotFoundE(31240995, 'unknown-tag').message

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_create_r_exception_project(self, mock_request_get, mock_request_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_issue_or_project_id_exception()
        mock_request_post.return_value = utils.get_response_mattermost()

        body = {
            'event_type': 'create_r',
            'project_name': "unknown-project",
            'title': "Test",
            'tag_name': "v4.0",
        }

        actual_result = self.service.create_r(body)

        assert actual_result.message == ProjectNotFoundE("unknown-project").message

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_create_r_exception_already_exists(self, mock_request_get, mock_requests_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_project_id()
        mock_requests_post.side_effect = [utils.get_response_create_r_already_exists(), utils.get_response_mattermost()]

        body = {
            'event_type': 'create_r',
            'project_name': "Mattermost-Coffeebot",
            'title': "Test",
            'tag_name': "v4.0",
        }

        actual_result = self.service.create_r(body)

        assert actual_result == "Release already exists"

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_create_i(self, mock_request_get, mock_requests_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_project_id()
        mock_requests_post.side_effect = [utils.get_response_create_i(), utils.get_response_mattermost()]

        body = {
            'event_type': 'create_i',
            'project_name': "Mattermost-Coffeebot",
            'title': "test_title",
            'description': "test_description",
        }

        actual_result = self.service.create_i(body)

        assert actual_result['project_id'] == 31240995
        assert actual_result['title'] == "test_title"
        assert actual_result['description'] == "test_description"

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_create_i_exception_project(self, mock_request_get, mock_request_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_issue_or_project_id_exception()
        mock_request_post.return_value = utils.get_response_mattermost()

        body = {
            'event_type': 'create_i',
            'project_name': "unknown-project",
            'title': "test_title",
            'description': "test_description",
        }

        actual_result = self.service.create_i(body)

        assert actual_result.message == ProjectNotFoundE('unknown-project').message

    @mock.patch('services.gitlab_service.requests.put')
    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_close_i(self, mock_requests_get, mock_request_post, mock_request_put):
        self.service = GitLabService()

        mock_requests_get.side_effect = [utils.get_response_project_id(), utils.get_response_issue_id()]
        mock_request_post.return_value = utils.get_response_mattermost()
        mock_request_put.return_value = utils.get_response_close_i()

        body = {
            'event_type': 'close_i',
            'project_name': "Mattermost-Coffeebot",
            'title': "API_ERROR"
        }

        actual_result = self.service.close_i(body)

        assert actual_result['project_id'] == 31240995
        assert actual_result['title'] == "API_ERROR"
        assert actual_result['description'] == "test_description"

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_close_i_exception_project(self, mock_request_get, mock_request_post):
        self.service = GitLabService()

        mock_request_get.return_value = utils.get_response_issue_or_project_id_exception()
        mock_request_post.return_value = utils.get_response_mattermost()

        body = {
            'event_type': 'close_i',
            'project_name': "unknown-project",
            'title': "API_ERROR"
        }

        actual_result = self.service.close_i(body)

        assert actual_result.message == ProjectNotFoundE('unknown-project').message

    @mock.patch('services.gitlab_service.requests.post')
    @mock.patch('services.gitlab_service.requests.get')
    @mock.patch.dict(os.environ, {"MATTERMOST_URL": "http://None"})
    def test_close_i_exception_issue(self, mock_requests_get, mock_request_post):
        self.service = GitLabService()

        mock_requests_get.side_effect = [utils.get_response_project_id(),
                                         utils.get_response_issue_or_project_id_exception()]
        mock_request_post.return_value = utils.get_response_mattermost()

        body = {
            'event_type': 'close_i',
            'project_name': "Mattermost-Coffeebot",
            'title': "unknown-issue"
        }

        actual_result = self.service.close_i(body)

        assert actual_result.message == IssueNotFoundE(31240995, 'unknown-issue').message
