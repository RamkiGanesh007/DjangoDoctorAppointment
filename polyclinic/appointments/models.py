import datetime
from django.db import models

# Create your models here.

class Doctor(models.Model):
    
    name = models.CharField(max_length = 100)
    specialization = models.CharField(max_length = 40)

    def __str__(self):
        return 'Doctor {0}, {1}'.format(self.name, self.specialization)

    def appointments_month(self):
        today = datetime.datetime.today()
        return Appointment.objects.filter(
                appointment_time__year=today.year,
                appointment_time__month=today.month
                )


class Appointment(models.Model):

    patient_name = models.CharField('Your name:', max_length=40)
    patient_middlename = models.CharField('Your middle name:', max_length=40)
    patient_surname = models.CharField('Your last name:', max_length=40)
    doctor = models.ForeignKey(Doctor, verbose_name="Choose a doctor:")
    appointment_time = models.DateTimeField('Appointment date and time:')

    def __str__(self):
        return '[{0} {1} {2} made an appointment with {3}, {4} on {5}'.format(
                self.patient_name,
                self.patient_middlename,
                self.patient_surname,
                self.doctor.name,
                self.doctor.specialization,
                self.appointment_time)

    def get_absolute_url(self):
            return "/"


