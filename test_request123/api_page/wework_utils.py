
from test_request123.api_page.base_api import BaseApi


class WeWorkUtils(BaseApi):
	def _get_token(self,corpsecret,corpid = "ww9f8f12a7e4ebc373"):
		data = {
			"method": "get",
			"url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
			"params": {"corpid": corpid, "corpsecret": corpsecret}
		}

		result = self.send_api(data)
		return result["access_token"]