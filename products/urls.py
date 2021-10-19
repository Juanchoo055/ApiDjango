from django.urls import path

from products import views


urlpatterns = [
    path(
        route = "",
        view = views.productView.as_view()
    ),

    path(
        route = '<str:pk>/',
        view = views.productUpdate.as_view({'put':'update', 'delete':'destroy'})
    ),
    path(
        route = 'detail/<str:pk>/',
        view = views.productDetailView.as_view()
    ),
    path(
        route = 'export/',
        view = views.export.as_view()
    ),
        
        
]
