const currentUrl = new URL(window.location.href);

const domain = currentUrl.origin;
const path = currentUrl.pathname;
// request page content

const token = localStorage.getItem('token');

fetch(currentUrl, {
    method: "POST",
    headers: {
        'Authorization': `Bearer ${token}`,
    }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const text = response.text();
        return text; // Assuming the response contains HTML/text content
    })
    .then(newContent => {
        // Step 2: Replace the current content with the new content
        const currentContent = document.querySelector('#content'); // Replace with your element's selector
        currentContent.innerHTML = newContent;
    }).
    then(() => {
        if (path === "/login"){
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
        }
        else if (path === "/dashboard")
        {
            console.log("dashboard")
        }
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });


    