class Info:
    def __init__(self,api_object,url):
        self.api_object = api_object
        self.new_url = url+"info/"

    def get_info(self):
        self.response = self.api_object.api_get_request(self.new_url)
        self.result = self.response.json()
        self.news_sites=self.result["news_sites"]