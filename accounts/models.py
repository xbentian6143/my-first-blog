from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(max_length=10, blank=True, null=True)
    icon = models.ImageField(upload_to='images' ,blank=True, null=True)
    introduction = models.CharField(max_length=75, blank=True, null=True)
    follower = models.ManyToManyField('User', related_name='followers', blank=True,symmetrical=False )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Connection(models.Model):
    #フォローする人
    followed_user = models.ForeignKey(get_user_model(), related_name="followed_user", on_delete=models.CASCADE)
    #フォローされた人
    followed_target = models.ForeignKey(get_user_model(), related_name="followed_target", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
