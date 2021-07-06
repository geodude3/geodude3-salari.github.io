from . import views
from django.urls import path


app_name = "homepage"


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("todo", views.todo.todo1, name="todo"),
    path("account", views.account, name="account"),
    path("add", views.add, name="add"),
    path("delete", views.todo.delete, name="delete")
]