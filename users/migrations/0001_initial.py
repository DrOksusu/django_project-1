# Generated by Django 3.2.25 on 2024-10-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=30)),
                ('disp_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'user-role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Media_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'media_file',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedicalStatistics_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('진료일', models.CharField(max_length=20)),
                ('차트번호', models.CharField(max_length=20)),
                ('이름', models.CharField(max_length=50)),
                ('보험구분', models.CharField(max_length=50)),
                ('수입집계', models.CharField(max_length=50)),
                ('진료의사', models.CharField(max_length=50)),
                ('어시스트', models.CharField(max_length=50)),
                ('당일접수', models.CharField(max_length=20)),
                ('수납자', models.CharField(max_length=50)),
                ('총진료비', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('청구액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('본인부담금', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('비급여', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('부가가치세', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('할인액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('총수납액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('카드수납', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('현금수납', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('기타_온라인', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('현영발행액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('건강생활유지비승인', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('미수_선수', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('총미수_선수', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('진료비구분', models.CharField(blank=True, max_length=50, null=True)),
                ('진료내역', models.TextField(blank=True, null=True)),
                ('메모', models.TextField(blank=True, null=True)),
                ('최초내원', models.CharField(blank=True, max_length=20, null=True)),
                ('내원경로', models.CharField(blank=True, max_length=50, null=True)),
                ('고객성향', models.CharField(blank=True, max_length=50, null=True)),
                ('고객구분', models.CharField(blank=True, max_length=50, null=True)),
                ('고객구분2', models.CharField(blank=True, max_length=50, null=True)),
                ('리콜구분', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'medical_statistics_1',
                'managed': True,
                'unique_together': {('진료일', '차트번호')},
            },
        ),
        migrations.CreateModel(
            name='MedicalStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('진료일', models.CharField(max_length=20)),
                ('차트번호', models.CharField(max_length=20)),
                ('이름', models.CharField(max_length=50)),
                ('보험구분', models.CharField(max_length=50)),
                ('수입집계', models.CharField(max_length=50)),
                ('진료의사', models.CharField(max_length=50)),
                ('어시스트', models.CharField(max_length=50)),
                ('당일접수', models.CharField(max_length=20)),
                ('수납자', models.CharField(max_length=50)),
                ('총진료비', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('청구액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('본인부담금', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('비급여', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('부가가치세', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('할인액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('총수납액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('카드수납', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('현금수납', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('기타_온라인', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('현영발행액', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('건강생활유지비승인', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('미수_선수', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('총미수_선수', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('진료비구분', models.CharField(blank=True, max_length=50, null=True)),
                ('진료내역', models.TextField(blank=True, null=True)),
                ('메모', models.TextField(blank=True, null=True)),
                ('최초내원', models.CharField(blank=True, max_length=20, null=True)),
                ('내원경로', models.CharField(blank=True, max_length=50, null=True)),
                ('고객성향', models.CharField(blank=True, max_length=50, null=True)),
                ('고객구분', models.CharField(blank=True, max_length=50, null=True)),
                ('고객구분2', models.CharField(blank=True, max_length=50, null=True)),
                ('리콜구분', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'medical_statistics',
                'managed': True,
                'unique_together': {('진료일', '차트번호')},
            },
        ),
    ]
