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
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
*{
    box-sizing:border-box;
    user-select:none;
    -webkit-user-select:none;
}

body{
    margin:0;
    background:#080808;
    font-family:Arial,sans-serif;
    color:white;
    overflow:hidden;
}

#game{
    width:min(100vw,520px);
    height:760px;
    margin:auto;
    position:relative;
    background:#080808;
    overflow:hidden;
}

/* ================= MENU ================= */

#menu{
    position:absolute;
    inset:0;
    background:
        radial-gradient(circle at center,#301010 0%,#090909 65%);
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    z-index:20;
}

.title{
    font-size:48px;
    font-weight:900;
    font-style:italic;
    text-align:center;
    color:#ff2020;
    text-shadow:
        0 0 5px #ff0000,
        0 0 15px #ff3b00,
        0 0 30px #ff0000;
    animation:heartbeat 1.15s infinite;
    margin-bottom:12px;
}

@keyframes heartbeat{
    0%,100%{transform:scale(1)}
    15%{transform:scale(1.06)}
    30%{transform:scale(1)}
    45%{transform:scale(1.04)}
    60%{transform:scale(1)}
}

.subtitle{
    font-size:17px;
    color:#ffb0b0;
    font-style:italic;
    margin-bottom:28px;
}

.menuBox{
    width:88%;
    max-width:390px;
    padding:20px;
    border-radius:20px;
    background:rgba(25,25,25,.94);
    border:1px solid #ff2929;
    box-shadow:0 0 25px rgba(255,0,0,.25);
}

.label{
    text-align:center;
    font-weight:bold;
    margin:10px 0;
}

.row{
    display:flex;
    gap:10px;
    justify-content:center;
    margin-bottom:12px;
}

button{
    border:none;
    color:white;
    font-weight:bold;
    cursor:pointer;
}

.choice{
    flex:1;
    padding:12px 8px;
    border-radius:12px;
    background:#292929;
    border:1px solid #555;
    font-size:16px;
}

.choice.selected{
    background:#b51212;
    border-color:#ff3333;
    box-shadow:0 0 12px #ff0000;
}

.start{
    width:100%;
    padding:15px;
    margin-top:10px;
    border-radius:14px;
    background:#e31313;
    font-size:21px;
    box-shadow:0 0 18px rgba(255,0,0,.45);
}

.record{
    text-align:center;
    margin-top:15px;
    padding:10px;
    border-radius:12px;
    background:#151515;
    color:#ffd45c;
}

.musicMenu{
    display:flex;
    align-items:center;
    justify-content:space-between;
    background:#151515;
    border-radius:12px;
    padding:10px 14px;
    margin-bottom:12px;
}

/* ================= GAME ================= */

#play{
    display:none;
    position:absolute;
    inset:0;
}

.topbar{
    height:75px;
    background:#090909;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 18px;
    position:relative;
    z-index:10;
}

.hearts{
    font-size:25px;
    font-weight:bold;
    color:#ff2020;
}

.score{
    font-size:27px;
    font-weight:bold;
}

.soundBtn,
.pauseBtn{
    width:55px;
    height:55px;
    border-radius:15px;
    background:#222;
    font-size:24px;
}

.pauseBtn{
    font-size:32px;
}

/* ĐƯỜNG ĐUA NGẮN VỪA KHUNG */

.road{
    position:absolute;
    left:10%;
    right:10%;
    top:75px;
    height:560px;
    overflow:hidden;
    background:#363636;
    border-left:10px solid #606060;
    border-right:10px solid #606060;
}

.road:before,
.road:after{
    content:"";
    position:absolute;
    top:0;
    bottom:0;
    width:7px;
    background:repeating-linear-gradient(
        to bottom,
        white 0 55px,
        transparent 55px 110px
    );
    opacity:.9;
}

.road:before{
    left:33.333%;
    transform:translateX(-50%);
}

.road:after{
    left:66.666%;
    transform:translateX(-50%);
}

/* nền đường chạy */

.roadMoving{
    position:absolute;
    inset:-300px 0 0 0;
    background:
        repeating-linear-gradient(
            to bottom,
            rgba(255,255,255,.025) 0 70px,
            rgba(0,0,0,.05) 70px 140px
        );
    animation:roadmove .35s linear infinite;
}

@keyframes roadmove{
    from{transform:translateY(0)}
    to{transform:translateY(140px)}
}

/* XE */

.car{
    position:absolute;
    font-size:50px;
    z-index:5;
    transform:translate(-50%,-50%);
}

.player{
    font-size:55px;
    z-index:8;
    touch-action:none;
}

/* ĐIỀU KHIỂN */

.controls{
    position:absolute;
    bottom:12px;
    left:0;
    right:0;
    height:95px;
    z-index:12;
    display:flex;
    justify-content:center;
    align-items:center;
    gap:8px;
}

.ctrl{
    width:58px;
    height:58px;
    border-radius:15px;
    background:#242424;
    border:2px solid #555;
    font-size:27px;
    box-shadow:0 4px 10px rgba(0,0,0,.5);
}

/* PAUSE */

#pauseScreen,
#gameOver{
    display:none;
    position:absolute;
    inset:0;
    z-index:30;
    background:rgba(0,0,0,.82);
    align-items:center;
    justify-content:center;
    flex-direction:column;
}

.pauseBox{
    background:#171717;
    padding:25px;
    border-radius:20px;
    width:80%;
    text-align:center;
}

.pauseBox button{
    width:100%;
    padding:13px;
    border-radius:12px;
    background:#c91515;
    margin-top:10px;
    font-size:17px;
}

/* GAME OVER */

.gameOverText{
    font-size:55px;
    font-weight:900;
    color:#ff2424;
    text-shadow:0 0 15px red;
    animation:fall .8s cubic-bezier(.2,.8,.3,1) forwards;
}

@keyframes fall{
    0%{
        transform:translateY(-350px) rotate(-8deg);
        opacity:0;
    }
    60%{
        transform:translateY(25px) rotate(4deg);
        opacity:1;
    }
    75%{
        transform:translateY(-12px) rotate(-2deg);
    }
    100%{
        transform:translateY(0) rotate(0);
        opacity:1;
    }
}

.gameOver button{
    margin-top:30px;
    padding:14px 35px;
    border-radius:14px;
    background:#d71919;
    font-size:18px;
}

@media(max-height:700px){
    #game{
        height:680px;
    }

    .road{
        height:485px;
    }

    .controls{
        bottom:5px;
    }
}
</style>
</head>

<body>

<div id="game">

<!-- ================= MENU ================= -->

<div id="menu">

    <div class="title">
        🔥 NGỌN LỬA RỰC CHÁY 🔥
    </div>

    <div class="subtitle">
        🏎️ FIRE ROAD RACING 🏎️
    </div>

    <div class="menuBox">

        <div class="musicMenu">
            <span>🎵 NHẠC</span>
            <button class="choice" id="menuMusic"
                    onclick="toggleMusic()">
                🔊 BẬT
            </button>
        </div>

        <div class="label">⚡ CHỌN CẤP ĐỘ</div>

        <div class="row">
            <button class="choice selected"
                    onclick="selectDifficulty('easy',this)">
                DỄ
            </button>

            <button class="choice"
                    onclick="selectDifficulty('medium',this)">
                VỪA
            </button>

            <button class="choice"
                    onclick="selectDifficulty('hard',this)">
                KHÓ
            </button>
        </div>

        <div class="label">🚗 CHỌN XE</div>

        <div class="row">
            <button class="choice selected"
                    onclick="selectCar('🚗',this)">
                🔴 ĐỎ
            </button>

            <button class="choice"
                    onclick="selectCar('🚕',this)">
                🟡 VÀNG
            </button>
        </div>

        <button class="start" onclick="startGame()">
            🔥 BẮT ĐẦU
        </button>

        <div class="record">
            🏆 KỶ LỤC: <span id="menuRecord">0</span>
        </div>

    </div>
</div>


<!-- ================= GAME ================= -->

<div id="play">

    <div class="topbar">

        <div class="hearts" id="hearts">
            3❤️
        </div>

        <button class="soundBtn"
                onclick="toggleMusic()"
                id="gameMusic">
            🔊
        </button>

        <div class="score" id="score">
            0
        </div>

        <button class="pauseBtn"
                onclick="pauseGame()">
            ☰
        </button>

    </div>

    <div class="road" id="road">

        <div class="roadMoving"></div>

        <div class="car player"
             id="player">
             🚗
        </div>

    </div>


    <div class="controls">

        <button class="ctrl"
                onclick="movePlayer('left')">
            ←
        </button>

        <button class="ctrl"
                onclick="movePlayer('up')">
            ↑
        </button>

        <button class="ctrl"
                onclick="movePlayer('down')">
            ↓
        </button>

        <button class="ctrl"
                onclick="movePlayer('right')">
            →
        </button>

    </div>

</div>


<!-- ================= PAUSE ================= -->

<div id="pauseScreen">

    <div class="pauseBox">

        <h2>⏸️ TẠM DỪNG</h2>

        <button onclick="resumeGame()">
            ▶️ TIẾP TỤC
        </button>

        <button onclick="backMenu()">
            🏠 VỀ MENU
        </button>

    </div>

</div>


<!-- ================= GAME OVER ================= -->

<div id="gameOver">

    <div class="gameOverText">
        GAME OVER
    </div>

    <div style="margin-top:15px">
        Điểm: <span id="finalScore">0</span>
    </div>

    <button onclick="backMenu()">
        🏠 VỀ MENU
    </button>

</div>


<!-- ÂM THANH -->

<audio id="bgMusic" loop preload="auto">
    <source
        src="https://cdn.jsdelivr.net/gh/honghoasamsunglt2-tech/ngon-lua-ruc-chay@main/Nh%E1%BA%A1c%20game.mp3"
        type="audio/mpeg">
</audio>

<audio id="endMusic" preload="auto">
    <source
        src="https://cdn.jsdelivr.net/gh/honghoasamsunglt2-tech/ngon-lua-ruc-chay@main/Nh%E1%BA%A1c%20game%20k%E1%BA%BFt%20th%C3%BAc.mp3"
        type="audio/mpeg">
</audio>


<script>

const play = document.getElementById("play");
const menu = document.getElementById("menu");
const road = document.getElementById("road");
const player = document.getElementById("player");

const heartsText = document.getElementById("hearts");
const scoreText = document.getElementById("score");

const bgMusic = document.getElementById("bgMusic");
const endMusic = document.getElementById("endMusic");

let difficulty = "easy";
let selectedCar = "🚗";

let musicOn = true;
let playing = false;
let paused = false;

let hearts = 3;
let score = 0;

let playerX = 50;
let playerY = 82;

let obstacles = [];
let spawnTimer = null;
let gameTimer = null;

let speed = 3;


/* ================= CHỌN CẤP ĐỘ ================= */

function selectDifficulty(level,button){

    difficulty = level;

    document.querySelectorAll(".row .choice")
    .forEach(b=>{
        if(
            b.innerText.includes("DỄ") ||
            b.innerText.includes("VỪA") ||
            b.innerText.includes("KHÓ")
        ){
            b.classList.remove("selected");
        }
    });

    button.classList.add("selected");
}


/* ================= CHỌN XE ================= */

function selectCar(car,button){

    selectedCar = car;

    document.querySelectorAll(".row .choice")
    .forEach(b=>{
        if(
            b.innerText.includes("ĐỎ") ||
            b.innerText.includes("VÀNG")
        ){
            b.classList.remove("selected");
        }
    });

    button.classList.add("selected");
}


/* ================= ÂM NHẠC ================= */

function toggleMusic(){

    musicOn = !musicOn;

    const menuButton =
        document.getElementById("menuMusic");

    const gameButton =
        document.getElementById("gameMusic");

    if(musicOn){

        menuButton.innerText = "🔊 BẬT";
        gameButton.innerText = "🔊";

        if(playing){
            bgMusic.play().catch(()=>{});
        }

    }else{

        menuButton.innerText = "🔇 TẮT";
        gameButton.innerText = "🔇";

        bgMusic.pause();
    }
}


/* ================= BẮT ĐẦU ================= */

function startGame(){

    menu.style.display = "none";
    play.style.display = "block";

    document.getElementById("gameOver").style.display = "none";

    hearts = 3;
    score = 0;

    heartsText.innerText = "3❤️";
    scoreText.innerText = "0";

    playerX = 50;
    playerY = 82;

    player.style.left = playerX + "%";
    player.style.top = playerY + "%";

    player.innerText = selectedCar;

    obstacles.forEach(o=>o.remove());
    obstacles = [];

    playing = true;
    paused = false;

    if(difficulty === "easy"){
        speed = 3;
    }

    if(difficulty === "medium"){
        speed = 5;
    }

    if(difficulty === "hard"){
        speed = 10;
    }

    if(musicOn){
        bgMusic.currentTime = 0;
        bgMusic.play().catch(()=>{});
    }

    clearInterval(spawnTimer);
    clearInterval(gameTimer);

    /* Xe xuất hiện nhiều */

    spawnTimer = setInterval(
        spawnObstacle,
        difficulty === "hard" ? 430 : 600
    );

    gameTimer = setInterval(gameLoop,30);

    /* tạo sẵn nhiều xe */

    for(let i=0;i<5;i++){
        setTimeout(spawnObstacle,i*250);
    }
}


/* ================= TẠO CHƯỚNG NGẠI ================= */

function spawnObstacle(){

    if(!playing || paused)return;

    const item =
        Math.random() < 0.72
        ? ["🛻","🚛","🚚"][Math.floor(Math.random()*3)]
        : "🚧";

    const obj = document.createElement("div");

    obj.className = "car obstacle";

    obj.innerText = item;

    let lane =
        Math.floor(Math.random()*3);

    let x =
        16.7 + lane*33.3;

    obj.style.left = x + "%";
    obj.style.top = "-8%";

    road.appendChild(obj);

    obstacles.push(obj);
}


/* ================= Ổ GÀ ================= */

function createPothole(){

    const hole = document.createElement("div");

    hole.className = "car obstacle";

    hole.innerText = "🕳️";

    let lane =
        Math.floor(Math.random()*3);

    let x =
        16.7 + lane*33.3;

    hole.style.left = x + "%";
    hole.style.top = "-8%";

    road.appendChild(hole);

    obstacles.push(hole);
}


/* ================= GAME LOOP ================= */

function gameLoop(){

    if(!playing || paused)return;

    obstacles.forEach((obj,index)=>{

        let top =
            parseFloat(obj.style.top);

        top += speed * 0.7;

        obj.style.top = top + "%";

        if(top > 108){

            obj.remove();

            obstacles.splice(index,1);

            score++;

            scoreText.innerText = score;
        }

        checkCollision(obj);
    });

    /* ổ gà xuất hiện khá nhiều */

    if(Math.random() < 0.035){
        createPothole();
    }
}


/* ================= VA CHẠM ================= */

function checkCollision(obj){

    const a = player.getBoundingClientRect();
    const b = obj.getBoundingClientRect();

    const hit =
        a.left < b.right &&
        a.right > b.left &&
        a.top < b.bottom &&
        a.bottom > b.top;

    if(!hit)return;

    const type = obj.innerText;

    obj.remove();

    if(type === "🕳️"){

        gameOver();

        return;
    }

    hearts--;

    if(hearts <= 0){

        gameOver();

    }else{

        heartsText.innerText =
            hearts + "❤️";
    }
}


/* ================= DI CHUYỂN BẰNG NÚT ================= */

/*
   Mỗi lần bấm = xe chạy một đoạn.
   Không cần giữ nút.
*/

function movePlayer(direction){

    if(!playing || paused)return;

    const step = 17;

    if(direction === "left"){
        playerX -= step;
    }

    if(direction === "right"){
        playerX += step;
    }

    if(direction === "up"){
        playerY -= step;
    }

    if(direction === "down"){
        playerY += step;
    }

    playerX =
        Math.max(8,Math.min(92,playerX));

    playerY =
        Math.max(8,Math.min(88,playerY));

    player.style.left = playerX + "%";
    player.style.top = playerY + "%";
}


/* ================= KÉO XE TRỰC TIẾP ================= */

let dragging = false;

player.addEventListener("pointerdown",e=>{

    if(!playing || paused)return;

    dragging = true;

    player.setPointerCapture(e.pointerId);
});


player.addEventListener("pointermove",e=>{

    if(!dragging)return;

    const rect =
        road.getBoundingClientRect();

    playerX =
        ((e.clientX-rect.left)/rect.width)*100;

    playerY =
        ((e.clientY-rect.top)/rect.height)*100;

    playerX =
        Math.max(8,Math.min(92,playerX));

    playerY =
        Math.max(8,Math.min(88,playerY));

    player.style.left = playerX+"%";
    player.style.top = playerY+"%";
});


player.addEventListener("pointerup",()=>{
    dragging=false;
});


/* ================= PAUSE ================= */

function pauseGame(){

    if(!playing)return;

    paused = true;

    document.getElementById("pauseScreen")
        .style.display = "flex";

    bgMusic.pause();
}


function resumeGame(){

    paused = false;

    document.getElementById("pauseScreen")
        .style.display = "none";

    if(musicOn){
        bgMusic.play().catch(()=>{});
    }
}


/* ================= GAME OVER ================= */

function gameOver(){

    playing = false;

    clearInterval(spawnTimer);
    clearInterval(gameTimer);

    bgMusic.pause();

    if(musicOn){

        endMusic.currentTime = 0;

        endMusic.play().catch(()=>{});
    }

    document.getElementById("finalScore")
        .innerText = score;

    document.getElementById("gameOver")
        .style.display = "flex";

    let oldRecord =
        Number(localStorage.getItem("ngonLuaRecord") || 0);

    if(score > oldRecord){

        localStorage.setItem(
            "ngonLuaRecord",
            score
        );
    }
}


/* ================= VỀ MENU ================= */

function backMenu(){

    playing = false;
    paused = false;

    clearInterval(spawnTimer);
    clearInterval(gameTimer);

    bgMusic.pause();
    endMusic.pause();

    obstacles.forEach(o=>o.remove());
    obstacles = [];

    document.getElementById("pauseScreen")
        .style.display = "none";

    document.getElementById("gameOver")
        .style.display = "none";

    play.style.display = "none";
    menu.style.display = "flex";

    document.getElementById("menuRecord")
        .innerText =
        localStorage.getItem("ngonLuaRecord") || 0;
}


/* ================= RECORD ================= */

document.getElementById("menuRecord")
    .innerText =
    localStorage.getItem("ngonLuaRecord") || 0;


/* ================= PHÍM BÀN PHÍM ================= */

document.addEventListener("keydown",e=>{

    if(!playing || paused)return;

    if(e.key === "ArrowLeft")
        movePlayer("left");

    if(e.key === "ArrowRight")
        movePlayer("right");

    if(e.key === "ArrowUp")
        movePlayer("up");

    if(e.key === "ArrowDown")
        movePlayer("down");
});

</script>

</div>

</body>
</html>
"""

components.html(
    game,
    height=760,
    scrolling=False
)
