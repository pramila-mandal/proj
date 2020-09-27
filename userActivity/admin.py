from django.contrib import admin
from .models import User, Activity

class UserAdmin(admin.ModelAdmin): 
    pass

class ActivityAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
admin.site.register(Activity, ActivityAdmin)
