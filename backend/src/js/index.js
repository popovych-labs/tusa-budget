const currentDomain = window.location.origin

const domain = `${currentDomain}`

const form = document.getElementById("login");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const errorMessage = document.getElementById("error-msg")

    try {
        const response = await fetch(`${domain}/login`, {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            window.location.href = "/action_select"
            // Process the data on the frontend as needed.
        } 
        else if (response.status === 401) {
            console.error("401 Unauthorized", response)
            errorMessage.style.display = 'block';
        }
        else {
            const errorData = await response.json();
            console.error("Form submission error:", errorData);
            // Handle the validation error on the frontend.
        }
    } catch (error) {
        console.error("Server error:", error);
        // Handle server-related errors on the frontend.
    }
});