from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddRecordForm, EditRecordByHeadOfDepartment
from .models import Department, Employee, EmployeeRole, Record
from users.models import User


def index(request):
    records = Record.objects.order_by('-interview_date')
    if not request.user.is_authenticated:
        return render(request, "index.html", {'records': records})
    else:
        redirect('login')
    check_user = Employee.objects.filter(employee=request.user)
    if not check_user:
        return render(request, "index.html", {'records': records})
    user_employee = get_object_or_404(Employee, employee=request.user)
    return render(request, "index.html", {'records': records, 'user_employee': user_employee})


def add_record(request):
    department = get_object_or_404(Department, department__employee=request.user)
    if department.id == 1:
        form = AddRecordForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'pages/add_record_page.html', {'form': form,})
    else:
        return render(request, 'error.html', {'department': department})


def record_edit(request, record_id):
    department = get_object_or_404(Department, department__employee=request.user)
    if department.id == 1:
        record = get_object_or_404(Record, id=record_id)
        form = AddRecordForm(
            request.POST or None,
            files=request.FILES or None,
            instance=record
        )
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'pages/add_record_page.html', {'form': form, 'record': record})
    else:
        return render(request, 'error.html', {'department': department})


def add_data(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    department = record.department
    user_eployee = get_object_or_404(Employee, employee=request.user)
    if user_eployee.employee_department == department and user_eployee.employee_role.id == 1:
        button = True
        form = EditRecordByHeadOfDepartment(
            request.POST or None,
            files=request.FILES or None,
            instance=record
        )
        if form.is_valid():
            form.instance.head_of_department_name = request.user
            form.save()
            return redirect('index')
        return render(request, 'pages/add_data_page.html', {'form': form, 'record': record, 'button': button})
    else:
        return render(request, 'error.html', {'department': department})


def page_not_found(request, exception):
    return render(
        request,
        'templates/misc/404.html',
        {'path': request.path},
        status=404
    )


def server_error(request):
    return render(request, 'templates/misc/500.html', status=500)
