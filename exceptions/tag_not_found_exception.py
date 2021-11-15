class TagNotFound(Exception):
    """Raised when the tag is not found

    Attributes:
    project id -- the id of the project
    tag name -- the name of the tag
    """
    def __init__(self, project_id, tag_name, message=""):
        self.project_id = project_id
        self.tag_name = tag_name
        self.message = message.join(f"The tag name '{tag_name}' was not found in the project with "
                                    f"id number '{project_id}'")
        super().__init__(self.message)
