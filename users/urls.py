from django.urls import path

from users import views

urlpatterns = [

    path(
        route = "",
        view = views.loginView.as_view(),
        name="loginView"
    ),
    path(
        route = "register",
        view = views.registerView.as_view(),
        name="registerView"
    ),
    path(
        route = "user",
        view = views.UserView.as_view(),
        name="usersView"
    )
]