class IsNotDirectoryError(Exception):
    def __init__(self, directory):
        self.directory = directory
        self.message = f"Directory {self.directory} dont exists"
        super().__init__(self.message)

class GroupExists(Exception):
    def __init__(self, groupName, new_url):
        self.groupName = groupName
        self.new_url = new_url
        self.message = f"Group {self.groupName} exists in the new instance {new_url}"
        super().__init__(self.message)

class InvalidPath(Exception):
    def __init__(self, path):
        self.path = path
        self.message = f"Path {self.path} must end with '/' (slash)"
        super().__init__(self.message)

class EmptyDirectory(Exception):
    def __init__(self, path):
        self.path = path
        self.message = f"Directory {self.path} is not empty"
        super().__init__(self.message)