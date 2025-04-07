import os
import sys
import django

def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "netfix.settings")
    django.setup()
    
    # Apply migrations
    from django.core.management import call_command
    print("Applying migrations...")
    call_command('makemigrations', 'users')
    call_command('makemigrations', 'services')
    call_command('makemigrations', 'main')
    call_command('migrate')
    
    # Create a superuser if none exists
    from users.models import User
    if not User.objects.filter(is_superuser=True).exists():
        print("Creating superuser...")
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )
        print("Superuser created successfully!")
    else:
        print("Superuser already exists")
    
    print("Database setup completed successfully!")

if __name__ == "__main__":
    main()
