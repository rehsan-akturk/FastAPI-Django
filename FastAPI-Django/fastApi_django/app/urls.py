from django.urls import path
from . import views
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',  views.Driverall.as_view(), name="driver_get_all"),
    path('driver_driver/<str:startDate>/<str:endDate>/<str:minScore>/<str:maxScore>',  views.Drivers.as_view(),  name="driver"), ###parameters link
    
    path('button',  views.Button.as_view(), name="button")


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)