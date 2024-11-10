from django.contrib.auth.management.commands.createsuperuser import (
    Command as BaseCreateSuperuserCommand
)
from django.core.management import CommandError

from users.models import User
import getpass

class Command(BaseCreateSuperuserCommand):
    help = 'Create a super, using custom model fields'
    
    def add_arguments(self, parser):
        super().add_arguments(parser)
          
    def handle(self, *args, **options):
        username = input('Username: ')
        email = input('Email: ')
        password = getpass.getpass("Password: ")
        password_confirm = getpass.getpass("Password (again): ")
        birthday = input('Birthday: ')
        phone_number = input('Phone number: ')

        if not email:
            raise CommandError(_('Email field is required.'))
        
        
        if password != password_confirm:
            raise CommandError('Passwords don\'t match.')
        
        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(
                'Superuser or user with this email already exists.'
            ))
        
        User.objects.create_superuser(
            username=username,
            password=password,
            birthday=birthday,
            phone_number=phone_number,
            email=email
        )
        
        self.stdout.write(self.style.SUCCESS('Superuser created succesfully'))
        
        
