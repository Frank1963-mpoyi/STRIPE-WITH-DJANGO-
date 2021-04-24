from django.shortcuts import render
from django.conf import settings 
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from django.views.generic.base import TemplateView
from django.urls import reverse
import stripe






@csrf_exempt
def create_checkout_session(request):
    
    template_name = 'blog/home.html'
    stripe.api_key = settings.STRIPE_SECRET_KEY # here we assign our secret key to direct stripe to our account 
    
    session = stripe.checkout.Session.create(
                
                payment_method_types=['card'],
                
                line_items=[
                    {
                        'price' : 'price_1I8IrPH5FGERXivQ3VMAS9No', # this Key I got from stripe price account 
                        'quantity': 1 # quantity of the product
                        
                    }
                ],
                mode='payment',
                success_url= request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('cancelled')),
            )
    
    context = {
        'session_id' : session.id,# name session refer to session up 
        'publicKey': settings.STRIPE_PUBLISHABLE_KEY # stripe public key from settings.py 
    }
    return render(request, template_name, context)
    
    
    
    



# stripe.api_key = settings.STRIPE_SECRET_KEY # this is your own private key for stripe not to give money to someone else
# # in parent module api_key = None here we assign to his value in settings.py



# class HomePageViewS(TemplateView):
#     template_name = 'blog/home_two.html'

#     def get_context_data(self, **kwargs): # new
#         # the first is for the parent class
#         context = super().get_context_data(**kwargs)
        
#         # the second is for child class
#         context['key'] = settings.STRIPE_PUBLISHABLE_KEY
#         return context
    
