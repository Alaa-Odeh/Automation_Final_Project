import unittest

from infra.infra_web.browser_wrapper import BrowserWrapper
from logic.web_logic.home_page_pathfinder import PathfinderPage
from logic.web_logic.skill_test_page import SkillTestPage


class TestSkillTests(unittest.TestCase):
    def setUp(self):
        self.test_cases = [self.test_skill_assessment_python_answered_partially,self.test_full_skill_assessment_dsa_quiz]
        self.browser=BrowserWrapper()

    def test_run(self):
        if self.browser.config["grid"]:
            self.browser.build_cap()
            if self.browser.config["grid type"]=="serial":
                self.browser.test_grid_serial(self.test_cases,"first_user")
            if self.browser.config["grid type"]=="parallel":
                self.browser.test_grid_parallel(self.test_cases,"first_user")
        else:
            self.browser.run_single_browser(self.test_cases,self.browser.config["browser"],"first_user")

    def test_skill_assessment_python_answered_partially(self,driver):
        self.pathfinder_page = PathfinderPage(driver)
        self.skill_assessment_page=SkillTestPage(driver)
        self.pathfinder_page.click_on_tests_button()
        number_of_questions_to_answer=5
        self.skill_assessment_page.answer_test_questions(number_of_questions_to_answer)
        self.assertEqual(int(self.skill_assessment_page.get_number_of_questions_answered()),number_of_questions_to_answer)



    def test_full_skill_assessment_dsa_quiz(self,driver):
        self.pathfinder_page = PathfinderPage(driver)
        self.pathfinder_page.click_on_tests_button()
        self.skill_assessment_page=SkillTestPage(driver)
        quiz_not_completed=self.skill_assessment_page.answer_all_test_questions()
        quiz_after_completion=self.skill_assessment_page.get_test_history()
        self.assertIn(quiz_after_completion,quiz_not_completed,"The quiz is not completed")

