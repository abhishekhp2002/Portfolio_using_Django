from django.urls import path
from .import views
'''from ..portfolio.urls import urlpatterns'''
'''path('contact/',views.contact),
    path('', views.index, name='index')'''
urlpatterns=[
    
    path('', views.IndexView.as_view(), name='index')
]