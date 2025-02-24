document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("feedbackForm").addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent form from submitting traditionally

      // Get form values
      const name = document.getElementById("name").value;

      // ✅ Show success message
      document.getElementById("responseMessage").innerText = `Thank you for your feedback, ${name}!`;

      // ✅ Clear the form
      document.getElementById("feedbackForm").reset();
  });
});
