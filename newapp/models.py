from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class EmployeeData(models.Model):
    fullname = models.CharField(db_column='FullName', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    jobid = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='JobId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'EmployeeData'
    
    def __str__(self):
        return self.fullname




class Jobs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descar = models.CharField(db_column='DescAr', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    descen = models.CharField(db_column='DescEn', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Jobs'

    def __str__(self):
        return self.descen+'|'+self.descar
    
    def delete(self, *args, **kwargs):
        if self.employeedata_set.exists():
            raise ValidationError("This job is assigned to one or more employees and cannot be deleted.")
        super().delete(*args, **kwargs)