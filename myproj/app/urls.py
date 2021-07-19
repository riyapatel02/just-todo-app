from django.urls import path
from .import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('update-todo/',views.update_todo, name='update_todo'),
    path('delete-todo/<id>/',views.delete_todo, name='delete_todo'),
    path('login/',views.login,name='login'),
    path('signup/',views.register,name='signup')
]
