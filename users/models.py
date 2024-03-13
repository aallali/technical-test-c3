from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField('username', unique=True)
    is_beta_player = models.BooleanField("Is beta player", default=False)
    is_company_user = models.BooleanField("Is company user", default=False)
    is_growth_user = models.BooleanField("Is growth user", default=False)
