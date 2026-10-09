import pytest
import requests


def test_get_post_1(base_url):
    response = requests.get(f"{base_url}/posts/1", timeout=5)
    assert response.status_code == 200, f"预期200，实际{response.status_code}"
    data = response.json()
    assert data["id"] == 1, f"预期id=1，实际{data['id']}"
    assert data["userId"] == 1
    assert "title" in data


@pytest.mark.parametrize("post_id", [0, -1, 999, "abc", 999999])
def test_get_post_not_exist(post_id, base_url):
    response = requests.get(f"{base_url}/posts/{post_id}", timeout=5)
    assert response.status_code == 404, f"post_id={post_id} 预期404，实际{response.status_code}"


@pytest.mark.parametrize("post_id, expected_status", [
    (1, 200),
    (50, 200),
    (0, 404),
    (999999, 404),
], ids=["post-1", "post-50", "id-0", "id-huge"])
def test_get_post_status(post_id, expected_status, base_url):
    response = requests.get(f"{base_url}/posts/{post_id}", timeout=5)
    assert response.status_code == expected_status, \
        f"post_id={post_id} 预期{expected_status}，实际{response.status_code}"


def test_get_all_posts(base_url):
    response = requests.get(f"{base_url}/posts", timeout=5)
    assert response.status_code == 200
    data = response.json()


    assert len(data) == 100