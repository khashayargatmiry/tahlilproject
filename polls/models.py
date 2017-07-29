from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Building(models.Model):
    postal_code = models.CharField(max_length=10 , primary_key=True)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    number = models.IntegerField()


class Apartment(models.Model):
    id = models.IntegerField(primary_key=True)
    building = models.ForeignKey('Building' , on_delete=models.CASCADE , null=True)
    floor = models.IntegerField()
    _owner = models.ForeignKey('Owner' , on_delete=models.CASCADE , null=True)
    main_neighbor = models.ForeignKey('Neighbor' , on_delete=models.CASCADE , null=True)

    class Meta:
        unique_together = ('building' , 'floor')

class Neighbor(models.Model):
    national_id = models.CharField(max_length=10 , primary_key=True)
    neighbor_name = models.CharField(max_length=100)
    neighbor_family_name = models.CharField(max_length=100)
    _apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE , default=0)
    username = models.CharField(max_length=30 , default='Untitiled')
    password = models.CharField(max_length=30 , default='123456')
    sex = models.CharField(max_length=5 , null=True)
    email = models.CharField(max_length=30 , null=True)
    type = models.CharField(max_length=30 , null=True)
    bank_account = models.CharField(max_length=30)
    _bank = models.ForeignKey('Bank' , on_delete=models.CASCADE)
    #neighbor_nationalId = models.IntegerField()

class Owner(models.Model):
    _apartment = models.ForeignKey('Apartment' , on_delete=models.CASCADE)
    national_id = models.CharField(max_length=10 , primary_key=True)

class Bank(models.Model):
    name = models.CharField(primary_key=True , max_length=20)


class Receipt(models.Model):
    receipt_number = models.IntegerField()
    _bank = models.ForeignKey('Bank' , on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField()

    class Meta:
        unique_together = ('receipt_number' , '_bank')

class Facility(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    _building = models.ForeignKey('Building' , on_delete=models.CASCADE , null=True)

    class Meta:
        unique_together = ('name' , '_building')


class Reservation(models.Model):
    neighbor = models.ForeignKey('Neighbor' , on_delete=models.CASCADE)
    facility = models.ForeignKey('Facility' , on_delete=models.CASCADE)
    duration = models.IntegerField(default=1)
    date_time = models.DateTimeField('date of reservation')

    class Meta:
        unique_together = ('neighbor' , 'facility' , 'date_time')

class Contract(models.Model):
    _owner = models.ForeignKey('Owner' , on_delete=models.CASCADE)
    tenant = models.ForeignKey('Neighbor' , on_delete=models.CASCADE)
    _apartment = models.ForeignKey('Apartment' , on_delete=models.CASCADE)
    payement_date = models.DateField('date for payement')
    payement = models.IntegerField(default=1000000)
    backup_payement = models.IntegerField(default=4000000)

    class Meta:
        unique_together = ('_owner' , 'tenant' , '_apartment')

class Dashboard(models.Model):
    _building = models.ForeignKey('Building' , on_delete=models.CASCADE)
    date_time = models.DateTimeField('notification date')
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=300)

    class Meta:
        unique_together = ('_building' , 'date_time')

class UnAvailableTimes(models.Model):
    facility = models.ForeignKey('Facility' , on_delete=models.CASCADE)
    date_time = models.DateTimeField('available times')

class Charge(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=300000)
    due_date = models.DateField('charge due date')
    is_payed = models.BooleanField(default=False)
    receipt = models.ForeignKey('Receipt' , on_delete=models.CASCADE , null=True)
    _apartment = models.ForeignKey('Apartment' , on_delete=models.CASCADE)

    class Meta:
        unique_together = ('due_date' , '_apartment')


class MonthlyPayment(models.Model):
    tenant = models.ForeignKey('Neighbor' , on_delete=models.CASCADE)
    owner = models.ForeignKey('Owner' , on_delete=models.CASCADE)
    due_date = models.DateField('date of payment')
    amount = models.IntegerField(default=2000000)
    is_payed = models.BooleanField(default=False)
    delay_time = models.IntegerField(default=0)

    class Meta:
        unique_together = ('due_date', 'tenant')


class Bill(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=300000)
    due_date = models.DateField('charge due date')
    is_payed = models.BooleanField(default=False)
    receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE, null=True)
    _apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('due_date', '_apartment')





class RequestLetter(models.Model):
    sender = models.ForeignKey('Neighbor' , related_name='polls_RequestLetter_related' ,
                               related_query_name='polls_RequestLetters')
    receiver = models.ManyToManyField('Neighbor')
    number = models.IntegerField(default=1)
    type = models.CharField(max_length=30)
    text = models.CharField(max_length=300)



class WarningLetter(models.Model):
    receiving_neighbor = models.ForeignKey('Neighbor', on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    text = models.CharField(max_length=300)

    class Meta:
        unique_together = ('receiving_neighbor' , 'number')




#class ApartmentForm(ModelForm):
#    class Meta:
#        model = Apartment
#        fields = ['number' , 'floor_num']