import concurrent
import json
import os
import time
import unittest
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from tests.test_api.test_articles import TestArticles
from tests.test_api.test_blogs import TestBlogs
from tests.test_api.test_info import TestInfo
from tests.test_api.test_reports import TestReports


##
class ContinueTestResult(unittest.TextTestResult):
    def addError(self, test, err):
        super().addError(test, err)
        # Do not stop the test suite upon an error
        return

    def addFailure(self, test, err):
        super().addFailure(test, err)
        # Do not stop the test suite upon a failure
        return



def run_test_suite(test_suite):
    runner = unittest.TextTestRunner(resultclass=ContinueTestResult)
    runner.run(test_suite)

suites = [
        unittest.TestLoader().loadTestsFromTestCase(TestReports),
        unittest.TestLoader().loadTestsFromTestCase(TestBlogs),
        unittest.TestLoader().loadTestsFromTestCase(TestArticles),
        unittest.TestLoader().loadTestsFromTestCase(TestInfo),
    ]
cur_dir = Path(__file__).resolve().parents[2].joinpath("config_api.json")

config_path = str(cur_dir)+'\\config_api.json'
with open(cur_dir, 'r') as config_file:
    config = json.load(config_file)
if __name__ == '__main__':
    start_time = time.time()
    if config["grid type"] == "parallel":
        # Run the test suites in parallel using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=config["grid size"]) as executor:
            future_to_test_case = {
                        executor.submit(run_test_suite, suite) for suite in suites
                    }

        for future in concurrent.futures.as_completed(future_to_test_case):
            test_case = future_to_test_case[future]
            try:
                future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (test_case, exc))

    elif config["grid type"] == "serial":
        for suite in suites:
            run_test_suite(suite)

    end_time = time.time()  # End timing
    total_time = end_time - start_time
    print(f"Total time to run all tests: {total_time:.2f} seconds")
