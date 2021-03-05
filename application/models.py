from django.db import models
from users.models import User


class Department(models.Model):
    department_name = models.TextField('наименование отдела', blank=False, max_length=100)

    def __str__(self):
        return self.department_name


class EmployeeRole(models.Model):
    role = models.TextField('наименование должности', blank=False, max_length=100)

    def __str__(self):
        return self.role


class Employee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='where_work')
    employee_role = models.ForeignKey(EmployeeRole, on_delete=models.PROTECT)

    def __str__(self):
        return self.employee.get_full_name()


class Record(models.Model):
    applicant_name = models.TextField('ФИО соискателя', blank=False, max_length=100)
    phone_number = models.TextField('телефон соискателя', blank=False, max_length=11)
    position = models.TextField('должность', blank=False, max_length=30)
    department = models.ForeignKey(Department, 'подразделение', related_name='applicant_department', blank=False)
    interview_date = models.DateField('дата выдачи тестового задания')
    time_to_complete = models.PositiveIntegerField('время на выполнение задания')
    department_hr = models.ForeignKey(Department, 'название отдела, проводившего собеседование', related_name='hr_department', blank=False,)
    name_hr = models.ForeignKey(Employee, 'ФИО сотрудника, проводившего собеседование', blank=False, max_length=100)
    position_hr = models.ForeignKey(EmployeeRole, 'должность сотрудника, проводившего собеседование', blank=False, max_length=100)
    date_of_get = models.DateTimeField('дата получения результата тестового задания', blank=True, null=True)
    head_of_department_name = models.TextField('ФИО руководителя подразделения, получившего результат тестового задания', blank=True, null=True, max_length=100)




