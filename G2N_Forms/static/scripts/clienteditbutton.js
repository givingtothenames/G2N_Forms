// Get all the view buttons
const viewButtons = document.querySelectorAll('.btn-view');

// Loop through each button and add a click event listener
viewButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        // Get the clicked row and its id
        const row = event.target.closest('tr');
        const rowId = row.dataset.rowId;

        // Get the value of the first column
        const value = row.querySelector('td[data-value]').dataset.value;

        // Construct the URL of the new page
        const url = `/view-data?id=${rowId}&value=${value}`;

        // Redirect to the new page
        window.location.href = url;
    });
});
