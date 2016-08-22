
from django.apps import AppConfig

class PasswordTokenExpirationConfig(AppConfig): # Our app config class
    name  = 'password_token_expiration'
    label = 'token_expiration'
    verbose_name = "Password Token Expiration"