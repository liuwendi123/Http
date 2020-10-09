import requests

corpid = "ww9f8f12a7e4ebc373"
corpsecret = "5Ch82BN2bilhJvBtix9Ir10yNw51eYUaNjpRAtp9ZBk"
def get_token():
	url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
	#获取token
	result = (requests.get(url).json())
	return result["access_token"]

def test_get():
	token = get_token()
	url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=LiuWenDi"
	print(requests.get(url).json())

def test_add():
	token = get_token()
	url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
	data = {
		"userid": "zhangsi",
		"name": "张四",
		"mobile": "17272097209",
		"department": [1]
	}
	print(requests.post(url, json=data).json())
def test_delete():
	token = get_token()
	url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=zhangsi"
	print(requests.get(url).json())

def test_update():
	token = get_token()
	url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
	data = {
		"userid": "zhangsi",
		"name": "lalala"
	}
	print(requests.post(url, json=data).json())
