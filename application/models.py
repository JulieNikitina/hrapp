from django.db import models
from users.models import User


class Department(models.Model):
    department_name = models.TextField(
        verbose_name='наименование отдела',
        blank=False,
        max_length=100)

    def __str__(self):
        return self.department_name


class EmployeeRole(models.Model):
    role = models.TextField(
        verbose_name='наименование должности',
        blank=False,
        max_length=100)

    def __str__(self):
        return self.role


class Employee(models.Model):
    employee = models.ForeignKey(
        User, verbose_name='Сотрудник',
        on_delete=models.CASCADE,
        related_name='worker'
    )
    employee_department = models.ForeignKey(
        Department,
        verbose_name='Наименование отдела',
        on_delete= models.PROTECT,
        related_name='department'
    )
    employee_role = models.ForeignKey(
        EmployeeRole,
        verbose_name='Должность сотрудника',
        on_delete=models.PROTECT,
        related_name='position')

    def __str__(self):
        return f' {self.employee.get_full_name()} {self.employee_role} {self.employee_department}'


class Record(models.Model):
    applicant_name = models.TextField(
        verbose_name='ФИО соискателя',
        blank=False,
        max_length=100
    )
    phone_number = models.TextField(
        verbose_name='Телефон соискателя',
        blank=False,
        max_length=11
    )
    position = models.TextField(
        verbose_name='Вакансия',
        blank=False,
        max_length=30)
    department = models.ForeignKey(
        Department,
        verbose_name='Наименование отдела',
        on_delete=models.PROTECT,
        related_name='applicant_department',
        blank=False)
    interview_date = models.DateField(
        verbose_name='дата выдачи тестового задания',
        help_text='Пожалуйста, используйте поддерживаемый формат: ДД-ММ-ГГГГ'
    )
    time_to_complete = models.PositiveIntegerField(
        verbose_name='Время на выполнение задания'
    )
    department_hr = models.ForeignKey(
        Department,
        verbose_name='Название отдела, проводившего собеседование',
        on_delete=models.PROTECT,
        related_name='hr_department',
        blank=False,
    )
    name_hr = models.ForeignKey(
        Employee,
        verbose_name='ФИО сотрудника, проводившего собеседование',
        on_delete=models.PROTECT,
        blank=False,
        max_length=100
    )
    position_hr = models.ForeignKey(
        EmployeeRole,
        verbose_name='Должность сотрудника, проводившего собеседование',
        on_delete=models.PROTECT,
        blank=False,
        max_length=100
    )
    date_of_get = models.DateTimeField(
        verbose_name='Дата получения результата тестового задания',
        blank=True,
        null=True)
    head_of_department_name = models.ForeignKey(
        User,
        verbose_name='ФИО руководителя подразделения,'
                     'получившего результат тестового задания',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
