from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title','id','slug')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ('title','id')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name','subject')
  
admin.site.register(Comment)
  