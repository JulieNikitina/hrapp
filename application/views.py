from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddRecordForm, EditRecordByHeadOfDepartment
from .models import Department, Employee, EmployeeRole, Record


def index(request):
    records = Record.objects.order_by('-interview_date')
    return render(request, "index.html", {'records': records})


def add_record(request):
    form = AddRecordForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'add_record.html', {'form': form})


def record_edit(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = AddRecordForm(
        request.POST or None,
        files=request.FILES or None,
        instance=record
    )
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'add_record.html', {'form': form, 'record': record})


def add_data(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    form = EditRecordByHeadOfDepartment(
        request.POST or None,
        files=request.FILES or None,
        instance=record
    )
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'add_data.html', {'form': form, 'record': record})