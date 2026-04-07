// Add to cart form functionality
document.querySelectorAll('form[action*="add_to_cart"]').forEach(form => {
    form.addEventListener('submit', function(e) {
        const quantity = this.querySelector('input[name="quantity"]');
        if (quantity && parseInt(quantity.value) < 1) {
            e.preventDefault();
            alert('Please enter a valid quantity');
        }
    });
});

// Confirm delete actions
document.querySelectorAll('form[action*="delete"]').forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!confirm('Are you sure?')) {
            e.preventDefault();
        }
    });
});

// Update cart quantity
document.querySelectorAll('input[name="quantity"]').forEach(input => {
    input.addEventListener('change', function() {
        if (parseInt(this.value) < 1) {
            this.value = 1;
        }
    });
});

// Tooltip initialization (Bootstrap)
document.addEventListener('DOMContentLoaded', function() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
});
