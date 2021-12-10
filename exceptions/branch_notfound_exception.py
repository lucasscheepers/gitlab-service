class BranchNotFoundE(Exception):
    """Raised when the branch is not found

    Attributes:
    project id -- the id of the project
    branch name -- the name of the branch
    """
    def __init__(self, project_id, branch_name, message=""):
        self.project_id = project_id
        self.branch_name = branch_name
        self.message = message.join(f"The branch name '{branch_name}' was not found in the project with "
                                    f"id number '{project_id}'")
        super().__init__(self.message)
