from django.contrib import admin
from .models import Project, UploadProjectFiles, ReferenceLinks, CheckBoxes
# Register your models here.


admin.site.register(Project)
admin.site.register(UploadProjectFiles)
admin.site.register(CheckBoxes)
admin.site.register(ReferenceLinks)