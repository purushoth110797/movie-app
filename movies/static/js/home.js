// Access all rating texts
let ratingTexts = document.querySelectorAll('.rating-text');

ratingTexts.forEach(function(textElement) {
    let rating = parseFloat(textElement.innerText).toFixed(1);

    // color ranges for the rating
    const colorRange = [
        {min:1, max:2.9, color: "#FF0000"},
        {min:2.9, max:5.9, color: "#FFA500"},
        {min:5.9, max:7.9, color: "#FFFF00"},
        {min:7.9, max:10, color: "#008000"},
    ]
    // calling the function and getting the color based on the rating
    const color = getColorForRating(rating, colorRange);

    // Calculate the dash array length based on the rating
    const dashArray = (rating / 10) * (2 * Math.PI * 45);

    // Calculate the gap length
    const gapArray = 2 * Math.PI * 45 - dashArray;

    // Update the stroke dash array and text content
    textElement.parentNode.querySelector('.progress-circle').style.strokeDasharray = `${dashArray} ${gapArray}`;
    textElement.textContent = `${rating}`;
    textElement.parentNode.querySelector('.progress-circle').style.stroke = color;
});

// Function to find color based on rating
function getColorForRating(rating, colorRanges) {
    for (let i = 0; i < colorRanges.length; i++) {
        if (rating >= colorRanges[i].min && rating <= colorRanges[i].max) {
            return colorRanges[i].color;
        }
    }
    // Default color if rating doesn't fall into any range
    return '#f4decb';
}

// Get the button
var mybutton = document.getElementById("moveToTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

