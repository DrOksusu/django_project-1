
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class UserRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    role_name = models.CharField(max_length=30)
    disp_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user-role'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_email = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=100, blank=True, null=True)
    role = models.ForeignKey(UserRole, models.DO_NOTHING, db_column='role')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'users'

class Media_file(models.Model):    
    file = models.FileField(upload_to='') # 빈디렉토리는 현재 media 폴더에 저장되는 것으로 설정(settings.py에서 설정한 경로)
    description = models.CharField(max_length=255, blank=True, null=True) #null 허용
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        managed = True        
        db_table = 'media_file'

class MedicalStatistics_2(models.Model):
    treatment_date = models.CharField(max_length=20)  # 필드 이름에 공백이 없어야 합니다
    chart_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    insurance_classification = models.CharField(max_length=50)
    income_aggregation = models.CharField(max_length=50)
    treating_doctor = models.CharField(max_length=50)
    assist = models.CharField(max_length=50)
    same_day_reception = models.CharField(max_length=20)
    recipient = models.CharField(max_length=50)
    total_medical_expenses = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    out_of_pocket_expenses = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    non_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount_received = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    card_storage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cash_receipt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_online = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    prefectural_issued_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    disapproval_for_healthy_lifestyle = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unexpected_player = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_number_of_outstanding_players = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    classification_of_medical_expenses = models.CharField(max_length=50, null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    first_visit = models.CharField(max_length=20, null=True, blank=True)
    visit_path = models.CharField(max_length=50, null=True, blank=True)
    customer_propensity = models.CharField(max_length=50, null=True, blank=True)
    customer_classification = models.CharField(max_length=50, null=True, blank=True)
    customer_classification_2 = models.CharField(max_length=50, null=True, blank=True)
    recall_classification = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'medical_statistics_2'
        unique_together = (('treatment_date', 'chart_number'),)  # 여기도 필드명을 수정해야 함      

 