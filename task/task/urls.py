from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import transaction_view,all_customer_transaction_average,customer_details,individual_customer_transactions,calculate_std,home
urlpatterns = [
    # Examples:
    # url(r'^$', 'task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'home/$',home),
    url(r'^transaction/$',transaction_view),
   # url(r'^all_transactions/$',all_customer_transaction),
    url(r'^average/$',all_customer_transaction_average),
    url(r'^customer_details/$',customer_details),
    url(r'^individual_customer/$',individual_customer_transactions),
    url(r'^st_dev/$',calculate_std),
]
