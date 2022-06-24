from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from uuid import uuid4
class Command(BaseCommand):
    help = "Creates Demo user"

    def handle(self, *args, **kwargs):
        email = settings.DEMO_USER_EMAIL
        password = settings.DEMO_USER_PASSWORD

        if email and password:
            if not get_user_model().objects.filter(email=email).exists():
                user = get_user_model().objects.create_user(email=email, username=uuid4().hex)
                user.set_password(password)
                user.save()
            self.stdout.write(
                self.style.SUCCESS(f"Demo user created: email: `{email}`!")
            )
        else:
            self.stdout.write(
                self.style.ERROR(
                    "`DEMO_USER_EMAIL` and `DEMO_USER_PASSWORD` haven't been provided!"
                )
            )
