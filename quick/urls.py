
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #Clients Urls
    path("clients/", include(('clientAdmin.urls', 'clientAdmin'),namespace='clients')), 


    # #Products urls
    # path("products/", include(('products.urls', 'products'),namespace='products')), 

]   


