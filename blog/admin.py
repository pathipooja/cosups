from django.contrib import admin
from blog.models import Post,Orders,EarnCredits
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','marketer','product_details',"available_in",'status']
    list_filter=('status','marketer','created','publish')
    search_fields=('title','product_details')
    # raw_id_fields=('marketer',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}
class OrderAdmin(admin.ModelAdmin):
    list_display=['dealername','productname','apartmentaddress','flataddress','orderstatus']
class EarnCreditsAdmin(admin.ModelAdmin):
    list_display=['title','completed','slug','author','body','publish','created','updated','status']
    list_filter=('completed','status','author','created','publish')
    search_fields=('title','body')
    date_hierarchy='publish'
    ordering=['status','-publish']
    prepopulated_fields={'slug':('title',)}
admin.site.register(EarnCredits,EarnCreditsAdmin)
admin.site.register(Orders,OrderAdmin)
admin.site.register(Post,PostAdmin)
