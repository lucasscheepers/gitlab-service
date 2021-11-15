class IssueNotFound(Exception):
    """Raised when the issue is not found

        Attributes:
        project id -- the id of the project
        title issue -- the title of the issue
    """

    def __init__(self, project_id, title_issue, message=""):
        self.project_id = project_id
        self.title_issue = title_issue
        self.message = message.join(f"The issue '{title_issue}' was not found in the project with "
                                    f"id number '{project_id}'")
        super().__init__(self.message)
