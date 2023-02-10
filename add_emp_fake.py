import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','office_emp_project.settings')

django.setup()

from emp_app.models import employee
from faker import Faker
from faker import *
import random

fake=Faker()

def phonenumbergen():
	d1=random.randint(7,9)
	num=''+str(d1)
	for i in range(8):
		num=num+str(random.randint(0,9))
	return int(num)


def populate(n):
	for i in range(n):
		pfirst_name=fake.first_name()
		plast_name=fake.last_name()
		pdept=fake.random_int(min=1,max=3)
		psalary=fake.random_int(min=10000,max=50000)
		pbonus=fake.random_int(min=1000,max=5000)
		prole=fake.random_int(min=1,max=4)
		pphno=phonenumbergen()
		phire_date=fake.date()
		emp_records=employee.objects.get_or_create(first_name=pfirst_name,last_name=plast_name,dept_id=pdept,salary=psalary,bonus=pbonus,role_id=prole,phno=pphno,hire_date=phire_date)
populate(30)
