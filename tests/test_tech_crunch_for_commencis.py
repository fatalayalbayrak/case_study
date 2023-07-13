import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.article_page import ArticlePage


class TestTechCrunchForCommencis(unittest.TestCase):
    """Test case is:
      1. Open main page
      2. Check Article Authors visible or not
      3. Click first Article
      4. Open Article page and Check Browser Title and Article Title is matched or not
      5. 5-Check Browser Title and Article Title is matched or not

    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_tech_crunch_for_commencis(self):
        """The test checks Article author images visible or not and Article and Browser Title is match or not"""
        self.assertLogs("1-Open main page")
        home_page = HomePage(self.driver)

        self.assertLogs("Check Article Authors visible or not!")
        author_names_present = home_page.check_author_names_present()
        self.assertTrue(author_names_present, "Article Authors couldn't find!")

        self.assertLogs("2-Check Images are visible or not!!")
        images_present = home_page.check_images_present()
        self.assertTrue(images_present, "Images couldn't find!")

        self.assertLogs("3-Click first Article!")
        home_page.click_element()

        self.assertLogs("4-Open Article page and Check Browser Title and Article Title is matched or not!")
        article_page = ArticlePage(self.driver)

        self.assertLogs("5-Check Browser Title and Article Title is matched or not!")
        browser_title = self.driver.title
        article_title = article_page.get_article_title()
        self.assertEqual(browser_title, article_title, "The browser title does not match the article title.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
