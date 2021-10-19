from django.urls import path
from clientAdmin import views


urlpatterns = [
    path(
        route = "",
        view = views.clientView.as_view(),
        name="clientslist"
    ),

    path(
        route = '<int:id>/',
        view = views.clientDetailView.as_view(),
        name="clientDetail"
    ),

    path(
        route = 'add/',
        view = views.clientView.as_view(),
        name="clientAdd"
    ),

    path(
        route = 'update/<int:id>/',
        view = views.clientView.as_view(),
        name="clientUpdate"
    ),

    path(
        route = 'delete/<int:id>/',
        view = views.clientView.as_view(),
        name="clientDelete"
    )

    
    
]
