export function login_page(domain, search, token) {
    const form = document.getElementById("login");
 
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(form);
        const errorMessage = document.getElementById("error-msg")

        try {
            const response = await fetch(`${domain}/api/token`, {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                const bearerToken = data.access_token;
                localStorage.setItem("token", bearerToken)

                window.location.href = "/dashboard";
                // Process the data on the frontend as needed.
            } 
            else if (response.status === 401) {
                console.error("401 Unauthorized", response)
                errorMessage.style.display = 'block';
            }
            else if (response.status === 404) {
                console.error("404 Not Found", response)
                errorMessage.style.display = "block";
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
};