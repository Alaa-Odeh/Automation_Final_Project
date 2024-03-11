class Articles:
    def __init__(self,api_object,url):
        self.api_object = api_object
        self.new_url = url+"articles/"

    def get_articles(self,limit=20):
        self.new_url = f"{self.new_url}?limit={limit}"
        self.response = self.api_object.api_get_request(self.new_url)
        self.result = self.response.json()

    def get_article_by_id(self,article_id):
        self.new_url=f"{self.new_url}{article_id}/"
        self.result = self.api_object.api_get_request(self.new_url).json()



    def get_article_by_phrase_in_summary(self,phrase_in_summary):
        words_in_phrase=phrase_in_summary.replace(" ",'%20')
        self.new_url=f"{self.new_url}?summary_contains={words_in_phrase}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_summary=self.result["results"][0]['summary']

    def get_article_has_event(self):
        self.new_url=f"{self.new_url}?has_event=true"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_has_event=self.result["results"]

    def get_articles_updated_after_timestamp_included(self,timestamp_excluded):
        timestamp_excluded=timestamp_excluded.replace(":","%3A")
        self.new_url=f"{self.new_url}?updated_at_gte={timestamp_excluded}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_after_timestamp = self.result["results"]

    def get_article_by_event_id(self,event_id=915):
        self.new_url=f"{self.new_url}?event={event_id}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_event = self.result["results"]
