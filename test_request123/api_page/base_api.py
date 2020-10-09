import json

import requests


class BaseApi:
	"""
	api抽象
	"""



	def set(self, params):
		self.session = requests.session()
		self.session.params = params



	def send_api(self,data: dict):
		"""
		发送API
		"""
		print(json.dumps(data, indent=2))#锁进打印
		return requests.request(**data).json()