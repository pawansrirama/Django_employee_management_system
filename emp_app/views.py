from django.shortcuts import render
from django.http import HttpResponse
from .models import employee,role,department
from datetime import datetime
from django.db.models import Q
import time

# Create your views here.
def employee_view(request):
	return render(request,'emp_app/index.html')

def all_emp(request):
	emps=employee.objects.all()
	context={'emps':emps}
	return render(request,'emp_app/all_emp.html',context)


def add_emp(request):
	if request.method=="POST":
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		salary=int(request.POST['salary'])
		bonus=int(request.POST['bonus'])
		phno=int(request.POST['phno'])
		dept=int(request.POST['dept'])
		role=int(request.POST['role'])
		new_emp=employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phno=phno,dept_id=dept,role_id=role,hire_date=datetime.now())
		new_emp.save()
		return HttpResponse('employee added successfully')

	elif request.method=="GET":
		return render(request,'emp_app/add_emp.html')

	else:
		return HttpResponse('exception occured sorry employee not added')

def del_emp(request,emp_id=0):

	if emp_id:
		try:
			emp_removed=employee.objects.get(id=emp_id)
			emp_removed.delete()

			return render(request,'emp_app/index.html')
		except:
			return HttpResponse('please enter vaild inputs')

	emps=employee.objects.all()
	context={
		'emps':emps
	}
	return render(request, 'emp_app/del_emp.html',context)

def filter_emp(request):
	if request.method == "POST":
		name=request.POST['name']
		dept=request.POST['dept']
		role=request.POST['role']
		emps=employee.objects.all()
		if name:
			emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
		if dept:
			emps = emps.filter(dept__name=dept)
		if role:
			emps=emps.filter(role__name = role)
		context= {
			'emps':emps
		}
		return render(request,'emp_app/all_emp.html',context)

	elif request.method=="GET" :
		return render(request,'emp_app/filter_emp.html')
	else:
		return HttpResponse('an exception occured')