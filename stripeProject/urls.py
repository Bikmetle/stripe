from django.contrib import admin
from django.urls import path
from stripeApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:pk>', views.LandingPage),
    path('buy/<int:pk>', views.CreateCheckoutSession, name='buy'),
    path('success/', views.Success),
    path('canceled/', views.Canceled),
]
