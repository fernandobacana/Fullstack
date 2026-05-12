// script.js

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let score = 0;
let time = 30;

let gameRunning = false;

let speed = 1000;

const player = {
    x: 400,
    y: 350,
    width: 60,
    height: 90,
    speed: 2.5
};

const block = {
    x: 100,
    y: 100,
    size: 60
};

const keys = {};

let blockInterval;
let timerInterval;

document.addEventListener("keydown", (e) => {

  // impede repetir infinitamente segurando tecla
  if(keys[e.key.toLowerCase()]){
    return;
  }

  keys[e.key.toLowerCase()] = true;

  // quebrar bloco com espaço
  if(e.code === "Space"){
    breakBlock();
  }

});

document.addEventListener("keyup", (e) => {

    keys[e.key.toLowerCase()] = false;

});

function randomBlock() {

    block.x = Math.random() * (canvas.width - block.size);
    block.y = Math.random() * (canvas.height - block.size - 100);

}

function movePlayer() {

    if (keys["w"]) {
        player.y -= player.speed;
    }

    if (keys["s"]) {
        player.y += player.speed;
    }

    if (keys["a"]) {
        player.x -= player.speed;
    }

    if (keys["d"]) {
        player.x += player.speed;
    }

    // limites da tela
    if (player.x < 0) {
        player.x = 0;
    }

    if (player.y < 0) {
        player.y = 0;
    }

    if (player.x + player.width > canvas.width) {
        player.x = canvas.width - player.width;
    }

    if (player.y + player.height > canvas.height) {
        player.y = canvas.height - player.height;
    }

}

function drawSteve() {

    // cabeça
    ctx.fillStyle = "#d9a066";
    ctx.fillRect(player.x + 10, player.y, 40, 40);

    // cabelo
    ctx.fillStyle = "#4b2e1e";
    ctx.fillRect(player.x + 10, player.y, 40, 12);

    // corpo
    ctx.fillStyle = "#00aaff";
    ctx.fillRect(player.x + 12, player.y + 40, 36, 35);

    // pernas
    ctx.fillStyle = "#222288";
    ctx.fillRect(player.x + 12, player.y + 75, 14, 20);
    ctx.fillRect(player.x + 34, player.y + 75, 14, 20);

    // braço esquerdo
    ctx.fillStyle = "#d9a066";
    ctx.fillRect(player.x, player.y + 40, 10, 30);

    // braço direito
    ctx.fillRect(player.x + 50, player.y + 40, 10, 30);

    // picareta simples
    ctx.fillStyle = "#8b5a2b";

    // cabo
    ctx.fillRect(player.x + 55, player.y + 50, 5, 25);

    // topo da picareta
    ctx.fillStyle = "#aaaaaa";
    ctx.fillRect(player.x + 48, player.y + 45, 20, 5);

}

function drawBlock() {

    ctx.fillStyle = "#8b5a2b";
    ctx.fillRect(block.x, block.y, block.size, block.size);

    ctx.strokeStyle = "#5c3b1a";
    ctx.lineWidth = 3;
    ctx.strokeRect(block.x, block.y, block.size, block.size);

}

function breakBlock() {

    const distanceX = Math.abs((player.x + 30) - (block.x + 30));
    const distanceY = Math.abs((player.y + 45) - (block.y + 30));

    // alcance da picareta
    if (distanceX < 80 && distanceY < 80) {

        score++;

        document.getElementById("score").innerText = score;

        randomBlock();
    }

}

function drawBackground() {

    // céu
    ctx.fillStyle = "#87ceeb";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // chão
    ctx.fillStyle = "#55aa55";
    ctx.fillRect(0, 430, canvas.width, 70);

}

function gameLoop() {

    if (!gameRunning) {
        return;
    }

    movePlayer();

    drawBackground();

    drawBlock();

    drawSteve();

    requestAnimationFrame(gameLoop);

}

// SUBSTITUA A FUNÇÃO startGame POR ESSA:

function startGame(level){

  clearInterval(blockInterval);
  clearInterval(timerInterval);

  score = 0;
  time = 30;


  document.getElementById("score").innerText = score;
  document.getElementById("time").innerText = time;

  if(level === "facil"){
    speed = 1200;
  }

  if(level === "medio"){
    speed = 800;
  }

  if(level === "dificil"){
    speed = 500;
  }

  randomBlock();

  gameRunning = true;

  gameLoop();

  blockInterval = setInterval(() => {

    randomBlock();

  }, speed);

  timerInterval = setInterval(() => {

    time--;

    document.getElementById("time").innerText = time;

    if(time <= 0){

      clearInterval(blockInterval);
      clearInterval(timerInterval);

      gameRunning = false;

      alert("Fim de jogo! Pontuação: " + score);

    }

  }, 1000);

}   