from django.urls import path, include
from records import views

app_name = 'records'

crud_url_patterns = [
    path('add/', views.AddRecord.as_view(), name='add'),
    path('update/<int:pk>/', views.UpdateRecord.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteRecord.as_view(), name='delete'),
]

urlpatterns = [
    path('chart/data/', views.ChartView.as_view(), name='chart-data'),
    path('', views.ListRecords.as_view(), name='list'),
    path('', include(crud_url_patterns)),
]
