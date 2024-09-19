from django.contrib import admin
from .models import User, pet

#admin.site.register(User)
#admin.site.register(pet)

class UserAdmin(admin.ModelAdmin):
    ''' '''
    list_display = ('firstName', 'lastName', 'joined')

admin.site.register(User, UserAdmin)
