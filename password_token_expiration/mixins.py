from time import time
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.utils.timezone import timedelta
import datetime
from django.utils.timezone import utc
from rest_framework import exceptions

class PasswordTokenMixin(models.Model):

    password_token_expiration_date = models.DateTimeField(('password_token_expiration_date'), default=timezone.now)
    password_token = models.TextField(null=True)
    def set_password_token(self):
        # ensuring its gonna be unique over time
        while True:
            allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            t = int( time() )
            stamp = ''
            while t:
                stamp += allowed_chars[t % 62]
                t = int( t / 62 )

            queryset = get_user_model().objects.all()
            key = get_random_string(34) + str(stamp)
            user = queryset.filter(password_token=key).first()
            if not user:
                break


        self.password_token_expiration_date = datetime.datetime.now() + timedelta(seconds = 5)
        if datetime.datetime.now() > self.password_token_expiration_date:
            raise self.password_token = None
        #self ...... = now() + settings.MY_CONSTANT_IN_SECONDS
        self.password_token = key
    
    def unset_password_token(self):
        # ensuring its gonna be unique over time
        self.password_token = None
    # def expire_password_token(self, key):
    #     utc_now = datetime.datetime.utcnow()
    #     if token.created < utc_now - datetime.timedelta(seconds=20):
    #         self.password_token = None
    def get_password_token(self):
        return self.password_token

    class Meta:
        abstract = True



# class PasswordTokenMixin(models.Model):
#     # password_token_expiration_date = models.DateTimeField(null=True)

#         # default=timezone.now() + timedelta(days=2),
#         # help_text=('Token expiration date'),
    
#     def token_expiration_date(self):
#         default=timezone.now() + timedelta(days=2)
    # password_token_expiration_date = models.DateTimeField(
    # default=timezone.now()+timedelta(days=2),
    # help_text=('Token expiration date'),
    # )


    # def token_expiration_date(self):