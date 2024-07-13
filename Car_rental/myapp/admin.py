from django.contrib import admin
from myapp.models import Contact

# Register your models here.
admin.site.site_header = "Trator | Admin"
admin.site.register(Contact)

