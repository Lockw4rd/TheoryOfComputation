var inputTape = document.getElementById("inputTape");
var buttonExecute = document.getElementById("buttonExecute");
var output = document.getElementById("output");

buttonExecute.addEventListener("click", execute);

function delta(q,s){
    log("Delta("+q+","+s+")\n");
    switch(q){
        case 0:
            if(s == 'a') return 1;
            if(s == 'b') return 0;
            if(s == 'c') return 2;
            if(s == 'a') return 0;
            if(s == 'c') return 0;
            break;
        case 1:
            if(s == 'a') return 3;
            if(s == 'b') return 0;
            if(s == 'c') return 0;
            break;
        case 2:
            if(s == 'a') return 0;
            if(s == 'b') return 0;
            if(s == 'c') return 3;
            break;
        case 3:
            if(s == 'a') return 3;
            if(s == 'b') return 3;
            if(s == 'c') return 3;
        //break;
    }
    return -1;
}

function program(q, w){
    log("Programa("+q+","+w+")");
    if(q == -1 || w.length == 0)
        return q;
    return program(delta(q, w[0]), w.substring(1));
}

function execute(){
    output.value = "";
    var final = [3];
    var initial = 0;
    var tape = inputTape.value;
    console.time("Tempo");
    var state = program(initial, tape);
    if(final.includes(state)){
        log("\n\nAceita!")
        console.log("Palavra: " + tape + "; 1: Aceita;")
        console.timeEnd("Tempo")
    } else {
        log("\n\nRejeita!")
        console.log("Palavra: " + tape + "; 0: Rejeita;");
        console.timeEnd("Tempo");
    }
    output.focus();
}

function log(text){
    output.value =  output.value +"\n"+ text;
}
