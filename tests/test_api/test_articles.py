import concurrent
import os
import unittest
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from unittest import TestCase
from infra.infra_api.api_wrapper import APIWrapper
from logic.api_logic.articles import Articles


class TestArticles(TestCase):
    def setUp(self):
        self.my_api=APIWrapper()
        self.url = self.my_api.url
        self.articles=Articles(self.my_api,self.url)


    def test_article_status(self):
        self.articles.get_articles()
        self.assertEqual(self.articles.response.status_code,200)

    def test_articles_by_id(self):
        article_id = 22729
        self.articles.get_article_by_id(article_id)
        self.assertEqual(self.articles.result['id'],article_id)

    def test_articles_by_phrase(self):
        phrase = "Aerospace announced"
        self.articles.get_article_by_phrase_in_summary(phrase)
        self.assertIn(phrase,self.articles.result_summary)

    def test_article_has_event(self):
        self.articles.get_article_has_event()
        for article in self.articles.result_has_event:
            self.assertTrue(article['events'],f"The 'events' field is empty for article with id {article['id']}")

    def test_get_article_by_event_id(self):
        event_id=915
        self.articles.get_article_by_event_id(event_id)
        for article in self.articles.result_event:
            self.assertEqual(article['events'][0]['event_id'],event_id, f"The 'events' field is not correct for article with id {article['id']}")

    def test_articles_after_timestamp_included(self):
        timestamp_included = "2024-03-07T13:37:02.212000Z"
        timestamp = datetime.strptime(timestamp_included, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.articles.get_articles_updated_after_timestamp_included(timestamp_included)
        for article in self.articles.result_after_timestamp :
            try:
                article_timestamp = datetime.strptime(article['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                article_timestamp = datetime.strptime(article['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
            self.assertTrue(article_timestamp >= timestamp,
                          msg=f"Article ID {article['id']} was updated before the specified timestamp.")

