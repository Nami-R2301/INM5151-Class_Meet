const reg_txt = new RegExp('[,$?\'-;:/~`%^&*()@#!]');
const reg_email = new RegExp('([a-zA-z0-9\\-éàèêçîô`.]*@[a-zA-Z]*\\.(com|ca|org|edu|fr))');

const check_name = () => {
    let valid = true;
    document.getElementById("error_name").innerHTML = "";
    let msgE = "\tLe nom doit être minimalement composé de 2 caractères !".fontcolor("RED");
    let msgE2 = "\tLe nom ne doit pas contenir des caractères spéciaux !".fontcolor("RED");
    if (document.getElementById("name").value.search(reg_txt) !== -1) {
        console.log(document.getElementById("name").innerHTML.search(reg_email));
        document.getElementById("error_name").innerHTML = msgE2;
        valid = false;
    } else if (document.getElementById("name").value.length < 2) {
        document.getElementById("error_name").innerHTML = msgE;
        valid = false;
    }
    return valid;
}

const check_email = () => {
    let valid = true;
    document.getElementById("error_email").innerHTML = "";
    let msgE2 = "\tL'adresse courriel n'est pas une adresse de format valide !".fontcolor("RED");

    if (document.getElementById("email").value.search(reg_email) === -1
        || document.getElementById("email").value.length < 4) {
        console.log(document.getElementById("email").innerHTML.search(reg_email));
        document.getElementById("error_email").innerHTML = msgE2;
        valid = false;
    }
    return valid;
}

const check_password = () => {
    let valid = true;
    document.getElementById("error_pw").innerHTML = "";
    let msgE = "\tLe mot de passe ne peut être laissé vide !".fontcolor("RED");

    if (document.getElementById("pw").value.search(reg_email) === -1) {
        document.getElementById("error_pw").innerHTML = msgE;
        valid = false;
    }
    return valid;
}


const onSubmit = () => {
    let valide = true;
    const form = document.querySelector('form');
    for (let i = 0; i < 4; ++i) {
        if(!valide) break;
        document.getElementById("error_" + form.elements[i].id).innerHTML = "";
        document.getElementById(form.elements[i].id).style.borderColor = "#6c757d";
        if (i === 0) {
            valide = check_name();
        } else if (i === 1) {
            valide = check_email();
        } else valide = check_password();
    }
    return valide;
}