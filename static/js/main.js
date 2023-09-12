// activation aos
AOS.init();

// Start Landing
//Use Sblide
document.addEventListener("DOMContentLoaded", function () {
    var splideOne = new Splide("#landing-slide", {
        type: "loop",
        autoplay: true,
        interval: 3000,
    });

    splideOne.mount();
});
//End Landing

// Start reservation
//Click Input Date
let iconInpDate = document.querySelector(".reservation form .icon-date"),
    inpDate = document.querySelector(".reservation form #date");

inpDate.addEventListener("focus", () => {
    inpDate.setAttribute("type", "date");
    iconInpDate.style.display = "none";
});

inpDate.addEventListener("blur", () => {
    inpDate.setAttribute("type", "text");
    iconInpDate.style.display = "block";
});
// End reservation
