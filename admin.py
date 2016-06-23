from django.contrib import admin
from .models import *
# Register your models here.
class AdminItem(admin.ModelAdmin):
	list_display=['author','description','amount','expense_group']
	list_filter=('author','expense_group__name',)
class AdminBatch(admin.ModelAdmin):
	list_display=['name','members_included']
	def members_included(self,obj):
		return ', '.join([m.username for m in obj.members.all()])
admin.site.register(Item,AdminItem)
admin.site.register(Batch,AdminBatch)
