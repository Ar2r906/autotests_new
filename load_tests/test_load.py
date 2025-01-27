import random
import lorem
from locust import HttpUser, between, task

mass_image = [
    'png', 'svg', 'jpg', 'jpeg', 'gif', 'PNG', 'JPG', 'JPEG', 'GIF'
]



class LoadTest(HttpUser):
    host = "http://localhost:3000"
    wait_time = between(5, 10)

    # @task(1)
    # def add_news(self):
    #     text = lorem.text()
    #     payload = {
    #         "title": lorem.paragraph(),
    #         "content": text,
    #         # "image": f"src/images/image{random.randint(1,100000)}.{random.choice(mass_image)}",
    #     }
    #
    #     response = self.client.post('/api/news/create_news', data=payload)
    #     if response.status_code == 201:
    #         return "CREATED!"
    #     else:
    #         return "FAILED!"

    @task(1)
    def add_articles(self):
        text = lorem.text()
        payload = {
            "title": lorem.paragraph(),
            "content": text,
            # "image": f"src/images/image{random.randint(1,100000)}.{random.choice(mass_image)}",
        }

        response = self.client.post('/api/articles/create_articles', data=payload)
        if response.status_code == 201:
            return "CREATED!"
        else:
            return "FAILED!"