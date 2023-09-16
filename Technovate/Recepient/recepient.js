const ageInput = document.getElementById('age');
const livingStatusRadio = document.querySelector('input[value="Living"]');
const deceasedStatusRadio = document.querySelector('input[value="Deceased"]');
const organInputDiv = document.getElementById('organ-input');
const organInput = document.getElementById('organ');

// Add event listener for age input
ageInput.addEventListener('change', () => {
    const currentDate = new Date();
    const selectedDate = new Date(ageInput.value);
    const age = currentDate.getFullYear() - selectedDate.getFullYear();

    if (age < 18) {
        alert('You must be at least 18 years old to donate.');
        ageInput.value = ''; // Clear the age input
    }
    // else if(age >= 60){
    //     alert("You must be below 60 years to donate")
    // }
});

 // Function to update the output based on the selected options
 document.addEventListener('DOMContentLoaded', function() {
    const livingStatusRadios = document.querySelectorAll('input[name="living-status"]');
    const showDecasedElements = document.querySelector('.show-decased');
    const showLivingElements = document.querySelector('.show-living');

    // Function to update the displayed organ options based on the selected status
    function updateOrganOptions() {
        const selectedStatus = document.querySelector('input[name="living-status"]:checked');

        if (selectedStatus && selectedStatus.value === 'Living') {
            showDecasedElements.style.display = 'none';
            showLivingElements.style.display = 'block';
        } else if(selectedStatus && selectedStatus.value === 'Deceased') {
            showDecasedElements.style.display = 'block';
            showLivingElements.style.display = 'none';
        }else {
            showDecasedElements.style.display = 'none';
            showLivingElements.style.display = 'none';
        }
    }

    // Add event listener to the living status radios
    livingStatusRadios.forEach(radio => {
        radio.addEventListener('change', updateOrganOptions);
    });

    // Initialize the organ options based on the initial status
    updateOrganOptions();
});



function previewImage() {
const imageInput = document.getElementById('image');
const imagePreview = document.getElementById('image-preview');
const preview = document.getElementById('preview');
const removeButton = document.getElementById('remove-button');

if (imageInput.files && imageInput.files[0]) {
    const reader = new FileReader();

    reader.onload = function(e) {
        preview.src = e.target.result;
        imagePreview.style.display = 'block'; // Show the image preview container
        removeButton.style.display = 'block'; // Show the "Remove" button
    };

    reader.readAsDataURL(imageInput.files[0]);
}
}

function removeImage() {
const imageInput = document.getElementById('image');
const imagePreview = document.getElementById('image-preview');
const preview = document.getElementById('preview');
const removeButton = document.getElementById('remove-button');

imageInput.value = ''; // Clear the file input
preview.src = ''; // Clear the image preview
imagePreview.style.display = 'none'; // Hide the image preview container
removeButton.style.display = 'none'; // Hide the "Remove" button
}


const passwordField = document.getElementById('password');
const confirmPasswordField = document.getElementById('confirm-password');
const validationMessage = document.getElementById('password-validation-message');

passwordField.addEventListener('input', validatePassword);
confirmPasswordField.addEventListener('input', validatePassword);

function validatePassword() {
    const password = passwordField.value;
    const confirmPassword = confirmPasswordField.value;

    if (password !== confirmPassword) {
        validationMessage.textContent = "Passwords do not match";
        confirmPasswordField.setCustomValidity("Passwords do not match");
    } else {
        validationMessage.textContent = "";
        confirmPasswordField.setCustomValidity("");
    }
}



    