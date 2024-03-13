from django.contrib import admin
from . models import FundiUser, Topic, Session, Activity

# Register your models here.

admin.site.register(FundiUser)
admin.site.register(Topic)
admin.site.register(Session)
admin.site.register(Activity)

