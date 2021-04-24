
// EXPLAIN THE PROCESS

// paste in home.html will allow to create the instance of the stripe otherwise the stripe instance we define will be undefined
{/* <script src="https://js.stripe.com/v3/"></script> */}




fetch("/config/") // here we are going to django endpoint or urls.py to fetch data and that data is the 
// the seesion_id and publickey return in json format in views.py


.then((result) => { return result.json(); }) // here we put the result in json 
.then((data) => {  // the data(session_id, and publickey ) will be present in data 
    console.log(data)

    
    const stripe = Stripe(data.publicKey); // here we create the instance or object of stripe 
    // we fetch thge class we the help of his link and here we only need publickey 


// here when the user click the button the event is click after clicking we define in function what is going to happen after click the button
document.querySelector("#submitBtn").addEventListener("click", () => {

    fetch("/create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
    console.log(data);

    return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
    console.log(res);
    });
});
});