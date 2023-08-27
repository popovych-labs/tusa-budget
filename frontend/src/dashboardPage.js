export function dashboard_page(domain, search, token){
    var button = document.getElementById("create_tusa");

    button.addEventListener("click", async (event) => {
        event.preventDefault();

        try {

            const response = await fetch(`${domain}/api/create_tusa`, {
                method: "POST",
                headers: {
                    'Authorization': `Bearer ${token}`,
            }});
            if (response.ok) {
                const data = await response.json();
                const tusa_id = data.id;
                window.location.href = `/tusa?id=${tusa_id}`;
            }
            else {
                throw new Error("Something when wrong while creating Tusa resource");
            }
    
        } catch (error) {
            console.error("Server error:", error);
        };
        // window.location.href = "/tusa";
    });
    
};