import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")   # 改后：给 base_url 换正确的户口(scope="session")   # 改后：给 base_url 换正确的户口
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")   # 改后：给 base_url 换正确的户口(scope="session")   # 改后：给 base_url 换正确的户口
def created_post_id(base_url):          # fixture 也能依赖另一个 fixture（链式）
    response = requests.post(
        f"{base_url}/posts",
        json={"title": "fixture 造的帖子", "body": "test", "userId": 1},
        timeout=5,
    )
    new_id = response.json()["id"]
    print(f"\n[setup] 已创建帖子 {new_id}")
    yield new_id
    requests.delete(f"{base_url}/posts/{new_id}", timeout=5)
    print(f"[teardown] 已清理帖子 {new_id}")

  #  pytest test_posts.py test_lifecycle_day04.py - -html = report.html - -self - contained - html --reruns 2