class Login:
    def __init__(self, page):
        self.page = page
        self.username_locator = "//input[@placeholder='Enter your mail']"
        self.password_locator = "//input[@placeholder='Enter your password ']"
        self.submit_btn_locator = "//button[@type='submit']"

    def login(self):
        self.page.locator(self.username_locator).fill("namrata")
        self.page.locator(self.password_locator).fill("ABC@234")
        self.page.locator(self.submit_btn_locator).click()
        self.page.wait_for_timeout(15000)