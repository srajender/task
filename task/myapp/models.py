from django.db import models
from django import forms
from django.db.models import Sum,Avg,Count,Max,Min

# Create your models here.

type=(('C','credit'),('D','debit'),)

class Customer(models.Model):
	account_number		=	models.CharField(max_length=10,unique=True)
	customer_name		=	models.CharField(max_length=100)
	date_of_open		=	models.DateField(auto_now_add=True)
	mail_id 			=	models.EmailField(max_length=100,null=True,blank=True)
	mobile_number		=	models.CharField(max_length=10,null=True,blank=True)
	address				=	models.TextField()
	balance 			=	models.DecimalField(max_digits=20,decimal_places=2,default=0.00)

	def __str__(self):
		return self.account_number
		
class TransactionManager(models.Manager):
	def average(self,accno):
		return super(TransactionManager,self).get_queryset().filter(customer__account_number__exact=accno).aggregate(Avg("amount"))

	def average_of_all(self):
		return super(TransactionManager,self).get_queryset().aggregate(Avg("amount"))

class Transaction(models.Model):
	transaction_type    =	models.CharField(max_length=1,choices=type,default='C',help_text='select transaction type')
	transaction_date	= 	models.DateField(auto_now_add=True)
	amount				=	models.DecimalField(max_digits=20,decimal_places=2,default=0.00,help_text='enter amount')
	customer 			=	models.ForeignKey(Customer,on_delete=models.CASCADE)
	manager 			=	TransactionManager()

	def __str__(self):
		return self.customer.account_number
		
class TransactionForm(forms.ModelForm):
	class Meta:
		model=Transaction
		fields='__all__'