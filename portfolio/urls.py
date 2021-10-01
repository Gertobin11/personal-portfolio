from . import views
from django.urls import path


urlpatterns = [
    path('', views.portfolio_page, name='portfolio_page')
]
