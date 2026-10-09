from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://cn.bing.com")
#
#     page.locator("#sb_form_q").fill("接口测试")
#     page.keyboard.press("Enter")
#
#     page.wait_for_url("**q=**")      # 聪明等法：等网址里出现 q= 再继续
#     print("搜索后标题:", page.title())
#     assert "接口测试" in page.title(), f"预期标题含'接口测试'，实际{page.title()}"
#
#     page.screenshot(path="search_result.png")
#     browser.close()
#
# print("C-2 搜索自动化跑通！")
# # from playwright.sync_api import sync_playwright
# #
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    print(page.get_by_role("button", name="百度一下").get_attribute("id"))

#     page.locator("#chat-textarea").fill("接口测试")
#     page.get_by_role("button", name="百度一下").click()
#     # page.locator("#ci-submit-button").click()
#     # page.keyboard.press("Enter")
#     # print("当前网址:", page.url)
#     # page.wait_for_url("**wd=**")    # 等结果页真的到了，再继续往下读标题
#     page.wait_for_timeout(3000)  # 笨办法：硬等 3 秒，让一切跳转尘埃落定
#     print("等待后网址:", page.url)
#     print("等待后标题:", page.title())
#     page.screenshot(path="debug.png")  # 拍现场照片
#     print("搜索后标题：",page.title())
#     assert "接口测试" in page.title(),f"预期标题含'接口测试'，实际{page.title()}"
#
#     page.screenshot(path="search_result.png")
    browser.close()
#
# print("C-2 搜索自动化跑通！")
# #sb_form_q
#search_icon > svg > circle

#ci-submit-button
#chat-textarea
# with sync_playwright() as p:
#     browser = p.chromium.launch(channel="msedge", headless=False)
#     page = browser.new_page()
#     page.goto("https://www.baidu.com")
#
#     title = page.title()
#     print(page.content()[:200])
#     print("页面标题:", title)
#     assert "百度" in title,f"预期标题含'百度'，实际{title}"
#
#     page.screenshot(path="baidu.png")
#     browser.close()
#
# print("UI 自动化第一跑成功！")

#启动引擎
#开浏览器
#开页面
# 访问百度
# 取标题断言
# 截图关闭
