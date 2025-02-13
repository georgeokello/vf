from django.urls import path
# from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    # topic endpoints
    path('', views.viewTopic),
    path('addTopic/', views.addTopic),
    path('viewSecTopics/', views.viewSecTopics),
    path('viewPriTopics/', views.viewPriTopics),
    path('getTopic/<int:id>', views.getTopic),
    path('updateTopic/<int:id>', views.updateTopic),
    path('deleteTopic/<int:id>', views.deleteTopic),
    # session endpoints
    path('addSession/', views.addSession),
    path('getSession/<int:id>', views.getSession),
    path('viewSessions/<int:pk>', views.viewSessions),
    path('updateSession/<int:id>', views.updateSession),
    path('deleteSession/<int:id>', views.deleteSession),
    # activity endpoints
    path('addActivity/', views.addActivity),
    path('viewActivities/<int:pk>', views.viewActivities),
    path('getActivity/<int:id>', views.getActivity),
    path('updateActivity/<int:id>', views.updateActivity),
    path('deleteActivity/<int:id>', views.deleteActivity),
    # text activity endpoints
    # path('addTextActivity/', views.addTextActivity),
    # path('viewTextActivities/<int:pk>', views.viewTextActivities),
    
    # # video activity endpoints
    # path('addVideoActivity/', views.addVideoActivity),
    # path('viewVideoActivity/<int:pk>', views.viewVideoActivities),
    path('deleteVideoActivity/<int:pk>', views.deleteVideoActivity),
    path('updateVideoActivity/<int:pk>', views.updateVideoActivity),

    # path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    # upload activity details
    path('uploadActivity/', views.upload_activity, name="upload_activity"),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    # user 
    path('getProfile/', views.getProfile, name='UserProfile'),


    # feedback endpoints
    path('addFeedback', views.addFeedback, name='addFeedback'),
    path('viewFeedback', views.viewFeedback, name='viewFeedback'),

    # teachers 
    path('addTeacher/', views.add_teacher, name="addTeacher"),
    path('viewTeachers/', views.view_teachers, name="viewTeachers"),
    path('updateTeacher/<int:id>', views.update_teacher, name="updateTeacher"),
    path('deleteTeacher/<int:id>', views.delete_teacher, name="deleteTeacher"),

    # DEAR day
    # theme
    path('viewTheme/', views.viewTheme),
    path('addTheme/', views.addTheme),
    path('getTheme/<int:id>', views.getTheme),
    path('updateTheme/<int:id>', views.updateTheme),
    path('deleteTheme/<int:id>', views.deleteTheme),

    # sub theme
    path('addSubTheme/', views.addSubTheme),
    path('getSubTheme/<int:id>', views.getSubTheme),
    path('viewSubTheme/<int:pk>', views.viewSubTheme),
    path('updateSubTheme/<int:id>', views.updateSubTheme),
    path('deleteSubTheme/<int:id>', views.deleteSubTheme),

    # chapters
    path('addChapter/', views.addChapter),
    path('viewChapters/<int:pk>', views.viewChapters),
    path('getChapter/<int:id>', views.getChapter),
    path('updateChapter/<int:id>', views.updateChapter),
    path('deleteCapter/<int:id>', views.deleteChapter),
]
