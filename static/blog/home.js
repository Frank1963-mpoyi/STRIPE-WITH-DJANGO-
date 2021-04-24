

const submitBtn = document.querySelector('#submitBtn') // grab the buuton for event handler

submitBtn.addEventListener('click', event=> { 

    // new for ajax call 
    fetch('/checkout/') // after user click the buuton this fetch('/checkout/') is to fetch public key from this endpoint or url checkout in django urls.py

    .then((result) => {return result.json() }) //the data will be tranform in json format
    .then((data) => {// data available which is : session id and public key
    

        var stripe = Stripe(data.publicKey)  // use the the public key to create a new instance of the  stripe  // public key variable from views.py 
        
        
        //Redirect to the checkout page for the user to finish their purchase
        stripe.redirectToCheckout({

        sessionId : data.session_id // session id from our context in views.py 

        }).then(function(result){

        });

        })

    })