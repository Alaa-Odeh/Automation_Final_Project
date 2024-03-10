class Reports:
    def __init__(self, api_object, url):
        self.api_object = api_object
        self.new_url = url + "reports/"

    def get_reports(self):
        self.response = self.api_object.api_get_request(self.new_url)
        self.result = self.response.json()

    def get_reports_by_id(self,reports_id):
        self.new_url=f"{self.new_url}{reports_id}/"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()

    def get_reports_search(self,search_text):
        search_text=search_text.replace(" ","%20")
        self.new_url = f"{self.new_url}?search={search_text}"
        response = self.api_object.api_get_request(self.new_url)
        self.result = response.json()
        self.result_search =self.result["results"]