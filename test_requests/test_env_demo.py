from unittest import TestCase
from test_requests import env_demo

class TestApi(TestCase):
	data = {
		"method": "get",
		"url": "http://testing-studio:9999/demo.txt",
		"headers": None
	}

	def test_send(self):
		api = env_demo.Api()
		print(api.send(self.data).text)