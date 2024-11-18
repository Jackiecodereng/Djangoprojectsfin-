from django.contrib import admin

from sacco.models import Customer, Deposit

# Register your models here.


admin.site.site_header = ' Umoja Sacco Administration'# changes the title
admin.site.site_title = '  Sacco Admin'

# helps customize the page of customers

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','gender','dob']
    search_fields = ['first_name','last_name','email']
    list_filter = ['gender']
    list_per_page = 25

class DepositAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at', 'status', 'amount']
    search_fields = ['customer', 'status', 'amount']
    list_per_page = 25
    list_filter = ['status']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit , DepositAdmin)









#customize the head

# this file deals with login page and permissions.
#python manage.py --help
#python manage.py createsuperuser
# to clear termina click cls
#admin@gmail.com
#e:admin@gmail.com
#pass:123456
#y
#Id37290376!