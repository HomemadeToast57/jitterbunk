from django.urls import path

from . import views

app_name = "bunk"

urlpatterns = [
    path("bunkfeed/", views.main_bunk_feed),
    path("<int:id>/bunkfeed/", views.personal_bunk_feed, name="personal_feed"),
    path("bunkfeed/submit_bunk", views.submit_bunk, name="submit_bunk"),
    path("users/", views.user_list, name="user_list"),
    path("create_user/", views.create_user, name="create_user")
]

