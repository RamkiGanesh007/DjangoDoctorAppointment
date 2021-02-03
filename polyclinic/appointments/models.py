import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 100)
    specialization = models.CharField(max_length = 40)
    experience =models.IntegerField(default=True)

    def __str__(self):
        return 'Doctor {0}, {1},{2}'.format(self.name, self.specialization,self.experience)

    def appointments_month(self):
        today = datetime.datetime.today()
        return Appointment.objects.filter(
                appointment_time__year=today.year,
                appointment_time__month=today.month
                )


class Appointment(models.Model):
    # Age Gender PhoneNo Email Additional Info
    patient_name = models.CharField('Your name:', max_length=40)
    patient_middlename = models.CharField('Your middle name:', max_length=40)
    patient_surname = models.CharField('Your last name:', max_length=40)
    patient_age = models.IntegerField(null=False,validators=[MaxValueValidator(99),MinValueValidator(5)])
    # CHOICES = (('M','Male'),('F','Female'))
    # Gender=models.ChoiceField(choices=CHOICES, widget=models.RadioSelect)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=False)
    patient_mobile = models.IntegerField(null=False,validators=[MaxValueValidator(9999999999),MinValueValidator(6000000000)])
    patient_email = models.EmailField('Your Email Address:', max_length=40)
    patient_addinfo = models.TextField('Your Additional Info Here: ',max_length=200)
    doctor = models.ForeignKey(Doctor, verbose_name="Choose a doctor:",on_delete=models.DO_NOTHING)
    appointment_time = models.DateTimeField('Choose an Appointment date and time:')

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


