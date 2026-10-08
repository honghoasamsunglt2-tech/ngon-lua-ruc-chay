import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ngọn lửa rực cháy",
    page_icon="🔥",
    layout="centered"
)

game = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">

<style>
*{
    box-sizing:border-box;
    -webkit-tap-highlight-color:transparent;
}

html,body{
    margin:0;
    padding:0;
    background:#050505;
    color:white;
    font-family:Arial,sans-serif;
}

body{
    display:flex;
    justify-content:center;
}

#game{
    width:min(100vw,520px);
    min-height:100vh;
    background:
        radial-gradient(circle at 50% 15%,#4d0900 0%,#160300 35%,#050505 75%);
    overflow:hidden;
    position:relative;
}

/* ================= MENU ================= */

#menu{
    min-height:100vh;
    padding:35px 22px 30px;
    text-align:center;
}

.title{
    font-size:clamp(38px,10vw,62px);
    font-weight:1000;
    font-style:italic;
    line-height:1.02;
    color:#ff2414;
    text-shadow:
        0 0 5px #ff0000,
        0 0 15px #ff1a00,
        0 0 30px #ff3000,
        0 0 55px #ff0000;
    animation:heartBeat 1.25s infinite;
}

@keyframes heartBeat{
    0%,100%{
        transform:scale(1);
    }
    15%{
        transform:scale(1.04);
    }
    30%{
        transform:scale(1);
    }
    45%{
        transform:scale(1.035);
    }
}

.subtitle{
    margin-top:22px;
    font-size:24px;
    letter-spacing:3px;
    color:#ffd5cc;
    font-weight:bold;
}

.section-title{
    margin:25px 0 10px;
    font-size:22px;
    font-weight:bold;
    color:#ff704d;
}

/* NHẠC */

.musicBox{
    margin:18px auto;
    max-width:440px;
    height:75px;
    border:2px solid #ff4a32;
    border-radius:24px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 12px 0 22px;
    background:rgba(60,5,0,.7);
    box-shadow:0 0 18px rgba(255,40,10,.35);
}

.musicName{
    font-size:21px;
    font-weight:bold;
}

.musicButton{
    border:none;
    border-radius:18px;
    padding:14px 24px;
    font-size:18px;
    font-weight:bold;
    color:white;
    background:linear-gradient(135deg,#ff9d00,#ff2600);
    box-shadow:0 0 12px #ff4b16;
}

/* HÀNG NÚT */

.row{
    display:flex;
    gap:12px;
    width:100%;
}

.row button{
    flex:1;
}

.menuButton{
    min-height:65px;
    border:2px solid #ff402c;
    border-radius:22px;
    background:#180707;
    color:white;
    font-size:20px;
    font-weight:bold;
    box-shadow:0 0 12px rgba(255,30,10,.25);
}

.menuButton.selected{
    background:linear-gradient(135deg,#ffb000,#ff2500);
    border-color:#ffd25a;
    box-shadow:
        0 0 12px #ff4c00,
        0 0 25px rgba(255,50,0,.5);
}

.carButton{
    min-height:78px;
    border:2px solid #ff402c;
    border-radius:22px;
    background:#180707;
    color:white;
    font-size:19px;
    font-weight:bold;
}

.startButton{
    width:100%;
    margin-top:28px;
    min-height:78px;
    border:none;
    border-radius:25px;
    background:linear-gradient(135deg,#ff8c00,#ff0800);
    color:white;
    font-size:28px;
    font-weight:1000;
    box-shadow:
        0 0 15px #ff2700,
        0 0 35px rgba(255,40,0,.5);
    animation:startPulse 1.4s infinite;
}

@keyframes startPulse{
    0%,100%{transform:scale(1)}
    50%{transform:scale(1.025)}
}

.record{
    margin-top:25px;
    font-size:23px;
    font-weight:bold;
    color:#ffe6c7;
}

/* ================= GAME ================= */

#gameScreen{
    display:none;
    width:100%;
    min-height:100vh;
    position:relative;
}

.topBar{
    height:92px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:10px 15px;
    background:#080808;
    position:relative;
    z-index:20;
}

.hearts{
    font-size:25px;
    font-weight:bold;
}

.score{
    font-size:30px;
    font-weight:bold;
}

.pauseButton{
    width:62px;
    height:62px;
    border:0;
    border-radius:18px;
    background:#222;
    color:white;
    font-size:35px;
}

.soundGame{
    width:58px;
    height:58px;
    border:0;
    border-radius:18px;
    background:#222;
    color:white;
    font-size:25px;
}

.road{
    width:76%;
    max-width:400px;
    height:520px;
    margin:0 auto;
    position:relative;
    overflow:hidden;
    background:
        repeating-linear-gradient(
            to bottom,
            #343434 0px,
            #343434 85px,
            #414141 85px,
            #414141 170px
        );
    border-left:8px solid #666;
    border-right:8px solid #666;
}

.lane{
    position:absolute;
    top:0;
    bottom:0;
    width:5px;
    background:
        repeating-linear-gradient(
            to bottom,
            white 0px,
            white 40px,
            transparent 40px,
            transparent 85px
        );
    opacity:.9;
}

.lane1{left:33.33%}
.lane2{left:66.66%}

.player{
    position:absolute;
    width:58px;
    height:58px;
    font-size:48px;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:10;
    user-select:none;
    touch-action:none;
}

.obstacle{
    position:absolute;
    width:58px;
    height:58px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:43px;
    z-index:8;
}

.pothole{
    font-size:48px;
}

.controls{
    width:76%;
    max-width:400px;
    margin:10px auto 0;
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
}

.control{
    height:58px;
    border:2px solid #ff3b20;
    border-radius:18px;
    background:#170606;
    color:white;
    font-size:27px;
    font-weight:bold;
    user-select:none;
    touch-action:none;
}

.control:active{
    background:#ff2600;
}

/* GAME OVER */

#gameOver{
    display:none;
    position:absolute;
    inset:0;
    background:rgba(0,0,0,.82);
    z-index:50;
    align-items:center;
    justify-content:center;
    flex-direction:column;
}

.gameOverText{
    font-size:52px;
    font-weight:1000;
    color:#ff1717;
    text-shadow:
        0 0 8px red,
        0 0 20px red,
        0 0 40px red;
    animation:fall 1s ease-out;
}

@keyframes fall{
    0%{
        transform:translateY(-400px) rotate(-8deg);
    }
    65%{
        transform:translateY(25px) rotate(4deg);
    }
    80%{
        transform:translateY(-12px) rotate(-2deg);
    }
    100%{
        transform:translateY(0) rotate(0);
    }
}

.finalScore{
    font-size:24px;
    margin:18px;
}

.overButtons{
    display:flex;
    gap:12px;
}

.overButtons button{
    border:2px solid #ff3b20;
    background:#250606;
    color:white;
    border-radius:16px;
    padding:14px 20px;
    font-size:17px;
    font-weight:bold;
}

/* PAUSE */

#pauseScreen{
    display:none;
    position:absolute;
    inset:0;
    background:rgba(0,0,0,.82);
    z-index:40;
    align-items:center;
    justify-content:center;
    flex-direction:column;
}

.pauseTitle{
    font-size:42px;
    font-weight:bold;
    margin-bottom:20px;
}

.pauseBtn{
    width:210px;
    margin:7px;
    padding:15px;
    border-radius:17px;
    border:2px solid #ff3c20;
    background:#180606;
    color:white;
    font-size:19px;
    font-weight:bold;
}
</style>
</head>

<body>

<div id="game">

<!-- ================= MENU ================= -->

<div id="menu">

    <div class="title">
        🔥 NGỌN LỬA<br>RỰC CHÁY 🔥
    </div>

    <div class="subtitle">
        🏁 FIRE ROAD RACING 🏁
    </div>

    <div class="musicBox">
        <div class="musicName">🎵 NHẠC</div>
        <button class="musicButton" id="menuMusic"
                onclick="toggleMusic()">
            🔊 BẬT
        </button>
    </div>

    <div class="section-title">⚡ ĐỘ KHÓ ⚡</div>

    <div class="row">
        <button class="menuButton selected"
                id="easy"
                onclick="chooseDifficulty('easy')">
            DỄ
        </button>

        <button class="menuButton"
                id="medium"
                onclick="chooseDifficulty('medium')">
            VỪA
        </button>

        <button class="menuButton"
                id="hard"
                onclick="chooseDifficulty('hard')">
            KHÓ
        </button>
    </div>

    <div class="section-title">🚗 CHỌN XE 🚕</div>

    <div class="row">

        <button class="carButton selected"
                id="redCar"
                onclick="chooseCar('red')">
            🚗 XE ĐỎ
        </button>

        <button class="carButton"
                id="yellowCar"
                onclick="chooseCar('yellow')">
            🚕 XE VÀNG
        </button>

    </div>

    <button class="startButton"
            onclick="startGame()">
        🔥 BẮT ĐẦU 🔥
    </button>

    <div class="record">
        🏆 KỶ LỤC: <span id="record">0</span>
    </div>

</div>


<!-- ================= GAME ================= -->

<div id="gameScreen">

    <div class="topBar">

        <div class="hearts" id="hearts">
            3❤️
        </div>

        <button class="soundGame"
                onclick="toggleMusic()"
                id="gameSound">
            🔊
        </button>

        <div class="score" id="score">
            0
        </div>

        <button class="pauseButton"
                onclick="pauseGame()">
            ☰
        </button>

    </div>

    <div class="road" id="road">

        <div class="lane lane1"></div>
        <div class="lane lane2"></div>

        <div class="player"
             id="player">
            🚗
        </div>

    </div>

    <div class="controls">

        <button class="control"
                id="left">
            ◀
        </button>

        <button class="control"
                id="right">
            ▶
        </button>

        <button class="control"
                id="up">
            ▲
        </button>

        <button class="control"
                id="down">
            ▼
        </button>

    </div>


    <!-- PAUSE -->

    <div id="pauseScreen">

        <div class="pauseTitle">
            ⏸ TẠM DỪNG
        </div>

        <button class="pauseBtn"
                onclick="resumeGame()">
            ▶ TIẾP TỤC
        </button>

        <button class="pauseBtn"
                onclick="backToMenu()">
            🏠 VỀ MENU
        </button>

    </div>


    <!-- GAME OVER -->

    <div id="gameOver">

        <div class="gameOverText">
            GAME OVER
        </div>

        <div class="finalScore">
            Điểm: <span id="finalScore">0</span>
        </div>

        <div class="overButtons">

            <button onclick="backToMenu()">
                🏠 VỀ MENU
            </button>

            <button onclick="restartGame()">
                🔄 CHƠI LẠI
            </button>

        </div>

    </div>

</div>


<!-- ================= AUDIO ================= -->

<audio id="bgMusic" loop preload="auto">
    <source src="Nhạc game.mp3" type="audio/mpeg">
</audio>

<audio id="gameOverMusic" preload="auto">
    <source src="Nhạc game kết thúc.mp3" type="audio/mpeg">
</audio>


<script>

const player = document.getElementById("player");
const road = document.getElementById("road");
const menu = document.getElementById("menu");
const gameScreen = document.getElementById("gameScreen");
const pauseScreen = document.getElementById("pauseScreen");
const gameOverScreen = document.getElementById("gameOver");

const bgMusic = document.getElementById("bgMusic");
const gameOverMusic = document.getElementById("gameOverMusic");

let musicOn = true;
let difficulty = "easy";
let selectedCar = "red";

let hearts = 3;
let score = 0;
let running = false;
let paused = false;

let playerX = 0;
let playerY = 0;

let speed = 4;
let obstacles = [];
let spawnTimer = null;
let animation = null;


/* ================= MENU ================= */

function chooseDifficulty(level){

    difficulty = level;

    document.querySelectorAll(".menuButton")
        .forEach(b => b.classList.remove("selected"));

    document.getElementById(level)
        .classList.add("selected");
}


function chooseCar(car){

    selectedCar = car;

    document.getElementById("redCar")
        .classList.remove("selected");

    document.getElementById("yellowCar")
        .classList.remove("selected");

    if(car === "red"){
        document.getElementById("redCar")
            .classList.add("selected");
    }else{
        document.getElementById("yellowCar")
            .classList.add("selected");
    }
}


/* ================= MUSIC ================= */

function toggleMusic(){

    musicOn = !musicOn;

    if(musicOn){

        bgMusic.play().catch(()=>{});

        document.getElementById("menuMusic").textContent = "🔊 BẬT";
        document.getElementById("gameSound").textContent = "🔊";

    }else{

        bgMusic.pause();

        document.getElementById("menuMusic").textContent = "🔇 TẮT";
        document.getElementById("gameSound").textContent = "🔇";
    }
}


/* ================= START ================= */

function startGame(){

    menu.style.display = "none";
    gameScreen.style.display = "block";

    hearts = 3;
    score = 0;
    paused = false;
    running = true;

    document.getElementById("score").textContent = "0";

    updateHearts();

    if(difficulty === "easy"){
        speed = 4;
    }

    if(difficulty === "medium"){
        speed = 6;
    }

    if(difficulty === "hard"){
        speed = 11;
    }

    if(selectedCar === "red"){
        player.textContent = "🚗";
    }else{
        player.textContent = "🚕";
    }

    resetPlayer();

    clearObstacles();

    if(musicOn){
        bgMusic.play().catch(()=>{});
    }

    gameLoop();

    spawnTimer = setInterval(
        spawnObstacle,
        difficulty === "hard" ? 520 : 750
    );
}


/* ================= PLAYER ================= */

function resetPlayer(){

    playerX =
        (road.clientWidth - player.offsetWidth) / 2;

    playerY =
        road.clientHeight - 100;

    updatePlayer();
}


function updatePlayer(){

    player.style.left = playerX + "px";
    player.style.top = playerY + "px";
}


/*
GIỮ NÚT = XE CHẠY LIÊN TỤC
*/

let moveLeft = false;
let moveRight = false;
let moveUp = false;
let moveDown = false;

function holdButton(id, direction){

    const btn = document.getElementById(id);

    const start = e => {
        e.preventDefault();
        window[direction] = true;
    };

    const end = e => {
        e.preventDefault();
        window[direction] = false;
    };

    btn.addEventListener("pointerdown", start);
    btn.addEventListener("pointerup", end);
    btn.addEventListener("pointercancel", end);
    btn.addEventListener("pointerleave", end);
}

holdButton("left","moveLeft");
holdButton("right","moveRight");
holdButton("up","moveUp");
holdButton("down","moveDown");


function movePlayer(){

    const amount = 7;

    if(moveLeft){
        playerX -= amount;
    }

    if(moveRight){
        playerX += amount;
    }

    if(moveUp){
        playerY -= amount;
    }

    if(moveDown){
        playerY += amount;
    }

    const maxX =
        road.clientWidth - player.offsetWidth;

    const maxY =
        road.clientHeight - player.offsetHeight;

    playerX = Math.max(0,Math.min(maxX,playerX));
    playerY = Math.max(0,Math.min(maxY,playerY));

    updatePlayer();
}


/* ================= OBSTACLES ================= */

const obstacleTypes = [
    "🛻",
    "🚛",
    "🚚",
    "🚧",
    "🕳️"
];


function spawnObstacle(){

    if(!running || paused) return;

    const el = document.createElement("div");

    el.className = "obstacle";

    const type =
        obstacleTypes[
            Math.floor(Math.random()*obstacleTypes.length)
        ];

    el.textContent = type;

    const maxX =
        road.clientWidth - 58;

    el.style.left =
        Math.random()*maxX + "px";

    el.style.top = "-65px";

    road.appendChild(el);

    obstacles.push({
        el:el,
        x:parseFloat(el.style.left),
        y:-65,
        type:type,
        speed:speed
    });
}


/* ================= COLLISION ================= */

function collision(a,b){

    const r1 = a.getBoundingClientRect();
    const r2 = b.getBoundingClientRect();

    return !(
        r1.right < r2.left ||
        r1.left > r2.right ||
        r1.bottom < r2.top ||
        r1.top > r2.bottom
    );
}


function loseHeart(){

    hearts--;

    updateHearts();

    if(hearts <= 0){
        endGame();
    }
}


function updateHearts(){

    document.getElementById("hearts")
        .textContent = hearts + "❤️";
}


/* ================= GAME LOOP ================= */

function gameLoop(){

    if(!running){
        return;
    }

    if(!paused){

        movePlayer();

        for(let i=obstacles.length-1;i>=0;i--){

            const o = obstacles[i];

            o.y += o.speed;

            o.el.style.top = o.y + "px";

            if(collision(player,o.el)){

                if(o.type === "🕳️"){
                    endGame();
                    return;
                }

                loseHeart();

                o.el.remove();
                obstacles.splice(i,1);

                continue;
            }

            if(o.y > road.clientHeight){

                score++;

                document.getElementById("score")
                    .textContent = score;

                o.el.remove();
                obstacles.splice(i,1);
            }
        }
    }

    animation =
        requestAnimationFrame(gameLoop);
}


/* ================= GAME OVER ================= */

function endGame(){

    running = false;

    clearInterval(spawnTimer);

    cancelAnimationFrame(animation);

    obstacles.forEach(o => o.el.remove());

    obstacles = [];

    bgMusic.pause();

    document.getElementById("finalScore")
        .textContent = score;

    gameOverScreen.style.display = "flex";

    if(musicOn){
        gameOverMusic.currentTime = 0;
        gameOverMusic.play().catch(()=>{});
    }

    let oldRecord =
        Number(localStorage.getItem("ngonLuaRecord") || 0);

    if(score > oldRecord){

        localStorage.setItem(
            "ngonLuaRecord",
            score
        );

        document.getElementById("record")
            .textContent = score;
    }
}


/* ================= RESTART ================= */

function restartGame(){

    gameOverScreen.style.display = "none";

    startGame();
}


/* ================= PAUSE ================= */

function pauseGame(){

    if(!running) return;

    paused = true;

    pauseScreen.style.display = "flex";
}


function resumeGame(){

    paused = false;

    pauseScreen.style.display = "none";
}


function backToMenu(){

    running = false;

    clearInterval(spawnTimer);

    cancelAnimationFrame(animation);

    obstacles.forEach(o => o.el.remove());

    obstacles = [];

    bgMusic.pause();

    gameOverMusic.pause();

    pauseScreen.style.display = "none";
    gameOverScreen.style.display = "none";

    gameScreen.style.display = "none";
    menu.style.display = "block";

    document.getElementById("record")
        .textContent =
        localStorage.getItem("ngonLuaRecord") || 0;
}


/* ================= LOAD RECORD ================= */

document.getElementById("record")
    .textContent =
    localStorage.getItem("ngonLuaRecord") || 0;

</script>

</div>

</body>
</html>
"""

components.html(
    game,
    height=900,
    scrolling=False
)
