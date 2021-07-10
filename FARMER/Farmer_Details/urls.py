from django.urls import path
from . import views

urlpatterns = [
    path('', views.farmer_details, name='farmer_details'),
    path('dist/', views.district, name='dist'),
    path('taluka/', views.taluka, name='taluka'),
    path('frm_cnt/', views.frm_cnt, name='frm_cnt'),
    path('report/', views.report, name='report'),
]