function verificar() {

    // pega o valor 
    // variavel numero aleatorio vai gerar um numero e arredondar pra baixo
    let valorUsuario = document.getElementById("numero").value;
    let numeroAleatorio = Math.floor(Math.random() * 2);

    if (valorUsuario == numeroAleatorio) {
        document.getElementById("resultado").innerHTML = "Você acertou!";
        document.getElementById("caixao").style.setProperty("background-color", "green");

    }else {
        document.getElementById("resultado").innerHTML = "Errou numero era " + numeroAleatorio;
        document.getElementById("caixao").style.setProperty("background-color", "red");

    }

}