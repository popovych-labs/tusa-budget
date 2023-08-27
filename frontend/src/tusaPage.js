export async function tusa_page(domain, search, token){
    console.log("tusa");
    console.log(search);

    const table_inventory = document.getElementById("inventory");
    // #inventory table logic
    const button_add_row = document.getElementById("add_row");

    button_add_row.addEventListener("click", () => {
        var inputRow = button_add_row.closest("tr");
        var inputRowCells = inputRow.children;
        var anyEmptyCell = false;
        var newCellsData = [];

        for (let index = 0; index < inputRowCells.length - 1; index++) {
            var cell = inputRowCells[index];
            if (cell.textContent === "" && index < 2){
                anyEmptyCell = true;
                cell.classList.add("error_happened_with_cell");
                (function(cell) {
                    setTimeout(() => {
                        cell.classList.remove("error_happened_with_cell");
                    }, 2000);
                })(cell);
            }            
            else {
                newCellsData.push(cell.textContent);
            }
        }

        if (anyEmptyCell) return;

        var newRow = document.createElement("tr");
        for (let i=0; i < inputRowCells.length - 1; i++){
            inputRowCells[i].textContent = "";

            var cell = document.createElement("td");
            cell.textContent = newCellsData[i];
            newRow.appendChild(cell);
        }

        var deleteButton = document.createElement("button");
        deleteButton.setAttribute("id", "delete_row");
        deleteButton.textContent = "Видалити";
        deleteButton.classList.add("btn-view")

        deleteButton.addEventListener("click", async () => {
            var currentRow = deleteButton.closest("tr");
            currentRow.parentNode.removeChild(currentRow);
        });

        var cellWithButton = document.createElement("td");
        cellWithButton.appendChild(deleteButton);

        newRow.appendChild(cellWithButton);        
        table_inventory.append(newRow);
    })

    // fetch inventory items

    function appendCellToRow(row, cellData) {
        var cell = document.createElement("td");
        cell.textContent = cellData;
        row.appendChild(cell);
    }
    function appendDeleteButtonCelltoRow(row){
        var deleteButton = document.createElement("button");
        deleteButton.setAttribute("id", "delete_row");
        deleteButton.textContent = "Видалити";
        deleteButton.classList.add("btn-view");

        deleteButton.addEventListener("click", async () => {
            var currentRow = deleteButton.closest("tr");
            currentRow.parentNode.removeChild(currentRow);
        });

        var cellWithButton = document.createElement("td");
        cellWithButton.appendChild(deleteButton);
        row.appendChild(cellWithButton); 
    }


    try {
        const response = await fetch(`${domain}/api/inventory_items${search}`, {
            method: "GET",
            headers: {
                'Authorization': `Bearer ${token}`,
            }});
        
        if (response.ok){
            const data = await response.json();
            console.log(data);

            // iterate over rows
            for (let i=0; i < data.length; i++){
                var newRow = document.createElement("tr");    

                var rowData = data[i];
                console.log(rowData);

                appendCellToRow(newRow, rowData.item_name);
                appendCellToRow(newRow, rowData.price);
                appendCellToRow(newRow, rowData.owner_name);
                appendCellToRow(newRow, "");
                appendDeleteButtonCelltoRow(newRow);
                 
                table_inventory.append(newRow);
            }

        }
    } catch (error){
        console.error("Server error:", error);
        // Handle server-related errors on the frontend.
    };

};
