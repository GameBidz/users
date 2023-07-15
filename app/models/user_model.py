class User:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self) -> dict:
        return dict(username=self.username, email=self.email, password=self.password)
