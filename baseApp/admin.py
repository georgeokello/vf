from django.contrib import admin
from . models import FundiUser, Topic, Session, Activity,  Feedback, Teachers
from . models import Theme, Sub_Theme, Chapters

# Register your models here.

admin.site.register(FundiUser)
admin.site.register(Topic)
admin.site.register(Session)
admin.site.register(Activity)
admin.site.register(Teachers)
admin.site.register(Feedback)
admin.site.register(Theme)
admin.site.register(Sub_Theme)
admin.site.register(Chapters)


