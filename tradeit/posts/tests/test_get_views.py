import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_home_page_status_view(client):
    '''
    Checks home_page response status 
    '''
    url = reverse('posts:home')
    response = client.get(url)

    assert response.status_code == 200
   
@pytest.mark.django_db 
def test_create_post_status_view(client, user_test_instance):
    '''
    Checks create_post response status
    '''
    url = reverse('posts:create_post')
    client.login(username='test_user', password='Testuser13!')
    response = client.get(url)
    assert response.status_code == 200
    

@pytest.mark.django_db
def test_post_status_and_check_retrieved_object_view(client, 
                                                     post_test_instance):
    '''
    Checks post status and retrieved object
    '''
    obj = post_test_instance
    url = reverse('posts:post', args=[obj.slug])
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'TestObject' in response.content.decode()
    

@pytest.mark.django_db
def test_panel_denied_access_by_user_view(client, user_test_instance, post_test_instance):
    '''
    Checks panel management view if access is denied for no authorized users
    '''
    client.login(username='test_user', password='Testuser13!')
    obj = post_test_instance
    links = [('posts:panel_pendings', {}),
             ('posts:panel_history', {}), 
             ('posts:panel_edit_pending', {'args': [obj.slug]}),
             ]
    for link, kwargs in links:
        url = reverse(link, **kwargs)
        response = client.get(url)
        assert response.status_code == 403
        
        
@pytest.mark.django_db
def test_staff_and_admin_panel_access_view(client, 
                                           post_test_instance,
                                           superuser_test_instance, 
                                           staff_user_test_instance):
    '''
    Checks panel management view if access is provide for authorized users
    '''
    obj = post_test_instance
    users = {
        'admin': {'username': 'test_admin', 'password': 'admin'},
        'staff': {'username': 'test_staff', 'password': 'staff'},
    }
    for kwargs in users.values():
        client.login(**kwargs)
        links = [
            ('posts:panel_pendings', {}),
            ('posts:panel_history', {}),
            ('posts:panel_edit_pending', {'args': [obj.slug]})
        ]
        for link, kwargs in links:
            url = reverse(link, **kwargs)
            response = client.get(url)
            assert response.status_code == 200