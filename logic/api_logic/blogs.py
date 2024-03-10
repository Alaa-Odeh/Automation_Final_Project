class Blogs:
    def __init__(self,api_object,url):
        self.api_object = api_object
        self.new_url = url+"blogs/"

    def get_blogs(self):
        self.response = self.api_object.api_get_request(self.new_url)
        self.result = self.response.json()

    def get_blogs_by_id(self,blogs_id):
        self.new_url=f"{self.new_url}{blogs_id}/"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
    def get_blogs_has_launch(self):
        self.new_url = f"{self.new_url}?has_launch=true"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_has_launch = self.result["results"]

    def get_blogs_with_launch_id(self,launch_id):
        self.new_url = f"{self.new_url}?launch={launch_id}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_launch_id =self.result["results"]

    def get_blogs_titles_contains_phrase(self,phrase_in_title):
        words=phrase_in_title.replace(' ','%20')
        self.new_url = f"{self.new_url}?title_contains={words}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_title = self.result["results"]

    def get_blogs_in_news_site(self,news_site):
        words=news_site.replace(' ','%20')
        self.new_url =f"{self.new_url}?news_site={words}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_news_site = self.result["results"]

    def get_blogs_with_titles_in_news_site(self,news_site,in_title):
        in_title = in_title.replace(' ','%20')
        news_site = news_site.replace(' ','%20')
        self.new_url = f"{self.new_url}?news_site={news_site}&?title_contains={in_title}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()["results"]



