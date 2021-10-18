from django.urls import path
from clientAdmin import views


urlpatterns = [
    path(
        route = "",
        view = views.clientView.as_view(),
        name="clientlist"
    ),

    path(
        route = '<int:pk>/',
        view = views.clientDetailView.as_view(),
        name="clientDetail"
    )

    
    
]
