const searchInput = document.querySelector("[data-search]");

searchInput.addEventListener("input", function (e) {
    const value = e.target.value;
    console.log(value);
});