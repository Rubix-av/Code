const input = document.getElementById("input");

function addToDisplay(a){

    input.value += a;
}

function clearDisplay(){
    input.value = "";
}

function calculate(){
    try{
        input.value = eval(input.value);
    }    
    catch(error){
        input.value = "Error";
    }
}
