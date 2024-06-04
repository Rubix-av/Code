const inputBox = document.getElementById("input-box"); // refers to input box
const listContainer = document.getElementById("list-container"); // refers to container for <li>

function addTask(){
    if(inputBox.value === ""){
        alert("You must write something");
    }
    else{
        let li = document.createElement("li"); // creates an element li of <li> tag
        li.innerHTML = inputBox.value; // assigns value from inputBox to this <li> tag
        listContainer.appendChild(li); // appends child to container
        let span = document.createElement("span");
        span.innerHTML = "\u00d7"; // "\u00d7" is a code for cross icon
        li.appendChild(span);
    }
    inputBox.value = "";
    saveData();
}

listContainer.addEventListener("click", (e) => {
    if(e.target.tagName === "LI"){ 
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData(){
    localStorage.setItem("data", listContainer.innerHTML);
}

function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}
showTask();
