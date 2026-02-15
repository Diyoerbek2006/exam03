from handlers import Handlers


class ImageBot:
    def __init__(self, token: str):
        self.token = token
        self.handlers = Handlers()
