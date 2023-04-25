# In locust.py

from locust import HttpUser, task, constant
import random

class QuickstartUser(HttpUser):
    wait_time = constant(0) #wait_time is the amount of time the program waits after each request. With constant(0), then the program won’t wait at all after each request. If you use between(1,5) for example, then the program will wait a random number from 1 to 5 seconds after each request.
    host = "http://example.com"

    @task(5)
    def test_get_method(self):
        self.client.get("/articles/?article_id=1")

    @task
    def test_post_method(self):
        self.client.post("/articles/", {
			"title" : "A Title",
			"content" : "content!",
			"author_name" : "Mario",
        })

    @task
    def test_put_method(self):
            self.client.put("/articles/", {
			"id" : "3",
			"title" : "Title is Updated!",
			"content" : f"Your lucky number: {random.randint(0,9)}!",
			"author_name" : "Mario 2",
		})
        
    def on_start(self):
        self.client.post("/login", {"username":"foo", "password":"bar"})