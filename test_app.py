import unittest
import sys
from selenium import webdriver

class FirstSampleTest(unittest.TestCase):
    # setUp runs before each test case 
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="https://zalenium:cF2tP7jA9bF8iN8a@zalenium.apps.dev.thebrewery.app/wd/hub",
            desired_capabilities=webdriver.DesiredCapabilities.CHROME)

		# tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        # try:
        driver = self.driver

        # Url
        driver.get("https://thebrewery-craft-templates.github.io/sample-todo/")

        # Click on check box
        check_box_one = driver.find_element_by_name("li1")
        check_box_one.click()

        # Click on check box
        check_box_two = driver.find_element_by_name("li2")
        check_box_two.click()

        # Enter item in textfield
        textfield = driver.find_element_by_id("sampletodotext")
        textfield.send_keys("Yey, Let's add it to list")

        # Click on add button
        add_button = driver.find_element_by_id("addbutton")
        add_button.click()

        # Verified added item
        added_item = driver.find_element_by_xpath(
            "//span[@class='done-false']").text
        print(added_item)


if __name__ == "__main__":
    unittest.main()
