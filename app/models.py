from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=50)
    dept_id=models.CharField(max_length=30)
    location=models.CharField(max_length=80)

    def __str__(self):
        return self.dept_id

class employee(models.Model):
    name=models.CharField(max_length=90)
    company=models.CharField(max_length=80)
    ctc=models.PositiveIntegerField()
    dept_id=models.ForeignKey(department,on_delete=models.PROTECT)
    class Meta:
        db_table="emplaoyee"