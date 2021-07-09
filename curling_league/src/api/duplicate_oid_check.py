
class DuplicateOid(Exception):
    def __init__(self, prop):
        super().__init__()
        self.message = f"This OID +{prop} already exists!"
        self.oid = prop
