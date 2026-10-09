import requests


def test_delete_created_post(created_post_id, base_url):
    # 删除 fixture 创建的帖子
    response = requests.delete(f"{base_url}/posts/{created_post_id}", timeout=5)
    assert response.status_code == 200, f"预期200，实际{response.status_code}"


def test_lifecycle_on_fake_api(base_url):
    # 生命周期：创建 → 删除 → 查询
    # 假接口行为基线：POST 不真存，DELETE 演成功
    response = requests.post(
        f"{base_url}/posts",
        json={"title": "生命周期测试", "body": "test", "userId": 1},
        timeout=5,
    )
    new_id = response.json()["id"]

    response = requests.delete(f"{base_url}/posts/{new_id}", timeout=5)
    assert response.status_code == 200, f"预期200，实际{response.status_code}"

    response = requests.get(f"{base_url}/posts/{new_id}", timeout=5)
    assert response.status_code == 404, f"假接口不真存，预期404，实际{response.status_code}"