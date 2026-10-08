import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ngọn lửa rực cháy",
    page_icon="🔥",
    layout="centered"
)

game = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
*{
    box-sizing:border-box;
    user-select:none;
    -webkit-user-select:none;
}

body{
    margin:0;
    background:#080808;
    color:white;
    font-family:Arial,sans-serif;
    overflow:hidden;
}

#app{
    width:100%;
    max-width:430px;
    margin:auto;
}

/* ================= MENU ================= */

#menu{
    min-height:760px;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    padding:20px;
    background:
        radial-gradient(circle at center,#3a0505 0%,#100000 45%,#050505 100%);
}

.title{
    font-size:43px;
    font-weight:900;
    font-style:italic;
    text-align:center;
    color:#ff3030;
    text-shadow:
        0 0 8px #ff0000,
        0 0 20px #ff4500,
        0 0 35px #ff0000;
    animation:heartBeat 1.15s infinite;
    margin-bottom:10px;
}

@keyframes heartBeat{
    0%{transform:scale(1)}
    15%{transform:scale(1.08)}
    30%{transform:scale(1)}
    45%{transform:scale(1.05)}
    60%{transform:scale(1)}
    100%{transform:scale(1)}
}

.subtitle{
    font-size:17px;
    letter-spacing:3px;
    color:#ffb0b0;
    margin-bottom:25px;
}

.box{
    width:90%;
    max-width:330px;
    background:#171717;
    border:2px solid #ff3030;
    border-radius:18px;
    padding:14px;
    margin:7px;
    text-align:center;
    box-shadow:0 0 15px #ff000055;
}

.box-title{
    font-size:18px;
    margin-bottom:10px;
    font-weight:bold;
}

button{
    border:none;
    cursor:pointer;
    -webkit-tap-highlight-color:transparent;
}

.diff{
    display:flex;
    gap:8px;
    justify-content:center;
}

.diff button,
.car-btn{
    background:#292929;
    color:white;
    border:2px solid #555;
    border-radius:12px;
    padding:11px 13px;
    font-size:16px;
}

.diff button.active,
.car-btn.active{
    background:#b80000;
    border-color:#ff4444;
    box-shadow:0 0 12px #ff0000;
}

.car-list{
    display:flex;
    justify-content:center;
    gap:20px;
}

.car-btn{
    font-size:30px;
    width:90px;
}

.music-btn{
    background:#292929;
    color:white;
    border:2px solid #777;
    border-radius:12px;
    padding:10px 25px;
    font-size:17px;
}

.start-btn{
    width:90%;
    max-width:330px;
    padding:17px;
    margin-top:15px;
    border-radius:17px;
    background:linear-gradient(135deg,#ff1616,#7a0000);
    color:white;
    font-size:23px;
    font-weight:bold;
    box-shadow:0 0 20px #ff000088;
}

.record{
    margin-top:16px;
    font-size:17px;
    color:#ffd36b;
}

/* ================= GAME ================= */

#game{
    display:none;
    position:relative;
    width:100%;
    height:760px;
    background:#111;
    overflow:hidden;
}

#topbar{
    position:absolute;
    top:8px;
    left:8px;
    right:8px;
    height:50px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    z-index:20;
}

#hearts{
    font-size:20px;
    font-weight:bold;
}

#gameMusic{
    background:#202020;
    color:white;
    border:1px solid #777;
    border-radius:10px;
    padding:8px 10px;
    font-size:14px;
}

#menuBtn{
    width:44px;
    height:40px;
    border-radius:10px;
    background:#202020;
    color:white;
    font-size:24px;
    border:1px solid #777;
}

#road{
    position:absolute;
    top:66px;
    left:8%;
    width:84%;
    height:500px;
    background:#303030;
    border-left:8px solid #777;
    border-right:8px solid #777;
    overflow:hidden;
}

.lane-line{
    position:absolute;
    top:0;
    bottom:0;
    width:4px;
    background:repeating-linear-gradient(
        to bottom,
        #eee 0px,
        #eee 35px,
        transparent 35px,
        transparent 70px
    );
    opacity:.7;
}

.line1{left:33.33%}
.line2{left:66.66%}

#player{
    position:absolute;
    width:55px;
    height:78px;
    bottom:30px;
    left:calc(50% - 27px);
    font-size:50px;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:10;
    filter:drop-shadow(0 4px 5px #000);
}

.obstacle{
    position:absolute;
    width:55px;
    height:65px;
    font-size:45px;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:8;
}

.pothole{
    position:absolute;
    width:55px;
    height:30px;
    border-radius:50%;
    background:#090909;
    box-shadow:inset 0 0 10px #000;
    z-index:5;
}

#score{
    position:absolute;
    top:75px;
    left:50%;
    transform:translateX(-50%);
    font-size:20px;
    font-weight:bold;
    z-index:20;
    background:#0009;
    padding:5px 14px;
    border-radius:12px;
}

/* ================= CONTROLS ================= */

#controls{
    position:absolute;
    left:0;
    right:0;
    bottom:20px;
    height:150px;
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    align-items:center;
    padding:0 15px;
    z-index:30;
}

.ctrl{
    width:65px;
    height:65px;
    border-radius:50%;
    background:#222;
    border:2px solid #888;
    color:white;
    font-size:30px;
    box-shadow:0 4px 10px #000;
}

.left{
    justify-self:start;
}

.right{
    justify-self:end;
}

.middle{
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:8px;
}

.small{
    width:55px;
    height:45px;
    font-size:24px;
}

/* ================= PAUSE ================= */

#pauseScreen{
    display:none;
    position:absolute;
    inset:0;
    background:#000b;
    z-index:100;
    align-items:center;
    justify-content:center;
    flex-direction:column;
}

.pause-box{
    background:#191919;
    border:2px solid #ff3030;
    padding:25px;
    border-radius:20px;
    text-align:center;
}

.pause-box button{
    display:block;
    width:220px;
    padding:13px;
    margin:10px;
    border-radius:12px;
    background:#8d0000;
    color:white;
    font-size:17px;
}

/* ================= GAME OVER ================= */

#gameOver{
    display:none;
    position:absolute;
    inset:0;
    z-index:200;
    background:#000b;
    align-items:center;
    justify-content:center;
    flex-direction:column;
}

.game-over-text{
    font-size:55px;
    font-weight:900;
    color:#ff2222;
    text-shadow:
        0 0 8px red,
        0 0 20px red;
    animation:fall 1s ease-out,shake .15s 7;
}

@keyframes fall{
    0%{
        transform:translateY(-500px) rotate(-10deg);
        opacity:0;
    }
    70%{
        transform:translateY(25px) rotate(5deg);
    }
    100%{
        transform:translateY(0) rotate(0);
        opacity:1;
    }
}

@keyframes shake{
    0%{transform:translateX(-8px)}
    50%{transform:translateX(8px)}
    100%{transform:translateX(-8px)}
}

.over-score{
    font-size:20px;
    margin:15px;
}

.restart{
    padding:14px 35px;
    border-radius:14px;
    background:#b00000;
    color:white;
    font-size:19px;
}

</style>
</head>

<body>

<div id="app">

<!-- ================= MENU ================= -->

<div id="menu">

    <div class="title">
        🔥 NGỌN LỬA RỰC CHÁY 🔥
    </div>

    <div class="subtitle">
        FIRE ROAD RACING
    </div>

    <div class="box">

        <div class="box-title">🎵 ÂM NHẠC</div>

        <button
            id="menuMusic"
            class="music-btn"
            onclick="toggleMusic()">
            🔊 BẬT
        </button>

    </div>

    <div class="box">

        <div class="box-title">⚡ CHỌN CẤP ĐỘ</div>

        <div class="diff">

            <button
                id="easy"
                class="active"
                onclick="setDifficulty('easy')">
                DỄ
            </button>

            <button
                id="medium"
                onclick="setDifficulty('medium')">
                VỪA
            </button>

            <button
                id="hard"
                onclick="setDifficulty('hard')">
                KHÓ
            </button>

        </div>

    </div>

    <div class="box">

        <div class="box-title">🚗 CHỌN XE</div>

        <div class="car-list">

            <button
                id="redCar"
                class="car-btn active"
                onclick="setCar('🚗')">
                🚗
            </button>

            <button
                id="yellowCar"
                class="car-btn"
                onclick="setCar('🚕')">
                🚕
            </button>

        </div>

    </div>

    <button
        class="start-btn"
        onclick="startGame()">
        🔥 BẮT ĐẦU
    </button>

    <div class="record">
        🏆 KỶ LỤC: <span id="menuRecord">0</span>
    </div>

</div>


<!-- ================= GAME ================= -->

<div id="game">

    <div id="topbar">

        <div id="hearts">
            3❤️
        </div>

        <button
            id="gameMusic"
            onclick="toggleMusic()">
            🔊
        </button>

        <button
            id="menuBtn"
            onclick="pauseGame()">
            ☰
        </button>

    </div>

    <div id="score">
        0
    </div>

    <div id="road">

        <div class="lane-line line1"></div>
        <div class="lane-line line2"></div>

        <div id="player">🚗</div>

    </div>

    <!-- NÚT ĐIỀU KHIỂN -->

    <div id="controls">

        <button
            class="ctrl left"
            onpointerdown="moveLeft()">
            ⬅️
        </button>

        <div class="middle">

            <button
                class="ctrl small"
                onpointerdown="moveUp()">
                ⬆️
            </button>

            <button
                class="ctrl small"
                onpointerdown="moveDown()">
                ⬇️
            </button>

        </div>

        <button
            class="ctrl right"
            onpointerdown="moveRight()">
            ➡️
        </button>

    </div>


    <!-- PAUSE -->

    <div id="pauseScreen">

        <div class="pause-box">

            <h2>⏸ TẠM DỪNG</h2>

            <button onclick="continueGame()">
                ▶️ TIẾP TỤC
            </button>

            <button onclick="backToMenu()">
                🏠 VỀ MENU
            </button>

        </div>

    </div>


    <!-- GAME OVER -->

    <div id="gameOver">

        <div class="game-over-text">
            GAME OVER
        </div>

        <div class="over-score">
            Điểm: <span id="finalScore">0</span>
        </div>

        <button
            class="restart"
            onclick="restartGame()">
            🔄 CHƠI LẠI
        </button>

    </div>

</div>

<!-- ================= MUSIC ================= -->

<audio
    id="bgMusic"
    loop
    preload="auto">

    <source
        src="https://cdn.jsdelivr.net/gh/honghoasamsunglt2-tech/ngon-lua-ruc-chay@main/Nh%E1%BA%A1c%20game.mp3"
        type="audio/mpeg">

</audio>

<audio
    id="endMusic"
    preload="auto">

    <source
        src="https://cdn.jsdelivr.net/gh/honghoasamsunglt2-tech/ngon-lua-ruc-chay@main/Nh%E1%BA%A1c%20game%20k%E1%BA%BFt%20th%C3%BAc.mp3"
        type="audio/mpeg">

</audio>


<script>

const game = document.getElementById("game");
const menu = document.getElementById("menu");
const road = document.getElementById("road");
const player = document.getElementById("player");

const heartsText = document.getElementById("hearts");
const scoreText = document.getElementById("score");

const bgMusic = document.getElementById("bgMusic");
const endMusic = document.getElementById("endMusic");

let musicOn = true;
let difficulty = "easy";
let playerCar = "🚗";

let hearts = 3;
let score = 0;

let gameRunning = false;
let paused = false;

let speed = 4;
let spawnTime = 950;

let obstacles = [];
let lastSpawn = 0;
let lastTime = 0;

let px = 50;
let py = 82;


/* ================= DIFFICULTY ================= */

function setDifficulty(level){

    difficulty = level;

    document
        .querySelectorAll(".diff button")
        .forEach(b => b.classList.remove("active"));

    document
        .getElementById(level)
        .classList.add("active");

    if(level === "easy"){
        speed = 4;
        spawnTime = 1000;
    }

    if(level === "medium"){
        speed = 7;
        spawnTime = 700;
    }

    if(level === "hard"){
        speed = 13;
        spawnTime = 380;
    }
}


/* ================= CAR ================= */

function setCar(car){

    playerCar = car;

    player.textContent = car;

    document
        .querySelectorAll(".car-btn")
        .forEach(b => b.classList.remove("active"));

    if(car === "🚗"){
        document
            .getElementById("redCar")
            .classList.add("active");
    }else{
        document
            .getElementById("yellowCar")
            .classList.add("active");
    }
}


/* ================= MUSIC ================= */

function toggleMusic(){

    musicOn = !musicOn;

    if(musicOn){

        bgMusic.play().catch(()=>{});

        document.getElementById("menuMusic").textContent = "🔊 BẬT";
        document.getElementById("gameMusic").textContent = "🔊";

    }else{

        bgMusic.pause();

        document.getElementById("menuMusic").textContent = "🔇 TẮT";
        document.getElementById("gameMusic").textContent = "🔇";

    }
}


/* ================= START ================= */

function startGame(){

    menu.style.display = "none";
    game.style.display = "block";

    hearts = 3;
    score = 0;

    px = 50;
    py = 82;

    player.style.left = "calc(50% - 27px)";
    player.style.top = "390px";

    heartsText.textContent = "3❤️";
    scoreText.textContent = "0";

    obstacles.forEach(o => o.el.remove());
    obstacles = [];

    gameRunning = true;
    paused = false;

    lastSpawn = performance.now();
    lastTime = performance.now();

    if(musicOn){
        bgMusic.currentTime = 0;
        bgMusic.play().catch(()=>{});
    }

    requestAnimationFrame(loop);
}


/* ================= PLAYER MOVE ================= */

function moveLeft(){

    if(!gameRunning || paused) return;

    px -= 8;

    if(px < 5) px = 5;

    player.style.left =
        "calc(" + px + "% - 27px)";
}


function moveRight(){

    if(!gameRunning || paused) return;

    px += 8;

    if(px > 95) px = 95;

    player.style.left =
        "calc(" + px + "% - 27px)";
}


function moveUp(){

    if(!gameRunning || paused) return;

    py -= 8;

    if(py < 5) py = 5;

    player.style.top =
        (py * 4.3) + "px";
}


function moveDown(){

    if(!gameRunning || paused) return;

    py += 8;

    if(py > 82) py = 82;

    player.style.top =
        (py * 4.3) + "px";
}


/* ================= SPAWN ================= */

function spawnObstacle(){

    const el = document.createElement("div");

    el.className = "obstacle";

    const types = [
        "🛻",
        "🚛",
        "🚚",
        "🚧"
    ];

    el.textContent =
        types[Math.floor(Math.random()*types.length)];

    const lane =
        Math.floor(Math.random()*3);

    el.style.left =
        (lane * 33.33 + 5) + "%";

    el.style.top = "-70px";

    road.appendChild(el);

    obstacles.push({
        el:el,
        x:lane,
        y:-70,
        hit:false
    });


    /* Tăng mật độ xe */

    if(Math.random() < 0.45){

        const el2 = document.createElement("div");

        el2.className = "obstacle";

        el2.textContent =
            types[Math.floor(Math.random()*types.length)];

        let lane2 =
            Math.floor(Math.random()*3);

        while(lane2 === lane){
            lane2 =
                Math.floor(Math.random()*3);
        }

        el2.style.left =
            (lane2 * 33.33 + 5) + "%";

        el2.style.top = "-150px";

        road.appendChild(el2);

        obstacles.push({
            el:el2,
            x:lane2,
            y:-150,
            hit:false
        });
    }
}


/* ================= POTHOLE ================= */

function spawnPothole(){

    const hole = document.createElement("div");

    hole.className = "pothole";

    const lane =
        Math.floor(Math.random()*3);

    hole.style.left =
        (lane * 33.33 + 5) + "%";

    hole.style.top = "-40px";

    road.appendChild(hole);

    obstacles.push({
        el:hole,
        x:lane,
        y:-40,
        pothole:true,
        hit:false
    });
}


/* ================= COLLISION ================= */

function collision(a,b){

    const ar = a.getBoundingClientRect();
    const br = b.getBoundingClientRect();

    return !(
        ar.right < br.left ||
        ar.left > br.right ||
        ar.bottom < br.top ||
        ar.top > br.bottom
    );
}


/* ================= GAME LOOP ================= */

function loop(time){

    if(!gameRunning) return;

    if(paused){
        requestAnimationFrame(loop);
        return;
    }

    const dt =
        Math.min(time-lastTime,40);

    lastTime = time;

    if(time-lastSpawn > spawnTime){

        spawnObstacle();

        if(Math.random() < 0.35){
            spawnPothole();
        }

        lastSpawn = time;
    }


    obstacles.forEach(o => {

        o.y += speed * dt / 16;

        o.el.style.top =
            o.y + "px";


        if(!o.hit && collision(player,o.el)){

            o.hit = true;

            if(o.pothole){

                endGame();
                return;
            }


            /*
              TỈ LỆ VA CHẠM THUA CAO ~80%
            */

            if(Math.random() < 0.80){

                hearts--;

                heartsText.textContent =
                    hearts + "❤️";

                o.el.style.opacity = "0";

                if(hearts <= 0){
                    endGame();
                }

            }else{

                score++;

                scoreText.textContent =
                    score;

                o.el.style.opacity = ".35";
            }
        }


        if(o.y > 520){

            if(!o.hit && !o.pothole){

                score++;

                scoreText.textContent =
                    score;
            }

            o.el.remove();
        }

    });


    obstacles =
        obstacles.filter(o => o.y <= 520);

    requestAnimationFrame(loop);
}


/* ================= PAUSE ================= */

function pauseGame(){

    if(!gameRunning) return;

    paused = true;

    document
        .getElementById("pauseScreen")
        .style.display = "flex";

    bgMusic.pause();
}


function continueGame(){

    paused = false;

    document
        .getElementById("pauseScreen")
        .style.display = "none";

    if(musicOn){
        bgMusic.play().catch(()=>{});
    }

    lastTime = performance.now();
}


function backToMenu(){

    gameRunning = false;
    paused = false;

    bgMusic.pause();

    document
        .getElementById("pauseScreen")
        .style.display = "none";

    game.style.display = "none";
    menu.style.display = "flex";
}


/* ================= GAME OVER ================= */

function endGame(){

    if(!gameRunning) return;

    gameRunning = false;

    bgMusic.pause();

    if(musicOn){

        endMusic.currentTime = 0;

        endMusic.play().catch(()=>{});
    }

    document
        .getElementById("finalScore")
        .textContent = score;

    document
        .getElementById("gameOver")
        .style.display = "flex";


    let oldRecord =
        Number(localStorage.getItem("ngonLuaRecord") || 0);

    if(score > oldRecord){

        localStorage.setItem(
            "ngonLuaRecord",
            score
        );

        document
            .getElementById("menuRecord")
            .textContent = score;

    }
}


/* ================= RESTART ================= */

function restartGame(){

    endMusic.pause();

    document
        .getElementById("gameOver")
        .style.display = "none";

    startGame();
}


/* ================= RECORD ================= */

document
    .getElementById("menuRecord")
    .textContent =
    localStorage.getItem("ngonLuaRecord") || 0;

</script>

</div>

</body>
</html>
"""

components.html(
    game,
    height=800,
    scrolling=False
)
