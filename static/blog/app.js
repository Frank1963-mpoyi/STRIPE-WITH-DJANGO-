
// EXPLAIN THE PROCESS

// paste in home.html 
{/* <script src="https://js.stripe.com/v3/"></script> */}




fetch("/config/") // here we are going to django endpoint or urls.py to fetch data and that data is the 
// the seesion_id and publickey return in json format in views.py


.then((result) => { return result.json(); }) // here we put the result in json 
.then((data) => {  // the data present 
    console.log(data)

    
    const stripe = Stripe(data.publicKey);


document.querySelector("#submitBtn").addEv