from locust import HttpUser, task

# Service Read Non-Idempoten
class Stress_Test(HttpUser):
	@task
	def get_data(self):
		self.client.get("/read/1806205022/")

# Service Read Idempoten
class Stress_Test(HttpUser):
	@task
	def get_data(self):
		self.client.get("/read/1806205022/1/")