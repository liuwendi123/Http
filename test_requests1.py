import requests
import base64
import json
def test_demo():
	url = "https://httpbin.testing-studio.com/cookies"
	header = {
	    'User-Agent': 'hogwarts'
	     }
	cookie_data = {
		"hogwarts":"school",
		"teacher" : "AD"
	}
	r= requests.get(url= url, headers = header,cookies= cookie_data)
	print(r.request.headers)
