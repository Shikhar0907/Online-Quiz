from selenium import webdriver
import time
import unittest

class test_site(unittest.TestCase):

    def setUp(self):
        self.driver =driver = webdriver.Chrome(r"C:\Users\as\Desktop\Udemy_Course\Handy_Project\Handy_project\Test\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://localhost:8000/loginpage/")

    def test_login(self):
        self.driver.find_element_by_name('name').send_keys('Suar')
        self.driver.find_element_by_name('email').send_keys('suan1@gmail.com')
        self.driver.find_element_by_id('id_services_0').click()
        self.driver.find_element_by_name('Submit').click()
        time.sleep(3)

    def quiz_test(self):
        self.driver.find_element_by_css_selector("input[type='radio'][value='2012']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][value='handyperson or handyworker, is a person skilled at a wide range of repairs, typically around the home.']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][value='$15 to $20']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][value='Baby care']").click()
        self.driver.find_element_by_css_selector("input[type='radio'][value='No']").click()
        self.driver.find_element_by_name('Submit').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()