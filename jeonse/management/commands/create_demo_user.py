from django.conf import settings
from django.core.management.base import BaseCommand

from apps.accounts.models import CustomUser


class Command(BaseCommand):
    help = "Creates Demo user"

    def handle(self, *args, **kwargs):
        email = settings.DEMO_USER_EMAIL
        password = settings.DEMO_USER_PASSWORD

        if email and password:
            if not CustomUser.objects.filter(email=email).exists():
                user = CustomUser.objects.create_user(email)
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
