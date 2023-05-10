document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('mysearch');
  const products = document.querySelectorAll('.well-product');
  const filterButtons = document.querySelectorAll('.filters a');
  const clearFilterButton = document.querySelector('.clear-filter');
  let selectedFilter = 'all'; // Track the currently selected filter

  searchInput.addEventListener('input', function() {
    const searchValue = this.value.toLowerCase();

    products.forEach(function(product) {
      const productName = product.querySelector('h4').getAttribute('data-search').toLowerCase();
      if (productName.includes(searchValue)) {
        product.style.display = 'flex';
      } else {
        product.style.display = 'none';
      }
    });
  });

  filterButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      const filterValue = this.innerText.toLowerCase();

      // Update the selected filter
      selectedFilter = filterValue;

      // Apply the filter based on the updated selection
      products.forEach(function(product) {
        const productFilter = product.getAttribute('data-filter');
        if (selectedFilter === 'all' || productFilter === selectedFilter) {
          product.style.display = 'flex';
        } else {
          product.style.display = 'none';
        }
      });

      // Update the active state of the filter buttons
      filterButtons.forEach(function(btn) {
        if (btn.innerText.toLowerCase() === selectedFilter) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });
    });
  });

  // Clear All Filters
  clearFilterButton.addEventListener('click', function() {
    // Reset the selected filter
    selectedFilter = 'all';

    // Reset the active state of the filter buttons
    filterButtons.forEach(function(btn) {
      btn.classList.remove('active');
    });

    // Show all products
    products.forEach(function(product) {
      product.style.display = 'flex';
    });
  });
});
