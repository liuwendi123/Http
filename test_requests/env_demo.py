"""
在请求之前，对请求的URL进行替换
1.需要二次封装requests,对请求进行定制化
2.将请求的结构体的URL从一个写死的IP地址改为一个（任意的）域名
3.使用一个env配置的文件，存放各个环境的配置信息。
4.然后将请求结构体中的URL替换为'env'配置文件中个人选择的URL
5.将env 配置文件使用yaml 进行管理
"""
import requests
import yaml


class Api:
	env = yaml.safe_load(open("env.yaml"))
	#data 是一个请求的信息
	def send(self,data:dict):
		##替换
		data["url"] = str(data["url"]).replace("testing-studio", self.env["testing-studio"][self.env["default"]])

		r = requests.request(method=data["method"],url=data["url"],headers=data["headers"])
		return r
