import os
from unittest import TestCase

from infra.infra_api.api_wrapper import APIWrapper
from logic.api_logic.reports import Reports


class TestReports(TestCase):
    def setUp(self):
        self.my_api=APIWrapper()
        self.url = self.my_api.url
        self.reports=Reports(self.my_api,self.url)

    def test_reports_status(self):
        self.reports.get_reports()
        self.assertEqual(self.reports.response.status_code,200)

    def test_reports_by_id(self):
        report_id = 1540
        self.reports.get_reports_by_id(report_id)
        self.assertEqual(self.reports.result['id'],report_id)

    def test_reports_in_title_or_summary(self):
        phrase="SpaceX Crew"
        self.reports.get_reports_search(phrase)
        for report in self.reports.result_search:
            for word in phrase:
                self.assertIn(word,report['title']+report['summary'],
                                 f"The 'title or summary field does not have {phrase} for report with id {report['id']}")
