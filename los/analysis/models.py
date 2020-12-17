from django.db import models
from django_pandas.managers import DataFrameManager


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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


class Encounter(models.Model):
    provider_org = models.CharField(db_column='Provider_Org', max_length=40)  # Field name made lowercase.
    ecounter_id = models.CharField(db_column='Ecounter_ID', primary_key=True, max_length=40)  # Field name made lowercase.
    member_id = models.CharField(db_column='Member_ID', max_length=40)  # Field name made lowercase.
    provider_id = models.CharField(db_column='Provider_ID', max_length=40)  # Field name made lowercase.
    provider_npi = models.CharField(db_column='Provider_NPI', max_length=40)  # Field name made lowercase.
    clinic_id = models.CharField(db_column='Clinic_ID', max_length=65)  # Field name made lowercase.
    encounter_datetime = models.DateTimeField(db_column='Encounter_DateTime')  # Field name made lowercase.
    encounter_description = models.CharField(db_column='Encounter_Description', max_length=90)  # Field name made lowercase.
    cc = models.CharField(max_length=90)
    episode_id = models.CharField(db_column='Episode_ID', max_length=25)  # Field name made lowercase.
    patient_dob = models.DateField(db_column='Patient_DOB')  # Field name made lowercase.
    patient_gender = models.CharField(db_column='Patient_Gender', max_length=10)  # Field name made lowercase.
    facility_name = models.CharField(db_column='Facility_Name', max_length=20)  # Field name made lowercase.
    provider_name = models.CharField(db_column='Provider_Name', max_length=30)  # Field name made lowercase.
    speciality = models.CharField(db_column='Speciality', max_length=30)  # Field name made lowercase.
    clinic_type = models.CharField(db_column='Clinic_Type', max_length=20)  # Field name made lowercase.
    lab_orders_count = models.IntegerField(db_column='Lab_orders_count')  # Field name made lowercase.
    lab_results_count = models.IntegerField(db_column='Lab_results_count')  # Field name made lowercase.
    medication_orders_count = models.IntegerField()
    medication_fulfillment_count = models.IntegerField()
    vital_sign_count = models.IntegerField()
    therapy_orders_count = models.IntegerField()
    therapy_actions_count = models.IntegerField()
    immunization_count = models.IntegerField()
    has_appt = models.IntegerField(db_column='Has_Appt')  # Field name made lowercase.
    soap_note = models.CharField(db_column='SOAP_Note', max_length=1600)  # Field name made lowercase.
    consult_ordered = models.CharField(max_length=20)
    disposition = models.CharField(db_column='Disposition', max_length=30)  # Field name made lowercase.

    objects = DataFrameManager()

    class Meta:
        managed = False
        db_table = 'encounter'


class TestTable(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.

    objects = DataFrameManager()

    class Meta:
        managed = False
        db_table = 'test_table'
