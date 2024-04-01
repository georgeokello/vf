from django.urls import path
# from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    # topic
    path('', views.viewTopic),
    path('addTopic/', views.addTopic),
    path('getTopic/<int:id>', views.getTopic),
    path('updateTopic/<int:id>', views.updateTopic),
    path('deleteTopic/<int:id>', views.deleteTopic),
    # session
    # path('', views.viewTools),
    path('addSession/', views.addSession),
    path('getSession/<int:pk>', views.getSession),
    path('updateSession/<int:id>', views.updateSession),
    path('deleteSession/<int:id>', views.deleteSession),
    # activity
    # path('', views.viewTools),
    path('addActivity/', views.addActivity),
    path('getActivity/<int:id>', views.getActivity),
    path('updateActivity/<int:id>', views.updateActivity),
    path('deleteActivity/<int:id>', views.deleteActivity),

    # path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
