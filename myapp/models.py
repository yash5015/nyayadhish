from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models import Model
from datetime import date
# Create your models here.


class case(models.Model):
    Name_of_plaintiff_party = models.CharField(
        default="", blank=False, max_length=100)
    Name_of_defendant = models.CharField(
        default="", blank=False, max_length=100)
    Email_of_plaintiff = models.EmailField(default="")
    Email_of_defendant = models.EmailField(default="")
    Phone_No_of_plaintiff = models.CharField(
        default="", blank=False, max_length=11)
    Phone_No_of_defendant = models.CharField(
        default="", blank=False, max_length=11)
    Address_of_plaintiff = models.CharField(
        default="", blank=False, max_length=500)
    Address_of_defendant = models.CharField(
        default='', blank=False, max_length=500)
    section = models.CharField(max_length=50)
    chart_sheet_filling_date = models.DateField()
    case_No = models.CharField(max_length=100)
    case_type = models.CharField(max_length=100)
    case_statement = models.CharField(max_length=10000)
    last_hearing_date = models.DateField(default=date.today)
    gravity = models.IntegerField()

    def __str__(self):
        return self.case_No
