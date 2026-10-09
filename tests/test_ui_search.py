# UI 测试：必应搜索（浏览器开关由 page fixture 代劳）

def test_bing_search(page):
    page.goto("https://cn.bing.com")
    page.locator("#sb_form_q").fill("接口测试")
    page.keyboard.press("Enter")
    page.wait_for_url("**q=**")
    assert "接口测试" in page.title(), f"预期标题含'接口测试'，实际{page.title()}"