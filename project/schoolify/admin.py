from django.contrib import admin

# Register your models here.
from .models import  school,  classroom, student


##### Register your models here #####
admin.site.register(school)
admin.site.register(classroom)
admin.site.register(student)