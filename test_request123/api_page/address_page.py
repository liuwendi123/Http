import requests

from test_request123.api_page.base_api import BaseApi
from test_request123.api_page.wework_utils import WeWorkUtils


class AddressPage(BaseApi):
	"""
	通讯录管理增删改查
	"""




	def __init__(self):
		_corpsecret = "5Ch82BN2bilhJvBtix9Ir10yNw51eYUaNjpRAtp9ZBk"
		utils = WeWorkUtils()
		self.token =  utils._get_token(_corpsecret)


	def get_member_info(self):
		data = {
			"method": "get",
			"url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get",
			"params":  {"access_token": self.token, "userid":"zhangsi"}
        }
		return self.send_api(data)


	def add_member(self):
		data = {
			"method": "post",
			"url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
			"json":{"userid": "zhangsi","name": "张四","mobile": "17272097209","department": [1]}
		}
		return self.send_api(data)

	def delete_member(self):
		url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=zhangsi"
		data = {
			"method":"get",
			"url":f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid=zhangsi"
		}
		return self.send_api(data)

	def update_member(self):
		url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
		data = {
			"method":"post",
			"url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
			"json":{"userid": "zhangsi","name": "lalala"}
		}
		return self.send_api(data)
