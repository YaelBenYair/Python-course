

class FileTexrExceptions(Exception):
    pass

class FileNameExistsEror(FileTexrExceptions):
    def __init__(self, name_file):
        super().__init__(f"The file {name_file} already exists")