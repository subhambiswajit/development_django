# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RegistrationRegistrationprofile(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField(unique=True)
    activation_key = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class SocialAuthAssociation(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'


class SocialAuthCode(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=75, blank=True)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'


class SocialAuthNonce(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'


class SocialAuthUsersocialauth(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'


class StoreAuthor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'store_author'


class StoreBook(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=200)
    author_id = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'store_book'


class StoreBookorder(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    quantity = models.IntegerField()
    book = models.ForeignKey(StoreBook)
    cart = models.ForeignKey('StoreCart')

    class Meta:
        managed = False
        db_table = 'store_bookorder'


class StoreCart(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    active = models.IntegerField()
    order_date = models.DateField(blank=True, null=True)
    payment_type = models.CharField(max_length=100, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'store_cart'


class StoreReview(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    publish_date = models.DateField()
    text = models.TextField()
    book = models.ForeignKey(StoreBook)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'store_review'
