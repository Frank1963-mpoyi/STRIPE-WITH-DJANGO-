

from django.urls import path
from .views_two import create_checkout_session

from .views import  (
   
   checkout, 
   SuccessView ,  
   CancelledView, 
   stripe_webhook,
   home_view,
   
   )  





urlpatterns = [
   
   path('', home_view, name="home_view"),
   path('checkout/', checkout, name="checkout"),
   path('success', SuccessView.as_view(), name="success"), 
   path('cancelled', CancelledView.as_view(), name="cancelled"), 
   path('stripe_webhookt/', stripe_webhook, name="stripe_webhook"),
   
   
   
   # here is for views_two.py
   
   path('create_checkout_session', create_checkout_session, name="create_checkout_session"),

]
