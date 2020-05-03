const track = document.querySelector('.carouselTrack');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.carouselButtonRight');
const prevButton = document.querySelector('.carouselButtonLeft');
const dotNav = document.querySelector('.carouselNav');
const dots = Array.from(dotNav.children);
const finButton = document.querySelector('.finishButton');

const slideWidth = slides[0].getBoundingClientRect().width;


const setSlidePosition = (slide, index) => {
  slide.style.left = slideWidth * index + 'px'; 
}

slides.forEach(setSlidePosition);

const moveToSlide = (track, currentSlide, targetSlide) => {

  track.style.transform = 'translateX(-' + targetSlide.style.left + ')';
  currentSlide.classList.remove('currentSlide');
  targetSlide.classList.add('currentSlide');
}

const updateDots = (currentDot, targetDot) => {
  currentDot.classList.remove('currentSlide');
  targetDot.classList.add('currentSlide');
}

const arrowDisplay = (slides, prevButton, nextButton, targetIndex) => {
  if (targetIndex === 0) {
    prevButton.classList.add('isHidden');
    nextButton.classList.remove('isHidden');
  } else if (targetIndex === slides.length - 1) {
    prevButton.classList.remove('isHidden');
    nextButton.classList.add('isHidden');
  } else {
    prevButton.classList.remove('isHidden');
    nextButton.classList.remove('isHidden');
  }
}

/// move left
prevButton.addEventListener('click', e=>{
  const currentSlide = track.querySelector('.currentSlide');
  const prevSlide = currentSlide.previousElementSibling;
  const currentDot = dotNav.querySelector('.currentSlide');
  const prevDot = currentDot.previousElementSibling;
  const prevIndex = slides.findIndex(slide => slide === prevSlide);

  moveToSlide(track, currentSlide, prevSlide);
  updateDots(currentDot, prevDot);
  arrowDisplay(slides, prevButton, nextButton, prevIndex);
});


/// move right
nextButton.addEventListener('click', e => {
  const currentSlide = track.querySelector('.currentSlide');
  const nextSlide = currentSlide.nextElementSibling;
  const currentDot = dotNav.querySelector('.currentSlide');
  const nextDot = currentDot.nextElementSibling;
  const nextIndex = slides.findIndex(slide => slide === nextSlide);
  
  moveToSlide(track, currentSlide, nextSlide);
  updateDots(currentDot, nextDot);
  arrowDisplay(slides, prevButton, nextButton, nextIndex);



});

///click dot indicator, to slide
dotNav.addEventListener('click', e => {
  const targetDot = e.target.closest('button');

  if (!targetDot) return;

  const currentSlide = track.querySelector('.currentSlide');
  const currentDot = dotNav.querySelector('.currentSlide');
  const targetIndex = dots.findIndex(dot => dot === targetDot);
  const targetSlide = slides[targetIndex];

  moveToSlide(track, currentSlide, targetSlide);
  updateDots(currentDot, targetDot);

  arrowDisplay(slides, prevButton, nextButton, targetIndex);
})

function getInputValues(){
    $("#formSheet").hide();
  $("#results").show();
  document.getElementById("sUsername").innerHTML = document.getElementById('username').value;
  document.getElementById("sPassword").innerHTML = document.getElementById('password').value;
  document.getElementById("sFname").innerHTML = document.getElementById('fname').value;
  document.getElementById("sMname").innerHTML = document.getElementById('mname').value;
  document.getElementById("sLname").innerHTML = document.getElementById('lname').value;
  document.getElementById("sGender").innerHTML = document.getElementById('gender').value;
  document.getElementById("sAddress").innerHTML = document.getElementById('address').value;
  document.getElementById("sCity").innerHTML = document.getElementById('city').value;
  document.getElementById("sState").innerHTML = document.getElementById('state').value;
  document.getElementById("sZipCode").innerHTML = document.getElementById('zipcode').value;
  document.getElementById("sEmail").innerHTML = document.getElementById('email').value;
  document.getElementById("sPhoneNumber").innerHTML = document.getElementById('phone').value;
  document.getElementById("sCountry").innerHTML = document.getElementById('country').value;
  document.getElementById("sDOB").innerHTML = document.getElementById('dob').value;
  document.getElementById("sOrg").innerHTML = document.getElementById('org').value;

}
///form
