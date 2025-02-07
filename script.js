// Your JavaScript code goes here
console.log("Hello from script.js!");

// Example: Add an event listener
const allLinks = document.querySelectorAll('a');
allLinks.forEach(link => {
    link.addEventListener('click', function(event) {
        console.log('Link clicked:', event.target.href);
        // Add more logic as needed
    });
});