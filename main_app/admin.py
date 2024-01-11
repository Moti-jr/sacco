from django.contrib import admin

from main_app.models import Customer

# Register your models here.
admin.site.site_header = 'piko sacco'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',  'email'
                    ]
    # the search functionality

    search_fields = ['first_name', 'id_number', 'phone_no']
    list_filter = ["first_name"]
    list_per_page = 50


admin.site.register(Customer, CustomerAdmin)