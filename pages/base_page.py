from config.utils.logger import get_logger

class BasePage:
    def __init__(self, page):
        self.page = page
        self.logger = get_logger("UI_BasePage")

    def navigate(self, url):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def click(self, locator):
        self.logger.info(f"Clicking on {locator}")
        self.page.locator(locator).click()
        
    def fill(self, locator, text):
        self.logger.info(f"Filling {locator} with text")
        self.page.locator(locator).fill(text)