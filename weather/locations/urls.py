from django.urls import path, include
from . import views

app_name = 'locations'

crud_url_patterns = [
    path('add/', views.AddLocation.as_view(), name='add'),
    path('update/<int:pk>/', views.UpdateLocation.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteLocation.as_view(), name='delete'),
]

urlpatterns = [
    path('', views.ListLocations.as_view(), name='list'),
    path('', include(crud_url_patterns)),
]
