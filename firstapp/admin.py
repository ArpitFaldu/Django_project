from django.contrib import admin
from .models import Device,Review,Wishlist,Mobile,Laptop,Company,CompanyInfo
# Register your models here.
# admin.site.register(User)
admin.site.register(Device)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Mobile)
admin.site.register(Laptop)
admin.site.register(Company)
admin.site.register(CompanyInfo)