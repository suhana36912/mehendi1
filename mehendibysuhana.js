const menuToggle=document.getElementById('mobile-menu');
const navLinks=document.getElementById('nav-links');
menuToggle.addEventListener('click',()=>{
    navLinks.classList.toggle('active');
});
document.getElementById('booking-form').addEventListener('submit', function (e) {
    e.preventDefault(); // prevent default form submission

    const formData = {
        name: document.querySelector('input[placeholder="Enter your name"]').value,
        phone: document.querySelector('input[placeholder="Enter your number"]').value,
        email: document.querySelector('input[placeholder="Enter your email"]').value,
        address: document.querySelector('input[placeholder="Enter your address"]').value,
        booking_date: document.querySelector('input[type="date"]').value,
        client_count: document.querySelector('input[placeholder="Number of client"]').value
    };

    fetch('http://127.0.0.1:5000/submit-booking', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if (response.ok) {
            alert('Booking submitted successfully!');
            document.getElementById('booking-form').reset();
        } else {
            alert('Booking failed. Try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while submitting the booking.');
    });
});
