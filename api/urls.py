from django.urls import path

from . import views

urlpatterns = [
    path('apis/', views.api ),
    path('apis/<int:pk>', views.api ),
]