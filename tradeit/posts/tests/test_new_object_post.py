import pytest
from posts.models import Post
from users.models import User



@pytest.mark.django_db
def test_create_new_object_post(user_test_instance):
    data = {
    'name': 'New Slug object',
    'price': 1,
    'category': 'cars',
    'user': user_test_instance
    }

    obj = Post.objects.create(**data)
    assert isinstance(obj, Post)
    
@pytest.mark.django_db
def test_post_object_attributes(user_test_instance):
    data = {
    'name': 'New Slug object',
    'price': 1,
    'category': 'cars',
    'user': user_test_instance
    }
    obj = Post.objects.create(**data)
    for key in data.keys():
        assert getattr(obj, key) == data[key]
        
        

        
