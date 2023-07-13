from selenium.webdriver.common.by import By
from base.base_page import *


class HomePage(BasePage):
    ARTICLES = (By.CLASS_NAME, "post-block--unread")
    AUTHOR_NAMES = (By.CLASS_NAME, "river-byline__authors")
    IMAGES = (By.XPATH, ".//*[contains (@class, 'post-block--unread')]//*[contains (@class, 'post-block__media')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://techcrunch.com/")

    def check_images_present(self):
        """
        The function checks if all images on webpage for articles are displayed.
        :return: a boolean value. It returns True if all the images are displayed, and False if at least one image is not
        displayed.

        """
        images = self.driver.find_elements(*self.IMAGES)
        for image in images:
            if not image.is_displayed():
                return False

        return True

    def check_author_names_present(self):
        """
        The function checks if author names are present and displayed on webpage for articles.
        :return: a boolean value indicating whether the author names are displayed or not.

        """
        articles = self.driver.find_elements(*self.ARTICLES)
        for article in articles:
            author_names = article.find_element(*self.AUTHOR_NAMES)
            return author_names.is_displayed()

    def click_element(self, index=0):
        """
        The function `click_element` finds a list of elements on the web page and clicks on the element at the specified
        index.

        :param int index: The `index` parameter is used to specify which element to click. It is an optional parameter with a
        default value of 0. If no index is provided, the first element in the list of elements will be clicked, defaults to
        0

        """

        elements = self.driver.find_elements(*self.ARTICLES)
        if index < 0 or index >= len(elements):
            raise IndexError("Undefined Index!")

        element = elements[index]
        element.click()
