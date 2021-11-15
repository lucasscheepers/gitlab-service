class ProjectNotFound(Exception):
    """Raised when the project is not found

        Attributes:
        project name -- the name of the project
    """
    def __init__(self, project_name, message=""):
        self.project_name = project_name
        self.message = message.join(f"The project '{project_name}' was not found")
        super().__init__(self.message)
