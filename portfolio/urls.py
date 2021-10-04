from . import views
from django.urls import path


urlpatterns = [
    path('', views.portfolio_page, name='portfolio_page'),
    path('<int:pk>/', views.portfolio_details,
         name='portfolio_details')
]
