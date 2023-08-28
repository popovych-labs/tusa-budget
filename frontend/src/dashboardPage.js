export function dashboard_page(domain, search, token){
    const create_tusa_endpoint = `${domain}/api/create_tusa`;

    var button = document.getElementById("create_tusa");

    button.addEventListener("click", async (event) => {
        event.preventDefault();

        fetch(create_tusa_endpoint, {
            method: "POST",
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        }).then(async (response) => {
            const data = await response.json();
            const tusa_id = data.id;
            window.location.href = `/tusa?id=${tusa_id}`;
        }).catch((error) => {
            console.error("Server error: ", error);
        });
    });
};