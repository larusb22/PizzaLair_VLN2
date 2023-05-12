

  const form = document.getElementById('order-form');
  const select = document.getElementById('order-select');

  // Listen for form submission
  form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent default form submission
    const selectedOption = select.value;
    const currentUrl = new URL(window.location.href);

    // Set the 'order' query parameter to the selected option
    currentUrl.searchParams.set('order', selectedOption);

    // Redirect to the updated URL with the selected ordering
    window.location.href = currentUrl.toString();
  });