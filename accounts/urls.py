from django.urls import path
from .import views
from .views import LoginPageView

app_name = 'pages'
urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
]