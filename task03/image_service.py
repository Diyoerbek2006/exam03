from api_client import APIClient


class ImageService:
    def __init__(self):
        self.api_client = APIClient()

    def fetch_random_image(self, animal: str) -> str:
        return self.api_client.get_image_url(animal)
