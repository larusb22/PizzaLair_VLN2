

  const form = document.getElementById('order-form');
  const select = document.getElementById('order-select');


  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const selectedOption = select.value;
    const currentUrl = new URL(window.location.href);


    currentUrl.searchParams.set('order', selectedOption);

    window.location.href = currentUrl.toString();
  });