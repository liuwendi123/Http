import requests
from jsonpath import jsonpath
from hamcrest import *
class TestDemo:
	def test_get(self):
		r = requests.get('https://httpbin.testing-studio.com/get')
		print(r.status_code)
		print(r.text)
		print(r.json())
		assert r.status_code == 200

	def test_query(self):
		payload = {
			"level": 1,
			"name": "seveniruby"
		}
		r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
		print(r.text)
		assert r.status_code == 200


	def test_post(self):
		payload = {
			"level": 1,
			"name": "seveniruby"
		}
		r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
		print(r.text)
		assert r.status_code == 200

	def test_header(self):
		r = requests.get('https://httpbin.testing-studio.com/get',headers={"h": "header demo"})
		print(r.status_code)
		print(r.text)
		print(r.json())
		assert r.status_code == 200
		assert r.json()['headers'] ["H"] == "header demo"

	def test_postjie(self):
		payload = {
			"firstName": "张三",
            "city": {"code":"360100","value":"南昌市"}
		}
		r = requests.post('https://oral-test.colgate-zhongan.cn/api/fedweb/user/member/info/submit/1.0.0', data=payload)
		print(r.text)
		assert r.status_code == 200

	def test_post_json(self):
		payload = {
			"level": 1,
			"name": "seveniruby"
		}
		r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
		print(r.text)
		assert r.status_code == 200
		assert r.json()['json']['level'] == 1

	def test_hogewozi_json(self):
		r = requests.get('https://ceshiren.com/categories.json')
		print(r.text)
		assert r.status_code == 200
		assert r.json()['category_list']['categories'][0]['name'] == '社区治理'
		#print(jsonpath(r.json(), '$..name'))
		assert jsonpath(r.json(), '$..name')[0] == '社区治理'

	def test_hamcrest(self):
		r = requests.get('https://ceshiren.com/categories.json')
		print(r.text)
		assert r.status_code == 200
		assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('社区治理'))