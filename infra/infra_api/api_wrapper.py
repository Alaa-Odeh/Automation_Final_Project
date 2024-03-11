import json

import requests

class APIWrapper(object):
    def __init__(self):
        self.response=None
        self.my_request=requests
        config_path = '../../config_api.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.url = self.config["news"]

    def api_get_request(self,url):
        self.response=self.my_request.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self,url,body):
        self.response=self.my_request.post(url,body)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code
