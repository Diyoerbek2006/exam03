import requests


class APIClient:
    def get_image_url(self, api_type: str) -> str:
        if api_type == "dog":
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            data = response.json()
            return data["message"]

        elif api_type == "cat":
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            data = response.json()
            return data[0]["url"]

        elif api_type == "fox":
            response = requests.get("https://randomfox.ca/floof/")
            data = response.json()
            return data["image"]

        else:
            raise ValueError("Noto'g'ri api_type")
