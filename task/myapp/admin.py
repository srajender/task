from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
	list_display=('customer','transaction_type','transaction_date','amount','balance')

	def balance(self, obj):
		return '%s'%(obj.customer.balance)
	balance.short_description = 'Balance'

admin.site.register(Transaction,TransactionAdmin)