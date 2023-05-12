document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('mysearch');
  const products = document.querySelectorAll('.well-product');
  const clearFilterButton = document.querySelector('.clear-filter');

  searchInput.addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();
    filterProducts(searchValue);
  });

  clearFilterButton.addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = 'http://127.0.0.1:8000/menu';
  });

  function filterProducts(searchValue) {
    products.forEach(function(product) {
      const productName = product.querySelector('h4').getAttribute('data-search').toLowerCase();
      const isMatched = productName.includes(searchValue);

      if (isMatched) {
        product.style.display = 'flex';
      } else {
        product.style.display = 'none';
      }
    });
  }

});

