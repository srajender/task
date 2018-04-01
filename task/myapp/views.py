from django.shortcuts import render
from django.http import Http404
from myapp.forms import CustomerForm
from . models import Customer,Transaction,TransactionForm
import numpy as np
# Create your views here.
def home(request):
	return render(request,'home_page.html')
def transaction_view(request):
	t=TransactionForm(request.POST)
	context={
	'form':t
	}
	if request.method=='POST':
		if t.is_valid():
			q=t.cleaned_data
			amount=q['amount']
			acnumber=q['customer']
			type	=q['transaction_type']
			obj=Customer.objects.get(account_number=acnumber)
			t=Transaction(transaction_type=type,amount=amount,customer=obj)
			t.save()
			if type=='C':
				obj.balance=obj.balance+amount
				obj.save()
			else:
				if obj.balance>amount:
					obj.balance=obj.balance-amount
					obj.save()
				else:
					raise Exception("Your balance is low")
	return render(request,'transaction.html',context)

def all_customer_transaction_average(request):
	obj=Transaction.manager.average_of_all()
	context={
	'form':int(obj['amount__avg'])
	}
	return render(request,'average.html',context)

def customer_details(request):
	cust=CustomerForm(request.POST)
	context={
	'form':cust
	}
	if request.method=='POST':
		if cust.is_valid():
			c=cust.cleaned_data
			accnum=c['account_number']
			try:
				obj=Customer.objects.get(account_number=accnum)
			except Customer.DoesNotExist:
				raise Http404("Customer account number is invalid")
		return 	render(request,'cust1.html',{'form':obj})
	return render(request,'cust.html',context)


def individual_customer_transactions(request):
	cust=CustomerForm(request.POST)
	context={
	'form':cust
	}
	if request.method=='POST':
		if cust.is_valid():
			c=cust.cleaned_data
			accnum=c['account_number']
			try:
				obj=Transaction.manager.all().filter(customer__account_number=accnum)
				l=list()
				l1=list()
				for a in obj:
					l.append(a.amount)
				x=np.array(l)
				std = int(x.std())
				for b in obj:
					if std<=b.amount:
						l1.append(b.amount)
				cont={
					'form':obj,
					'list':l1,
					'std_dev':std
					}
			except Customer.DoesNotExist:
				raise Http404("Customer account number is invalid")
		return 	render(request,'standard_deviation.html',cont)
	return render(request,'cust.html',context)

def calculate_std(request):
	obj=Transaction.manager.all()
	l=list()
	l1=list()
	for a in obj:
		l.append(a.amount)
	x=np.array(l)
	std = int(x.std())
	for b in obj:
		if std<=b.amount:
			l1.append(b.amount)
	context={
	'form':obj,
	'list':l1,
	'std_dev':std
	}
	return render(request,'standard_deviation.html',context)