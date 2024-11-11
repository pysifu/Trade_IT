import pytest
from django.urls import reverse
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
    new_obj = Post.objects.get(**data)
    
    assert post_response.status_code == 302 # successful redirect
    assert new_obj is not None
    assert new_obj.status == 2

    
@pytest.mark.django_db
def test_panel_edit_pending_item(client,
                                 superuser_test_instance,
                                 post_test_instance):
    '''
    Checks if update panel view properly changing attribute is_approved
    '''
    obj = post_test_instance
    client.login(username='test_admin', password='admin')
    url = reverse('posts:panel_edit_pending', args=[obj.slug])
    data = {'status': 1}
    response = client.post(url, data)
    obj.refresh_from_db()
    
    assert response.status_code == 302
    assert obj.status == 1