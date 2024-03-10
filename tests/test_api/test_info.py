import os
from unittest import TestCase
from infra.infra_api.api_wrapper import APIWrapper
from logic.api_logic.info import Info


class TestInfo(TestCase):
    def setUp(self):
        self.my_api=APIWrapper()
        self.url = self.my_api.url
        self.info=Info(self.my_api,self.url)


    def test_info_status(self):
        self.info.get_info()
        self.assertEqual(self.info.response.status_code,200)

    def test_info_structure(self):
        self.info.get_info()
        expected_result=['version', 'news_sites']
        actuall_result=list(self.info.result.keys())
        self.assertListEqual(expected_result,actuall_result)
