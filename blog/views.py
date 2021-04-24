from django.shortcuts import render
from django.conf import settings 
from django.http.response import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from django.views.generic.base import TemplateView
from django.urls import reverse
import stripe



stripe.api_key = settings.STRIPE_SECRET_KEY 


def home_view(request):
    template_name = 'blog/home.html'
    context = {}
    return render(request, template_name, context)




# point to ajax and create session when user click the buy button different with other mether which 
#create many session in stripe webapp
@csrf_exempt
def checkout(request):
    
    session = stripe.checkout.Session.create(
                
                payment_method_types=['card'],
                
                line_items=[
                    {
                        'price' : 'price_1I8IrPH5FGERXivQ3VMAS9No',  
                        'quantity': 1 
                        
                    }
                ],
                mode='payment',
                success_url= request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri(reverse('cancelled')),
            )
    
    return JsonResponse(
        {
        'session_id' : session.id,
        'publicKey': settings.STRIPE_PUBLISHABLE_KEY  
    }
    )




class SuccessView(TemplateView):
    template_name = 'blog/success.html'



class CancelledView(TemplateView):
    template_name = 'blog/cancelled.html'
   
   
   
    
@csrf_exempt    
def stripe_webhook(request):
    
    # You can find your endpoint 's secret in your webhook settings
    endpoint_secret ='whsec_...'
    
    payload = request
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        event = stripe.webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    #Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        
    return HttpResponse(status=200)

# command to run webhook in the cli
# stripe listen --forward-to localhost:4242/webhook   

#we must specify the endpoint at the end when it finish to run it will give you webhook secret
#stripe listen --forward-to localhost:8000/stripe_webhookt/ 