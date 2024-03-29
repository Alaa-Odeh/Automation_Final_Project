import concurrent.futures
import datetime
import json
from pathlib import Path
import time
import unittest
import logging

from infra.infra_api.api_wrapper import APIWrapper
from tests.test_api.test_articles import TestArticles
from tests.test_api.test_blogs import TestBlogs
from tests.test_api.test_info import TestInfo
from tests.test_api.test_reports import TestReports


class ContinueTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_wrapper = APIWrapper()
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def addError(self, test, err):
        super().addError(test, err)
        # Log the error to Jira
        error_msg = self._exc_info_to_string(err, test)
        try:
            self.api_wrapper.create_issue(f"{test.id()} generated an error at {self.current_time}", error_msg, "FAP")
        except Exception as e:
            logging.error(f"Failed to create issue in Jira for error: {e}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        # Log the failure to Jira without calling the superclass method
        error_msg = str(err[1])
        self.api_wrapper.create_issue(f"{test.id()} failed at {self.current_time}", error_msg, "FAP")


def run_individual_test(test):
    suite = unittest.TestSuite([test])
    runner = unittest.TextTestRunner(resultclass=ContinueTestResult)
    runner.run(suite)


if __name__ == '__main__':
    api_wrapper = APIWrapper()
    start_time = time.time()

    test_classes = [TestReports, TestBlogs, TestArticles, TestInfo]

    all_test_cases = []
    for test_class in test_classes:
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        for test_case in test_suite:
            all_test_cases.append(test_case)

    cur_dir = Path(__file__).resolve().parents[2].joinpath("config_api.json")
    with open(cur_dir, 'r') as config_file:
        config = json.load(config_file)

    if config["grid type"] == "parallel":
        with concurrent.futures.ThreadPoolExecutor(max_workers=config["grid size"]) as executor:
            future_to_test = {executor.submit(run_individual_test, test): test for test in all_test_cases}

            for future in concurrent.futures.as_completed(future_to_test):
                test = future_to_test[future]
                try:
                    future.result()
                except Exception as e:
                    logging.error(f"Test execution or issue logging failed: {e}")
    elif config["grid type"] == "serial":
        for test in all_test_cases:
            run_individual_test(test)

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time to run all tests: {total_time:.2f} seconds")
