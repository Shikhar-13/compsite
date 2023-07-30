from django.contrib import admin

# Register your models here.
from compsite_pro.models import Topic , SubjectEntry,Notice


admin.site.register(Topic)
admin.site.register(SubjectEntry)
admin.site.register(Notice)