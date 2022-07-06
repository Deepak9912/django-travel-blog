function sendEmail(contactForm) {
    emailjs.send("service_jui1hv6", "Explorer", {
        "name": contactForm.name.value,
        "email": contactForm.email.value,
        "subject": contactForm.subject.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response) {
            document.getElementById('email_alert').innerHTML = `<h4">Thanks for your email!
            <br> We will contact you as soon as possible!</h4>`;
        },
        function(error) {
            document.getElementById('email_alert').innerHTML = `<h4">Sorry, something went wrong!
            <br> Try to send the email again.</h4>`;
        }
    );
    return false;  // To block from loading a new page
}