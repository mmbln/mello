# member/models.py
# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
    )

class MemberManager(BaseUserManager):
    def create_user(self,
                    login_name,
                    email,
                    full_name='',
                    member_img='',
                    password=None):
        email_ = self.normalize_email(email)
        user = self.model(login_name=login_name,
                          email=email_,
                          full_name = full_name,
                          image=member_img)
        if password:
            user.set_password(password)
        user.save()
        return (user)
    

    def create_superuser(self,
                         login_name,
                         email,
                         full_name='',
                         member_img='',
                         password=None):
        """
        creates a superuser
        """
        user = self.create_user(login_name,
                                email,
                                full_name = full_name,
                                member_img=member_img,
                                password=password)
        user.is_admin = True
        user.save()
        return(user)


STATUS_CHOICES=(
    ('en', 'Entered'),
    ('au', 'Authorized'),
    ('bl', 'Blocked'),
    ('pr', 'Password rocover'),
    ('il', 'Illegal')
)
    

class Member(AbstractBaseUser):
    login_name = models.CharField(max_length = 32,
                                  unique = True)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length = 64)
    status = models.CharField(max_length = 2,
                              choices=STATUS_CHOICES,
                              default='en')  # entered
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to='member')
    
    objects = MemberManager()

    USERNAME_FIELD = 'login_name'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.login_name

    
    
