const input = document.getElementById("input");
const symbols = ["(",")","/","+","-","*","=","."];

function addToDisplay(a){

    //
    if(input.value === "Error"){
        input.value = "";
    }
    else if(symbols.includes(input.value[input.value.length - 1]) && symbols.includes(a)){
        input.value = input.value.slice(0, -1) + a;
        return
    }
    
    input.value += a;
}

function clearDisplay(){
    input.value = "";
}

function calculate(){
    try{
        if(input.value === "Error" || input.value === ""){
            input.value = "Error";
        }
        else{
            input.value = eval(input.value);
        }
    }    
    catch(error){
        input.value = "Error";
    }
}
