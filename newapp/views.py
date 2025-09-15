from django.shortcuts import redirect, reverse, HttpResponse,render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmployeeData,Jobs
from .forms import EmployeeForm,JobForm
from django.core.exceptions import ValidationError
from django.contrib import messages
import requests

#@login_required
def Employee_list(request):
    records=EmployeeData.objects.all()
    mydict={'records':records}
    return render(request,'Listingpage.html',context=mydict)



#@login_required
def AddEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Replace with your URL name for employee list view
    else:
        form = EmployeeForm()
    
    return render(request, 'Add.html', {'form': form})



#@login_required
def EditEmployee(request,id=None):
    one_rec=EmployeeData.objects.get(pk=id)
    form=EmployeeForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict= {'form':form}
    return render(request,'Edit.html',context=mydict)



#@login_required
def DeleteEmployee(request, eid):
    employee = get_object_or_404(EmployeeData, pk=eid)

    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')  # Redirect to the employee list view after deletion

    context = {
        'employee': employee,
    }
    return render(request, 'delete.html', context)


#@login_required
def ViewEmployee(request,eid=None):
    mydict={}
    one_rec = EmployeeData.objects.get(pk=eid)
    mydict['employee']=one_rec
    return render(request,'View.html',mydict)





#@login_required
def job_list(request):
    jobs = Jobs.objects.all()
    context = {'jobs': jobs}
    return render(request, 'Listingpage_jobs.html', context)


#@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            # Swap descar and descen fields
            form.cleaned_data['descar'], form.cleaned_data['descen'] = form.cleaned_data['descen'], form.cleaned_data['descar']
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    
    return render(request, 'Add_jobs.html', {'form': form})

#@login_required
def edit_job(request, id):
    job = get_object_or_404(Jobs, id=id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # Redirect to job list view
    else:
        form = JobForm(instance=job)

    return render(request, 'Edit_jobs.html', {'form': form})



#@login_required
def delete_job(request, id):
    job = get_object_or_404(Jobs, id=id)
    if request.method == 'POST':
        try:
            job.delete()
            messages.success(request, 'Job deleted successfully.')
        except ValidationError as e:
            messages.error(request, str(e))
        return redirect('job_list')

    context = {'job': job}
    return render(request, 'Delete_jobs.html', context)

#@login_required
def view_job(request, id):
    job = get_object_or_404(Jobs, id=id)
    context = {'job': job}
    return render(request, 'View_jobs.html', context)



#@login_required
# def get_announcements(request):
#     api_url = "https://announcementstest.sbg.com.sa/api/v1/Announcement/GetAllPagedList"
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     payload = {
#         "pageNumber": 0,
#         "pageSize": 5  # Adjust page size as needed
#     }
#
#     try:
#         response = requests.post(api_url, json=payload, headers=headers)
#         response.raise_for_status()  # Raises an HTTPError for bad responses
#
#         announcements = response.json()['data']['items']
#
#         # For debugging: print the announcements response to console or log
#         print("API Response:", announcements)
#
#         return render(request, 'announcements.html', {'announcements': announcements})
#
#     except requests.exceptions.RequestException as e:
#         # Handle exceptions
#         print("Error fetching announcements:", e)
#         announcements = []
#
#     return render(request, 'announcements.html', {'announcements': announcements})

def get_announcements(request):
    api_url = " "
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "title": "Test Title",
        "body": "Test Body",
        "userId": 1
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        announcement = response.json()  # It's a single object

        print("API Response:", announcement)
        return render(request, 'announcements.html', {'announcements': [announcement]})

    except requests.exceptions.RequestException as e:
        print("Error fetching announcements:", e)
        return render(request, 'announcements.html', {'announcements': []})