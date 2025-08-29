import pytest
import django

from blog.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

@pytest.mark.django_db
def test_create_post():
    post = PostFactory()
    assert post.title.startswith('Post')

def test_django_version():
    assert django.get_version() == '5.2.5'  # replace with your expected Django version