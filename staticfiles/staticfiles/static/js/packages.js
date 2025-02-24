document.querySelectorAll('.toggle-btn').forEach(button => {
    button.addEventListener('click', function() {
        this.nextElementSibling.classList.toggle('show');
    });
});


// FOR MADATORY FIELDS FOR DATES AND PACKAGES

document.getElementById("bookingForm").addEventListener("submit", function(event) {
    let selectedDate = document.getElementById("date").value;
    let selectedPeople = document.getElementById("people").value;

    if (selectedDate === "" || selectedPeople === "") {
        alert("Please select both a date and a number of people before confirming booking.");
        event.preventDefault(); // Prevent form submission if validation fails
    }
});

// Open the modal when clicking "Book Now"
document.getElementById("openFormBtn").addEventListener("click", function() {
    document.getElementById("popupForm").style.display = "flex";
});

// Close the modal when clicking "X"
document.getElementById("closeForm").addEventListener("click", function() {
    document.getElementById("popupForm").style.display = "none";
});

// Close modal when clicking outside
window.onclick = function(event) {
    if (event.target === document.getElementById("popupForm")) {
        document.getElementById("popupForm").style.display = "none";
    }
};

// Show number of people input when a package is selected
document.getElementById("package").addEventListener("change", function() {
    let peopleInput = document.getElementById("peopleInput");
    if (this.value !== "") {
        peopleInput.classList.remove("hidden");
    } else {
        peopleInput.classList.add("hidden");
    }
});




const carousel = document.getElementById('video-carousel');
const slides = document.querySelectorAll('.carousel-slide');
const prevBtn = document.getElementById('prev-button');
const nextBtn = document.getElementById('next-button');

let index = 0;
const totalSlides = slides.length;

// Move to the next slide
function nextSlide() {
    index = (index + 1) % totalSlides;
    updateCarousel();
}

// Move to the previous slide
function prevSlide() {
    index = (index - 1 + totalSlides) % totalSlides;
    updateCarousel();
}

// Update carousel position
function updateCarousel() {
    carousel.style.transform = `translateX(-${index * 100}%)`;
}

// Auto-slide every 5 seconds
setInterval(nextSlide, 5000);

// Event Listeners for Buttons
nextBtn.addEventListener('click', nextSlide);
prevBtn.addEventListener('click', prevSlide);
