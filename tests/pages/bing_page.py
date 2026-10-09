class BingPage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.locator("#sb_form_q")

    def search(self,keyword):
        self.page.goto("https://cn.bing.com")
        self.search_box.fill(keyword)
        self.page.keyboard.press("Enter")
        self.page.wait_for_url("**q=**")

