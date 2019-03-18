from django.contrib import admin
from .views import Author
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','photo',)