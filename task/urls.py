from django.urls import path
from . import views
urlpatterns=[
    path('users/',views.showUserList, name='ShowUserList'),
    path('user-detail/<int:pk>/',views.UserDetails, name='User-Details'),
    path('create-list/',views.CreateUserList, name='Create-User-List'),
    path('update-list/<int:pk>', views.UpdateList, name='Update-list'),
    path('delete-user/<int:pk>', views.deleteUser , name='DeleteUser'),
]