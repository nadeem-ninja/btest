from django.contrib import admin

# Register your models here.
from activity.models import Profile, ActivityPeriod

admin.site.register(Profile)
admin.site.register(ActivityPeriod)
