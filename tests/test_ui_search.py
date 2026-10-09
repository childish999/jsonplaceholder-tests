# UI 测试：必应搜索（浏览器开关由 page fixture 代劳）

def test_bing_search_english(page, bing_page):
    bing_page.search("Playwright")
    assert "Playwright" in page.title(), f"预期标题含'Playwright'，实际{page.title()}"


def test_bing_search(page, bing_page):            # 测试直接收对象，连 BingPage(page) 都省了
    bing_page.search("接口测试")
    assert "接口测试" in page.title(), f"预期标题含'接口测试'，实际{page.title()}"
