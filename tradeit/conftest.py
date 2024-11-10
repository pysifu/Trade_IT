import pytest
from django.conf import settings
from posts.models import Post
from users.models import User

@pytest.fixture(scope='session')
def django_db_setup():
	settings.DATABASES['default'] = {
		'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_tradeit',
        'USER': 'tradeit',
        'PASSWORD': 'toor', 
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
        'TEST':{
            'NAME': 'test_db_tradeit',
        },
    }
 

@pytest.fixture
def post_test_instance(db):
    instance = Post.objects.create(
        name='TestObject',
        price=10,
        category='cars',
        user=User.objects.first()
    )
    return instance


@pytest.fixture
def superuser_test_instance(db):
    instance = User.objects.create_superuser(
        username='test_admin',
        email='admin@test.pl',
        phone_number='133123123',
        birthday='2000-01-01',
        password='admin'
    )
    return instance

@pytest.fixture
def staff_user_test_instance(db):
    instance = User.objects.create_user(
        username='test_staff',
        email='staff@test.pl',
        phone_number='137123123',
        birthday='2000-01-01',
        password='staff'
    )
    instance.is_staff = True
    instance.save()
    
    return instance


@pytest.fixture
def user_test_instance(db):
    instance = User.objects.create_user(
        username='test_user',
        email='user1@test.pl',
        phone_number='133123123',
        birthday='2000-01-01',
        password='Testuser13!'
    )
    return instance

