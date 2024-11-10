import pytest
from django.urls import reverse
from users.models import User
from posts.models import Post

@pytest.mark.django_db
def test_create_new_post_object(client, user_test_instance):
    '''
    Creates new object from form and response 
    '''
    client.login(username='test_user', password='Testuser13!')
    data = {
        'name': 'TestObject',
        'price': 10,
        'category': 'cars',
        'user': user_test_instance,
    }
    url = reverse('posts:create_post')
    post_response = client.post(url, data)

    assert post_response.status_code == 302 # successful redirect
    assert Post.objects.filter(**data)
    