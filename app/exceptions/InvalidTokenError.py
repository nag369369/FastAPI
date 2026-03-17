class InvalidTokenError(Exception):
    def __init__(self, message: str = "Invalid token provided"):
        self.message = message
        super().__init__(self.message)