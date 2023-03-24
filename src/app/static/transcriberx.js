// Get the buttons
const getStartedButtons = document.querySelectorAll("button");

// Add a click event listener to each button
getStartedButtons.forEach(button => {
  button.addEventListener("click", () => {
    // Navigate to the /start page
    window.location.href = "/upload";
  });
});
