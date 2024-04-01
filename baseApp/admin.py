from django.contrib import admin
from . models import FundiUser, Topic, Session, Activity, TextActivity, VideoActivity

# Register your models here.

admin.site.register(FundiUser)
admin.site.register(Topic)
admin.site.register(Session)
admin.site.register(Activity)
admin.site.register(TextActivity)
admin.site.register(VideoActivity)

