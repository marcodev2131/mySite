import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_list_view(client):
    url = reverse('post_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Post List' in response.content.decode()