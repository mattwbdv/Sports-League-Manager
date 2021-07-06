
class DuplicateEmail(Exception):
    def __init__(self, prop):
        super().__init__()
        self.ivar = f"This email +{prop} already exists!"
        self.email = prop
