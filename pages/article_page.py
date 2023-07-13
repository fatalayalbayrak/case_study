from selenium.webdriver.common.by import By
from base.base_page import *


class ArticlePage(BasePage):
    TITLE = (By.CLASS_NAME, 'article__title')
    BODY = (By.CSS_SELECTOR, 'div.article-content')

    def __init__(self, driver):
        super().__init__(driver)

    def get_article_title(self):
        """
        The function returns the text of the article title.
        :return: the text of the article title.

        """
        return self.get_text(self.TITLE)

