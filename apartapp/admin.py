from django.contrib import admin
from apartapp.models import MarketerDetail

# Register your models here.
class MarketerDetailAdmin(admin.ModelAdmin):
    list_display=['username','credits']
admin.site.register(MarketerDetail,MarketerDetailAdmin)
