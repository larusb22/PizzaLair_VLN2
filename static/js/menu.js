document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('mysearch');
  const products = document.querySelectorAll('.well-product');
  const filterButtons = document.querySelectorAll('.filter-btn');
  const clearFilterButton = document.querySelector('.clear-filter');
  let selectedFilter = 'all';

  searchInput.addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();
    filterProducts(searchValue, selectedFilter);
  });

  filterButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
      event.preventDefault();
      const filterValue = this.getAttribute('data-filter');
      selectedFilter = filterValue;
      filterProducts(searchInput.value.toLowerCase(), selectedFilter);
    });
  });

  clearFilterButton.addEventListener('click', function() {
    selectedFilter = 'all';
    searchInput.value = '';
    filterProducts('', selectedFilter);
  });

  function filterProducts(searchValue, filterValue) {
    products.forEach(function(product) {
      const productName = product.querySelector('h4').getAttribute('data-search').toLowerCase();
      const productFilter = product.getAttribute('data-filter');

      const isMatched = productName.includes(searchValue);
      const isFiltered = filterValue === 'all' || productFilter === filterValue;

      if (isMatched && isFiltered) {
        product.style.display = 'flex';
      } else {
        product.style.display = 'none';
      }
    });
  }
});