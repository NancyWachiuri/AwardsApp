from django.urls import path
from .import views

urlpatterns = [
    path('',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('home/',views.home, name="home"),

    path('project_details/<int:id>/', views.detail, name="project_details"),
    path('add_project/',views.add_project , name="add_project"),
    path('search_results/',views.search_results, name='search_results'),

    path('editreview/<int:id>/',views.edit_review, name="edit_review"),
    path('deletereview/<int:id>/',views.delete_review, name="delete_review")
]
