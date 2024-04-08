from django.contrib import admin
from .models import Region, Seed, Tractor, Worker, WorkType, Order,Fertiliser
# Register your models here.

admin.site.register(Region)
admin.site.register(Seed)
admin.site.register(Tractor)
admin.site.register(Worker)
admin.site.register(WorkType)
admin.site.register(Order)
admin.site.register(Fertiliser)


