// Function to delay the appearance of the portfolio button
window.onload = setTimeout(
    function() {
    let button = document.getElementById('portfolio-btn')
        button.classList.remove('hide-element')
}, 900)
