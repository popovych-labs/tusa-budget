import './style.css'

import { login_page } from './src/loginPage.js';
import { dashboard_page } from './src/dashboardPage.js'
import { tusa_page } from "./src/tusaPage";

import PlaceholderInitialsAvatar from "./src/libs/avatar.js";

var functionDict = {
    "/login": login_page,
    "/dashboard": dashboard_page,
    "/tusa": tusa_page
};

(function main() {

    const currentUrl = new URL(window.location.href);

    const domain = currentUrl.origin;
    const path = currentUrl.pathname;
    const search = currentUrl.search
    // request page content

    const token = localStorage.getItem('token');
    console.log(domain)

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

            const avatarPlaceholder = document.getElementById("avatar");
            if (avatarPlaceholder) {
                var avatarElement = PlaceholderInitialsAvatar.render(token);
                avatarPlaceholder.appendChild(avatarElement);
            }
        }).
        then(() => {
            const page_specific_script = functionDict[path];        
    
            if (page_specific_script === undefined){
                throw new Error("Error in functionDict");
            }
    
            page_specific_script(domain, search,  token);
        })
        .catch(error => {
            console.error('Error caught:', error);
        });
})();




    