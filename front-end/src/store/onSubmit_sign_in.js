const reg_email = new RegExp('([a-zA-z0-9\\-éàèêçîô`.]*@[a-zA-Z]*\\.(com|ca|org|edu|fr))');


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
    document.getElementById("error_pw").innerHTML = "";
    let msgE = "\tLe mot de passe ne peut être laissé vide !".fontcolor("RED");
    if (document.getElementById("pw").value.length > 1) {
        document.getElementById("error_pw").innerHTML = msgE;
    }

    return document.getElementById("pw").value.length > 1;
}

const onSubmit = () => {
    let valide = true;
    const form = document.querySelector('form');
    for (let i = 0; i < 4; ++i) {
        if(!valide) break;
        document.getElementById("error_" + form.elements[i].id).innerHTML = "";
        document.getElementById(form.elements[i].id).style.borderColor = "#6c757d";
        if (i === 0) {
            valide = check_email();
        } else valide = check_password();
    }
    return valide;
}