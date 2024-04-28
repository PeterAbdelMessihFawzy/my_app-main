from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
  wait_time = between(1, 2)  # Time between requests

  @task
  def index(self):
    self.client.get("/")  # Simulate accessing the homepage

  @task(weight=2)  # Make login requests twice as often
  def login(self):
    # Implement login logic using self.client.post
    pass

  def on_start(self):
    # Optional setup tasks
    pass
