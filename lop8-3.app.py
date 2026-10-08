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
    touch-action:none;
}

body{
    margin:0;
    background:#050505;
    color:white;
    font-family:Arial,sans-serif;
    overflow:hidden;
}

#game{
    width:100%;
    max-width:460px;
    height:790px;
    margin:auto;
    background:#090909;
    position:relative;
    overflow:hidden;
}

/* ================= MENU ================= */

#menu{
    position:absolute;
    inset:0;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    background:
        radial-gradient(circle at center,#3b0000 0%,#100000 40%,#050505 75%);
    z-index:20;
}

.title{
    font-size:clamp(38px,10vw,58px);
    font-weight:900;
    font-style:italic;
    text-align:center;
    color:#ff2020;
    text-shadow:
        0 0 5px #ff0000,
        0 0 15px #ff0000,
        0 0 30px #ff3b00;
    animation:heartbeat 1.15s infinite;
    line-height:1.05;
}

@keyframes heartbeat{
    0%,100%{transform:scale(1);}
    15%{transform:scale(1.08);}
    30%{transform:scale(1);}
    45%{transform:scale(1.06);}
    60%{transform:scale(1);}
}

.subtitle{
    margin-top:14px;
    font-size:17px;
    letter-spacing:2px;
    color:#ffb0b0;
}

.menuBox{
    width:88%;
    max-width:350px;
    margin-top:25px;
}

.menuBtn{
    width:100%;
    margin:7px 0;
    padding:14px;
    border:2px solid #ff3333;
    border-radius:14px;
    background:#180707;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.menuBtn:active{
    transform:scale(.97);
    background:#450909;
}

.section{
    text-align:center;
    color:#ff6b6b;
    font-weight:bold;
    margin-top:9px;
}

.selected{
    background:#8d1010 !important;
    box-shadow:0 0 15px #ff2020;
}

#record{
    text-align:center;
    margin-top:10px;
    font-size:17px;
    color:#ffd1d1;
}

/* ================= GAME ================= */

#gameScreen{
    position:absolute;
    inset:0;
    display:none;
    background:#080808;
}

#topbar{
    height:92px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:12px 16px;
    background:#090909;
    position:relative;
    z-index:10;
}

#hearts{
    color:#ff1616;
    font-size:27px;
    font-weight:900;
    min-width:80px;
}

#score{
    font-size:30px;
    font-weight:900;
}

#musicBtn{
    width:58px;
    height:58px;
    border:0;
    border-radius:15px;
    background:#202020;
    color:white;
    font-size:27px;
}

#pauseBtn{
    width:58px;
    height:58px;
    border:0;
    border-radius:15px;
    background:#202020;
    color:white;
    font-size:34px;
    line-height:1;
}

/* ================= ROAD ================= */

#road{
    position:absolute;
    top:92px;
    left:7%;
    width:86%;
    height:535px;
    background:#303030;
    border-left:9px solid #555;
    border-right:9px solid #555;
    overflow:hidden;
}

.laneLine{
    position:absolute;
    top:0;
    bottom:0;
    width:6px;
    background:repeating-linear-gradient(
        to bottom,
        #eeeeee 0px,
        #eeeeee 55px,
        transparent 55px,
        transparent 100px
    );
    opacity:.9;
}

.line1{
    left:33.33%;
}

.line2{
    left:66.66%;
}

/* ================= PLAYER ================= */

#player{
    position:absolute;
    width:62px;
    height:72px;
    font-size:58px;
    display:flex;
    align-items:center;
    justify-content:center;
    z-index:5;
    transition:none;
}

/* ================= OBSTACLES ================= */

.obstacle{
    position:absolute;
    width:65px;
    height:70px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:53px;
    z-index:4;
}

.pothole{
    font-size:48px;
}

/* ================= CONTROLS ================= */

#controls{
    position:absolute;
    left:9%;
    right:9%;
    bottom:18px;
    height:125px;
    border:4px solid #ff2638;
    border-radius:15px;
    background:rgba(0,0,0,.88);
    display:grid;
    grid-template-columns:1fr 1fr 1fr;
    grid-template-rows:1fr 1fr;
    gap:7px;
    padding:8px;
    z-index:15;
}

.control{
    border:0;
    border-radius:12px;
    background:#242424;
    color:white;
    font-size:30px;
    font-weight:bold;
}

.control:active,
.control.active{
    background:#850e16;
    transform:scale(.96);
}

.up{
    grid-column:2;
    grid-row:1;
}

.left{
    grid-column:1;
    grid-row:2;
}

.down{
    grid-column:2;
    grid-row:2;
}

.right{
    grid-column:3;
    grid-row:2;
}

/* ================= PAUSE ================= */

.overlay{
    position:absolute;
    inset:0;
    background:rgba(0,0,0,.82);
    display:none;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    z-index:30;
}

.overlay h2{
    font-size:42px;
    color:#ff2727;
    margin:10px;
}

.overlay button{
    width:220px;
    margin:7px;
    padding:14px;
    border-radius:12px;
    border:2px solid #ff3333;
    background:#180707;
    color:white;
    font-size:18px;
    font-weight:bold;
}

/* ================= GAME OVER ================= */

#gameOver{
    display:none;
}

.gameOverText{
    font-size:clamp(42px,11vw,65px);
    font-weight:900;
    color:#ff1111;
    text-shadow:
        0 0 5px red,
        0 0 15px red,
        0 0 30px #ff0000;
    animation:earthquake .55s infinite;
}

@keyframes earthquake{
    0%{transform:translateY(-450px) translateX(0);}
    45%{transform:translateY(0) translateX(-4px);}
    55%{transform:translateY(0) translateX(5px);}
    65%{transform:translateY(0) translateX(-4px);}
    75%{transform:translateY(0) translateX(4px);}
    100%{transform:translateY(0) translateX(0);}
}

.finalScore{
    font-size:21px;
    margin:20px;
}

.overBtn{
    width:230px !important;
    padding:15px !important;
    margin:7px !important;
    border:2px solid #ff3333 !important;
    border-radius:12px !important;
    background:#180707 !important;
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
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
        🏎️ FIRE ROAD RACING 🏎️
    </div>

    <div class="menuBox">

        <button class="menuBtn" onclick="toggleMenuMusic()">
            🔊 ÂM THANH: <span id="menuMusicText">BẬT</span>
        </button>

        <div class="section">⚡ CHỌN ĐỘ KHÓ ⚡</div>

        <button class="menuBtn difficulty selected"
                data-speed="5"
                onclick="selectDifficulty(this)">
            DỄ
        </button>

        <button class="menuBtn difficulty"
                data-speed="7"
                onclick="selectDifficulty(this)">
            VỪA
        </button>

        <button class="menuBtn difficulty"
                data-speed="11"
                onclick="selectDifficulty(this)">
            KHÓ
        </button>

        <div class="section">🚗 CHỌN XE 🚗</div>

        <button class="menuBtn car selected"
                data-car="🚗"
                onclick="selectCar(this)">
            🚗 XE ĐỎ
        </button>

        <button class="menuBtn car"
                data-car="🚕"
                onclick="selectCar(this)">
            🚕 XE VÀNG
        </button>

        <button class="menuBtn"
                onclick="startGame()">
            🔥 BẮT ĐẦU
        </button>

        <div id="record">
            🏆 KỶ LỤC: 0
        </div>

    </div>
</div>


<!-- ================= GAME ================= -->

<div id="gameScreen">

    <div id="topbar">

        <div id="hearts">
            3❤️
        </div>

        <button id="musicBtn" onclick="toggleGameMusic()">
            🔊
        </button>

        <div id="score">
            0
        </div>

        <button id="pauseBtn" onclick="pauseGame()">
            ☰
        </button>

    </div>

    <div id="road">

        <div class="laneLine line1"></div>
        <div class="laneLine line2"></div>

        <div id="player">🚗</div>

    </div>


    <!-- NÚT DI CHUYỂN -->

    <div id="controls">

        <button class="control up"
                data-dir="up">
            ▲
        </button>

        <button class="control left"
                data-dir="left">
            ◀
        </button>

        <button class="control down"
                data-dir="down">
            ▼
        </button>

        <button class="control right"
                data-dir="right">
            ▶
        </button>

    </div>


    <!-- PAUSE -->

    <div id="pauseScreen" class="overlay">

        <h2>⏸️ TẠM DỪNG</h2>

        <button onclick="resumeGame()">
            ▶️ TIẾP TỤC
        </button>

        <button onclick="backToMenu()">
            🏠 VỀ MENU
        </button>

    </div>


    <!-- GAME OVER -->

    <div id="gameOver" class="overlay">

        <div class="gameOverText">
            GAME OVER
        </div>

        <div class="finalScore">
            Điểm: <span id="finalScore">0</span>
        </div>

        <button class="overBtn"
                onclick="backToMenu()">
            🏠 VỀ MENU CHÍNH
        </button>

        <button class="overBtn"
                onclick="restartGame()">
            🔄 CHƠI LẠI
        </button>

    </div>

</div>


<!-- ================= ÂM THANH ================= -->

<audio id="bgMusic" loop preload="auto">
    <source
        src="https://raw.githubusercontent.com/honghoasamsunglt2-tech/ngon-lua-ruc-chay/main/Nh%E1%BA%A1c%20game.mp3"
        type="audio/mpeg">
</audio>

<audio id="endMusic" preload="auto">
    <source
        src="https://raw.githubusercontent.com/honghoasamsunglt2-tech/ngon-lua-ruc-chay/main/Nh%E1%BA%A1c%20game%20k%E1%BA%BFt%20th%C3%BAc.mp3"
        type="audio/mpeg">
</audio>


<script>

const menu = document.getElementById("menu");
const gameScreen = document.getElementById("gameScreen");
const road = document.getElementById("road");
const player = document.getElementById("player");

const heartsText = document.getElementById("hearts");
const scoreText = document.getElementById("score");
const recordText = document.getElementById("record");

const pauseScreen = document.getElementById("pauseScreen");
const gameOverScreen = document.getElementById("gameOver");

const bgMusic = document.getElementById("bgMusic");
const endMusic = document.getElementById("endMusic");

let difficultySpeed = 5;
let selectedCar = "🚗";

let musicOn = true;
let playing = false;
let paused = false;

let score = 0;
let hearts = 3;

let playerX = 0;
let playerY = 0;

let obstacles = [];
let lastSpawn = 0;
let animationId = 0;

let keys = {
    up:false,
    down:false,
    left:false,
    right:false
};


/* ================= CHỌN ĐỘ KHÓ ================= */

function selectDifficulty(button){

    document.querySelectorAll(".difficulty")
        .forEach(x => x.classList.remove("selected"));

    button.classList.add("selected");

    difficultySpeed =
        Number(button.dataset.speed);
}


/* ================= CHỌN XE ================= */

function selectCar(button){

    document.querySelectorAll(".car")
        .forEach(x => x.classList.remove("selected"));

    button.classList.add("selected");

    selectedCar = button.dataset.car;
}


/* ================= NHẠC MENU ================= */

function toggleMenuMusic(){

    musicOn = !musicOn;

    document.getElementById("menuMusicText")
        .textContent = musicOn ? "BẬT" : "TẮT";
}


/* ================= NHẠC TRONG GAME ================= */

function toggleGameMusic(){

    musicOn = !musicOn;

    if(musicOn){

        bgMusic.play().catch(()=>{});

        document.getElementById("musicBtn")
            .textContent = "🔊";

    }else{

        bgMusic.pause();

        document.getElementById("musicBtn")
            .textContent = "🔇";
    }
}


/* ================= BẮT ĐẦU ================= */

function startGame(){

    menu.style.display = "none";
    gameScreen.style.display = "block";

    score = 0;
    hearts = 3;

    scoreText.textContent = "0";
    heartsText.textContent = "3❤️";

    player.innerHTML = selectedCar;

    playing = true;
    paused = false;

    obstacles.forEach(o => o.remove());
    obstacles = [];

    playerX =
        road.clientWidth / 2 - player.offsetWidth / 2;

    playerY =
        road.clientHeight - 100;

    player.style.left = playerX + "px";
    player.style.top = playerY + "px";

    if(musicOn){

        bgMusic.currentTime = 0;
        bgMusic.play().catch(()=>{});
    }

    requestAnimationFrame(gameLoop);
}


/* ================= DI CHUYỂN ================= */

function updatePlayer(){

    const moveSpeed = 8;

    if(keys.left)
        playerX -= moveSpeed;

    if(keys.right)
        playerX += moveSpeed;

    if(keys.up)
        playerY -= moveSpeed;

    if(keys.down)
        playerY += moveSpeed;


    /* Không cho xe chạy ra ngoài đường */

    playerX = Math.max(
        0,
        Math.min(
            road.clientWidth - player.offsetWidth,
            playerX
        )
    );

    playerY = Math.max(
        0,
        Math.min(
            road.clientHeight - player.offsetHeight,
            playerY
        )
    );


    player.style.left = playerX + "px";
    player.style.top = playerY + "px";
}


/* ================= NÚT GIỮ LIÊN TỤC ================= */

document.querySelectorAll(".control")
.forEach(button => {

    const dir = button.dataset.dir;

    function startMove(e){

        e.preventDefault();

        keys[dir] = true;
        button.classList.add("active");
    }

    function stopMove(e){

        e.preventDefault();

        keys[dir] = false;
        button.classList.remove("active");
    }

    button.addEventListener("touchstart",
        startMove,
        {passive:false});

    button.addEventListener("touchend",
        stopMove,
        {passive:false});

    button.addEventListener("touchcancel",
        stopMove,
        {passive:false});

    button.addEventListener("mousedown",
        startMove);

    button.addEventListener("mouseup",
        stopMove);

    button.addEventListener("mouseleave",
        stopMove);
});


/* ================= BÀN PHÍM ================= */

document.addEventListener("keydown", e => {

    if(e.key === "ArrowLeft")
        keys.left = true;

    if(e.key === "ArrowRight")
        keys.right = true;

    if(e.key === "ArrowUp")
        keys.up = true;

    if(e.key === "ArrowDown")
        keys.down = true;
});

document.addEventListener("keyup", e => {

    if(e.key === "ArrowLeft")
        keys.left = false;

    if(e.key === "ArrowRight")
        keys.right = false;

    if(e.key === "ArrowUp")
        keys.up = false;

    if(e.key === "ArrowDown")
        keys.down = false;
});


/* ================= TẠO CHƯỚNG NGẠI ================= */

function spawnObstacle(){

    const obstacle = document.createElement("div");

    obstacle.className = "obstacle";

    const things = [
        "🛻",
        "🚛",
        "🚚",
        "🚧",
        "🕳️"
    ];

    const thing =
        things[Math.floor(Math.random() * things.length)];

    obstacle.textContent = thing;

    const maxX =
        road.clientWidth - 70;

    obstacle.x =
        Math.random() * maxX;

    obstacle.y = -80;

    obstacle.style.left =
        obstacle.x + "px";

    obstacle.style.top =
        obstacle.y + "px";

    if(thing === "🕳️"){
        obstacle.classList.add("pothole");
    }

    road.appendChild(obstacle);

    obstacles.push(obstacle);
}


/* ================= VA CHẠM ================= */

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


/* ================= GAME LOOP ================= */

function gameLoop(time){

    if(!playing)
        return;

    if(paused){

        animationId =
            requestAnimationFrame(gameLoop);

        return;
    }

    updatePlayer();


    /* Sinh xe nhiều vừa đủ */

    if(time - lastSpawn > 650){

        spawnObstacle();

        lastSpawn = time;
    }


    for(let i = obstacles.length - 1; i >= 0; i--){

        const o = obstacles[i];

        o.y += difficultySpeed;

        o.style.top =
            o.y + "px";


        /* Va chạm */

        if(collision(player,o)){

            const isPothole =
                o.textContent === "🕳️";

            o.remove();

            obstacles.splice(i,1);


            /* Ổ gà = thua ngay */

            if(isPothole){

                gameOver();
                return;
            }


            /* Đụng xe / rào = mất tim */

            hearts--;

            heartsText.textContent =
                hearts + "❤️";


            if(hearts <= 0){

                gameOver();
                return;
            }

            continue;
        }


        /* Xe đi qua màn hình */

        if(o.y > road.clientHeight){

            o.remove();

            obstacles.splice(i,1);

            score++;

            scoreText.textContent =
                score;
        }
    }


    animationId =
        requestAnimationFrame(gameLoop);
}


/* ================= GAME OVER ================= */

function gameOver(){

    playing = false;

    cancelAnimationFrame(animationId);

    bgMusic.pause();

    if(musicOn){

        endMusic.currentTime = 0;

        endMusic.play().catch(()=>{});
    }


    document.getElementById("finalScore")
        .textContent = score;

    gameOverScreen.style.display =
        "flex";


    let oldRecord =
        Number(localStorage.getItem("ngonLuaRecord") || 0);

    if(score > oldRecord){

        localStorage.setItem(
            "ngonLuaRecord",
            score
        );
    }

    updateRecord();
}


/* ================= CHƠI LẠI ================= */

function restartGame(){

    endMusic.pause();
    endMusic.currentTime = 0;

    gameOverScreen.style.display =
        "none";

    startGame();
}


/* ================= TẠM DỪNG ================= */

function pauseGame(){

    if(!playing)
        return;

    paused = true;

    bgMusic.pause();

    pauseScreen.style.display =
        "flex";
}


function resumeGame(){

    paused = false;

    pauseScreen.style.display =
        "none";

    if(musicOn){

        bgMusic.play().catch(()=>{});
    }
}


/* ================= VỀ MENU ================= */

function backToMenu(){

    playing = false;
    paused = false;

    cancelAnimationFrame(animationId);

    bgMusic.pause();
    endMusic.pause();

    obstacles.forEach(o => o.remove());

    obstacles = [];

    gameOverScreen.style.display =
        "none";

    pauseScreen.style.display =
        "none";

    gameScreen.style.display =
        "none";

    menu.style.display =
        "flex";

    updateRecord();
}


/* ================= KỶ LỤC ================= */

function updateRecord(){

    const record =
        Number(
            localStorage.getItem(
                "ngonLuaRecord"
            ) || 0
        );

    recordText.textContent =
        "🏆 KỶ LỤC: " + record;
}

updateRecord();

</script>

</body>
</html>
"""

components.html(
    game,
    height=800,
    scrolling=False
)
