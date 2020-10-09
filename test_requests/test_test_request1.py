from unittest import TestCase

from test_requests import test_request1

class TestApiRequest(TestCase):
	req_data = {
		"method":"get",
		"url":"http://127.0.0.1:9999/demo.txt",
		"headers":None,
		"encoding":"base64"
	}
	def test_send(self):
		ar = test_request1.ApiRequest()
		print(ar.send(self.req_data))