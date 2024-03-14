import os
import unittest
from unittest import TestCase
from infra.infra_api.api_wrapper import APIWrapper
from logic.api_logic.blogs import Blogs


class TestBlogs(TestCase):
    def setUp(self):
        self.my_api=APIWrapper()
        self.url = self.my_api.url
        self.blogs=Blogs(self.my_api,self.url)

    def test_blogs_status(self):
        self.blogs.get_blogs()
        self.assertEqual(self.blogs.response.status_code,200)

    def test_blogs_by_id(self,blogs_id = 1240):
        self.blogs.get_blogs_by_id(blogs_id)
        self.assertEqual(self.blogs.result['id'],blogs_id)

    def test_blogs_has_launch(self):
        self.blogs.get_blogs_has_launch()
        for blog in self.blogs.result_has_launch:
            self.assertTrue(blog['launches'],f"The 'launches' field is empty for blogs with id {blog['id']}")

    def test_blogs_with_launch_id(self,launch_id='942a1814-c237-41de-9970-d27bb9630f3b'):
        self.blogs.get_blogs_with_launch_id(launch_id)
        for blog in self.blogs.result_launch_id:
            self.assertEqual(blog['launches'][0]['launch_id'],launch_id,f"The 'launches' field is empty for blogs with id {blog['id']}")

    def test_blogs_phrase_in_title(self,phrase_in_title="Mars"):
        self.blogs.get_blogs_titles_contains_phrase(phrase_in_title)
        for blog in self.blogs.result_title:
            self.assertIn(phrase_in_title,blog['title'],
                             f"The 'title field does not have Mars for blogs with id {blog['id']}")


    def test_blogs_with_news_site(self,news_site="Planetary Society"):
        self.blogs.get_blogs_in_news_site(news_site)
        for blog in self.blogs.result_news_site:
            self.assertEqual( blog['news_site'], news_site,
                          f"The 'news_site field does not have Match for blogs with id {blog['id']}")


    @unittest.skip("Skipping this test")
    def test_blogs_with_title_in_news_site(self,news_site="Planetary Society",title="Mars"):

        self.blogs.get_blogs_with_titles_in_news_site(news_site,title)
        for blog in self.blogs.result:
            self.assertIn(title,blog['title'],f"The 'title field does not have Mars for blogs with id {blog['id']}")
            self.assertEqual(blog['news_site'], news_site,
                             f"The 'news_site field does not have Match for blogs with id {blog['id']}")


