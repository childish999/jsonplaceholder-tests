import requests


def test_create_post_success(base_url):
    # 正常创建：完整字段
    response = requests.post(
        f"{base_url}/posts",
        json={"title": "我的第一篇测试帖", "body": "这是正文", "userId": 1},
        timeout=5,
    )
    assert response.status_code == 201, f"预期201，实际{response.status_code}"
    data = response.json()
    assert data["id"] == 101, f"预期id=101，实际{data['id']}"
    assert data["title"] == "我的第一篇测试帖"


def test_create_post_empty(base_url):
    # 行为基线用例：空对象照单全收，只回 id，不为缺失字段补默认值
    response = requests.post(
        f"{base_url}/posts",
        json={},
        timeout=5,
    )
    assert response.status_code == 201, f"预期201，实际{response.status_code}"
    data = response.json()
    assert data == {"id": 101}, f"预期只回id，实际{data}"
    assert "title" not in data, f"接口不应为缺失字段补默认值，实际返回{data}"