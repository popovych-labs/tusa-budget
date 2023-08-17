const currentUrl = new URL(window.location.href);

const domain = currentUrl.origin;
const path = currentUrl.pathname;
const search = currentUrl.search
// request page content

const token = localStorage.getItem('token');

function login_page() {
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

function dashboard_page(){
    var button = document.getElementById("create_tusa");

    button.addEventListener("click", () => {
        window.location.href = "/tusa";
    });
    
}

function tusa_page(){
    console.log("tusa")
}

var functionDict = {
    "/login": login_page,
    "/dashboard": dashboard_page,
    "/tusa": tusa_page
}

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

        if (response.redirected){
            window.location.href = response.url;
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
        page_specific_script = functionDict[path];
        

        if (page_specific_script === undefined){
            throw new Error("Error in functionDict");
        }

        page_specific_script();
    })
    .catch(error => {
        console.error('Error caught:', error);
    });


    