import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    """
    setUp is a special unittest method that will run before each test
    """
    def setUp(self):
        self.browser = webdriver.Firefox()

    """
    tearDown is a special unittest method that will run after each test,
    even if there is an error during the test
    """
    def tearDown(self):
        self.browser.quit()

    """
    any method that begins with "test_" is a test method and will be run by
    the test runner
    """
    def test_can_start_a_todo_list(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        #She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)

        """
        self.fail("error message") fails no matter what and produces the error message passed to it
        """
        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        # She types "Buy peacokc feathers" into a text box:
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()