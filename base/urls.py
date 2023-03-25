from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name="homeUrl"),
    path('room/<str:pk>', v.room, name="roomUrl")
]
