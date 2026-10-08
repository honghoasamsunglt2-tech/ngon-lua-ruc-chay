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
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
*{
    box-sizing:border-box;
    user-select:none;
    -webkit-user-select:none;
}

html,body{
    margin:0;
    padding:0;
    background:#080808;
    overflow:hidden;
    font-family:Arial,sans-serif;
}

#game{
    width:min(100vw,520px);
    height:760px;
    margin:auto;
    position:relative;
    overflow:hidden;
    background:#080808;
    color:white;
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
        radial-gradient(circle,#351010 0%,#090909 70%);
}

.title{
    font-size:47px;
    font-weight:900;
    font-style:italic;
    text-align:center;
    color:#ff2020;
    text-shadow:
        0 0 5px red,
        0 0 15px #ff3300,
        0 0 30px red;
    animation:heartBeat 1.1s infinite;
}

@keyframes heartBeat{
    0%,100%{transform:scale(1)}
    15%{transform:scale(1.06)}
    30%{transform:scale(1)}
    45%{transform:scale(1.04)}
    60%{transform:scale(1)}
}

.subtitle{
    margin:12px 0 25px;
    color:#ffb0b0;
    font-size:17px;
    font-style:italic;
}

.menuBox{
    width:88%;
    max-width:390px;
    padding:20px;
    border-radius:20px;
    background:#171717;
    border:1px solid #ff2424;
    box-shadow:0 0 25px rgba(255,0,0,.3);
}

.label{
    text-align:center;
    font-weight:bold;
    margin:10px 0;
}

.row{
    display:flex;
    gap:9px;
    margin-bottom:12px;
}

.choice{
    flex:1;
    padding:12px 7px;
    border-radius:12px;
    background:#292929;
    color:white;
    border:1px solid #555;
    font-weight:bold;
    font-size:15px;
}

.choice.selected{
    background:#b91515;
    border-color:#ff3333;
    box-shadow:0 0 12px red;
}

.musicMenu{
    display:flex;
    align-items:center;
    justify-content:space-between;
    background:#101010;
    padding:9px;
    border-radius:12px;
}

.start{
    width:100%;
    margin-top:8px;
    padding:15px;
    border:0;
    border-radius:14px;
    background:#e01616;
    color:white;
    font-size:21px;
    font-weight:bold;
}

.record{
    text-align:center;
    margin-top:14px;
    padding:10px;
    border-radius:12px;
    background:#101010;
    color:#ffd85c;
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
    padding:0 14px;
    position:relative;
    z-index:20;
}

.hearts{
    font-size:25px;
    font-weight:bold;
    color:#ff2020;
    min-width:70px;
}

.score{
    font-size:28px;
    font-weight:bold;
}

.soundBtn,
.pauseBtn{
    width:55px;
    height:55px;
    border:0;
    border-radius:15px;
    background:#242424;
    color:white;
    font-size:25px;
}

.pauseBtn{
    font-size:31px;
}

/* ================= ROAD ================= */

.road{
    position:absolute;
    left:10%;
    right:10%;
    top:75px;
    height:555px;
    overflow:hidden;
    background:#383838;
    border-left:9px solid #606060;
    border-right:9px solid #606060;
}

.roadLines{
    position:absolute;
    inset:0;
    background:
        linear-gradient(
            to right,
            transparent 0 32.8%,
            white 32.8% 34%,
            transparent 34% 66%,
            white 66% 67.2%,
            transparent 67.2%
        );
    background-size:100% 110px;
    opacity:.9;
    animation:roadMove .45s linear infinite;
}

@keyframes roadMove{
    from{background-position:0 0}
    to{background-position:0 110px}
}

/* ================= CARS ================= */

.car{
    position:absolute;
    transform:translate(-50%,-50%);
    font-size:48px;
    z-index:5;
}

.player{
    font-size:55px;
    z-index:10;
    touch-action:none;
}

/* ================= CONTROLS ================= */

.controls{
    position:absolute;
    bottom:8px;
    left:0;
    right:0;
    height:90px;
    z-index:25;
    display:flex;
    justify-content:center;
    align-items:center;
    gap:8px;
}

.ctrl{
    width:58px;
    height:58px;
    border:2px solid #555;
    border-radius:15px;
    background:#242424;
    color:white;
    font-size:28px;
    touch-action:none;
}

/* ================= PAUSE ================= */

#pauseScreen,
#gameOver{
    display:none;
    position:absolute;
    inset:0;
    z-index:50;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    background:rgba(0,0,0,.82);
}

.pauseBox{
    width:80%;
    padding:25px;
    border-radius:20px;
    background:#181818;
    text-align:center;
}

.pauseBox button{
    width:100%;
    padding:13px;
    margin-top:10px;
    border:0;
    border-radius:12px;
    background:#d71919;
    color:white;
    font-size:17px;
}

/* ================= GAME OVER ================= */

.gameOverText{
    font-size:54px;
    font-weight:900;
    color:#ff2020;
    text-shadow:0 0 20px red;
    animation:fall .8s ease-out;
}

@keyframes fall{
    0%{
        transform:translateY(-350px) rotate(-10deg);
        opacity:0;
    }

    65%{
        transform:translateY(20px) rotate(4deg);
        opacity:1;
    }

    80%{
        transform:translateY(-8px) rotate(-2deg);
    }

    100%{
        transform:translateY(0) rotate(0);
    }
}

.gameOver button{
    margin-top:25px;
    padding:14px 35px;
    border:0;
    border-radius:14px;
    background:#d71919;
    color:white;
    font-size:18px;
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

            <button
                class="choice"
                id="menuMusic"
                onclick="toggleMusic()">
                🔊 BẬT
            </button>
        </div>

        <div class="label">
            ⚡ CHỌN CẤP ĐỘ
        </div>

        <div class="row">

            <button
                class="choice selected"
                onclick="selectDifficulty('easy',this)">
                DỄ
            </button>

            <button
                class="choice"
                onclick="selectDifficulty('medium',this)">
                VỪA
            </button>

            <button
                class="choice"
                onclick="selectDifficulty('hard',this)">
                KHÓ
            </button>

        </div>

        <div class="label">
            🚗 CHỌN XE
        </div>

        <div class="row">

            <button
                class="choice selected"
                onclick="selectCar('🚗',this)">
                🔴 ĐỎ
            </button>

            <button
                class="choice"
                onclick="selectCar('🚕',this)">
                🟡 VÀNG
            </button>

        </div>

        <button
            class="start"
            onclick="startGame()">
            🔥 BẮT ĐẦU
        </button>

        <div class="record">
            🏆 KỶ LỤC:
            <span id="menuRecord">0</span>
        </div>

    </div>

</div>


<!-- ================= GAME ================= -->

<div id="play">

    <div class="topbar">

        <div class="hearts" id="hearts">
            3❤️
        </div>

        <button
            class="soundBtn"
            id="gameMusic"
            onclick="toggleMusic()">
            🔊
        </button>

        <div class="score" id="score">
            0
        </div>

        <button
            class="pauseBtn"
            onclick="pauseGame()">
            ☰
        </button>

    </div>


    <div class="road" id="road">

        <div class="roadLines"></div>

        <div
            class="car player"
            id="player">
            🚗
        </div>

    </div>


    <div class="controls">

        <button
            class="ctrl"
            id="leftBtn">
            ←
        </button>

        <button
            class="ctrl"
            id="upBtn">
            ↑
        </button>

        <button
            class="ctrl"
            id="downBtn">
            ↓
        </button>

        <button
            class="ctrl"
            id="rightBtn">
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
            🏠 VỀ GIAO DIỆN CHÍNH
        </button>

    </div>

</div>


<!-- ================= GAME OVER ================= -->

<div id="gameOver">

    <div class="gameOverText">
        GAME OVER
    </div>

    <div style="margin-top:15px;">
        Điểm:
        <span id="finalScore">0</span>
    </div>

    <button onclick="backMenu()">
        🏠 VỀ MENU
    </button>

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

const menu =
    document.getElementById("menu");

const play =
    document.getElementById("play");

const road =
    document.getElementById("road");

const player =
    document.getElementById("player");

const heartsText =
    document.getElementById("hearts");

const scoreText =
    document.getElementById("score");

const bgMusic =
    document.getElementById("bgMusic");

const endMusic =
    document.getElementById("endMusic");


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


/* ================= DIFFICULTY ================= */

function selectDifficulty(level,button){

    difficulty = level;

    document
        .querySelectorAll(".row .choice")
        .forEach(b => {
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


/* ================= CAR ================= */

function selectCar(car,button){

    selectedCar = car;

    document
        .querySelectorAll(".row .choice")
        .forEach(b => {
            if(
                b.innerText.includes("ĐỎ") ||
                b.innerText.includes("VÀNG")
            ){
                b.classList.remove("selected");
            }
        });

    button.classList.add("selected");
}


/* ================= MUSIC ================= */

function toggleMusic(){

    musicOn = !musicOn;

    document.getElementById("menuMusic").innerText =
        musicOn ? "🔊 BẬT" : "🔇 TẮT";

    document.getElementById("gameMusic").innerText =
        musicOn ? "🔊" : "🔇";

    if(musicOn){

        if(playing){
            bgMusic.play().catch(()=>{});
        }

    }else{

        bgMusic.pause();
    }
}


/* ================= START ================= */

function startGame(){

    menu.style.display = "none";
    play.style.display = "block";

    document.getElementById("gameOver")
        .style.display = "none";

    hearts = 3;
    score = 0;

    heartsText.innerText = "3❤️";
    scoreText.innerText = "0";

    playerX = 50;
    playerY = 82;

    player.style.left = playerX + "%";
    player.style.top = playerY + "%";

    player.innerText = selectedCar;

    obstacles.forEach(o => o.remove());
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
        speed = 12;
    }

    if(musicOn){

        bgMusic.currentTime = 0;

        bgMusic.play().catch(()=>{});
    }

    clearInterval(spawnTimer);
    clearInterval(gameTimer);

    /*
       Không spam xe.
       Có khoảng trống cho người chơi né.
    */

    spawnTimer = setInterval(
        spawnObstacle,
        difficulty === "hard" ? 850 : 1100
    );

    gameTimer =
        setInterval(gameLoop,30);

    /*
       Chỉ tạo 2 xe lúc đầu.
    */

    setTimeout(spawnObstacle,400);
    setTimeout(spawnObstacle,1100);
}


/* ================= OBSTACLE ================= */

function spawnObstacle(){

    if(!playing || paused)
        return;

    const types = [
        "🛻",
        "🚛",
        "🚚",
        "🚧"
    ];

    const item =
        types[
            Math.floor(
                Math.random()*types.length
            )
        ];

    const obj =
        document.createElement("div");

    obj.className =
        "car obstacle";

    obj.innerText = item;

    const lane =
        Math.floor(Math.random()*3);

    const x =
        16.7 + lane*33.3;

    obj.style.left = x + "%";
    obj.style.top = "-10%";

    road.appendChild(obj);

    obstacles.push(obj);
}


/* ================= POTHOLE ================= */

function createPothole(){

    if(!playing || paused)
        return;

    const hole =
        document.createElement("div");

    hole.className =
        "car obstacle";

    hole.innerText = "🕳️";

    const lane =
        Math.floor(Math.random()*3);

    const x =
        16.7 + lane*33.3;

    hole.style.left = x + "%";
    hole.style.top = "-10%";

    road.appendChild(hole);

    obstacles.push(hole);
}


/* ================= GAME LOOP ================= */

function gameLoop(){

    if(!playing || paused)
        return;

    for(
        let i = obstacles.length - 1;
        i >= 0;
        i--
    ){

        const obj =
            obstacles[i];

        let top =
            parseFloat(obj.style.top);

        top += speed * 0.7;

        obj.style.top =
            top + "%";

        if(top > 110){

            obj.remove();

            obstacles.splice(i,1);

            score++;

            scoreText.innerText =
                score;

            continue;
        }

        checkCollision(obj);
    }

    /*
       Ổ gà xuất hiện vừa phải.
    */

    if(Math.random() < 0.018){
        createPothole();
    }
}


/* ================= COLLISION ================= */

function checkCollision(obj){

    if(!obj.parentNode)
        return;

    const a =
        player.getBoundingClientRect();

    const b =
        obj.getBoundingClientRect();

    const hit =
        a.left < b.right &&
        a.right > b.left &&
        a.top < b.bottom &&
        a.bottom > b.top;

    if(!hit)
        return;

    const type =
        obj.innerText;

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


/* ================= GIỮ NÚT DI CHUYỂN ================= */

let movingDirection = null;
let moveInterval = null;


/*
    Nhấn giữ:
    xe chạy liên tục.

    Thả:
    xe dừng ngay.
*/

function movePlayer(direction){

    if(!playing || paused)
        return;

    movingDirection =
        direction;

    moveOnce();

    clearInterval(moveInterval);

    moveInterval =
        setInterval(
            moveOnce,
            30
        );
}


function moveOnce(){

    if(!movingDirection)
        return;

    /*
       Tốc độ di chuyển ngang/dọc.
    */

    const step = 1.8;

    if(movingDirection === "left"){
        playerX -= step;
    }

    if(movingDirection === "right"){
        playerX += step;
    }

    if(movingDirection === "up"){
        playerY -= step;
    }

    if(movingDirection === "down"){
        playerY += step;
    }

    playerX =
        Math.max(
            8,
            Math.min(92,playerX)
        );

    playerY =
        Math.max(
            8,
            Math.min(88,playerY)
        );

    player.style.left =
        playerX + "%";

    player.style.top =
        playerY + "%";
}


function stopMoving(){

    movingDirection = null;

    clearInterval(moveInterval);

    moveInterval = null;
}


/* ================= NÚT ĐIỀU KHIỂN ================= */

function setupControl(id,direction){

    const button =
        document.getElementById(id);

    button.addEventListener(
        "pointerdown",
        function(e){

            e.preventDefault();

            movePlayer(direction);
        }
    );

    button.addEventListener(
        "pointerup",
        function(e){

            e.preventDefault();

            stopMoving();
        }
    );

    button.addEventListener(
        "pointercancel",
        stopMoving
    );

    button.addEventListener(
        "pointerleave",
        function(){

            stopMoving();
        }
    );
}


setupControl(
    "leftBtn",
    "left"
);

setupControl(
    "rightBtn",
    "right"
);

setupControl(
    "upBtn",
    "up"
);

setupControl(
    "downBtn",
    "down"
);


/* ================= KÉO XE ================= */

let dragging = false;


player.addEventListener(
    "pointerdown",
    function(e){

        if(!playing || paused)
            return;

        dragging = true;

        player.setPointerCapture(
            e.pointerId
        );
    }
);


player.addEventListener(
    "pointermove",
    function(e){

        if(!dragging)
            return;

        const rect =
            road.getBoundingClientRect();

        playerX =
            ((e.clientX - rect.left)
            / rect.width) * 100;

        playerY =
            ((e.clientY - rect.top)
            / rect.height) * 100;

        playerX =
            Math.max(
                8,
                Math.min(92,playerX)
            );

        playerY =
            Math.max(
                8,
                Math.min(88,playerY)
            );

        player.style.left =
            playerX + "%";

        player.style.top =
            playerY + "%";
    }
);


player.addEventListener(
    "pointerup",
    function(){

        dragging = false;
    }
);


/* ================= PAUSE ================= */

function pauseGame(){

    if(!playing)
        return;

    paused = true;

    document.getElementById(
        "pauseScreen"
    ).style.display = "flex";

    bgMusic.pause();
}


function resumeGame(){

    paused = false;

    document.getElementById(
        "pauseScreen"
    ).style.display = "none";

    if(musicOn){

        bgMusic.play().catch(()=>{});
    }
}


/* ================= GAME OVER ================= */

function gameOver(){

    playing = false;

    clearInterval(spawnTimer);
    clearInterval(gameTimer);
    clearInterval(moveInterval);

    movingDirection = null;

    bgMusic.pause();

    if(musicOn){

        endMusic.currentTime = 0;

        endMusic.play().catch(()=>{});
    }

    document.getElementById(
        "finalScore"
    ).innerText = score;

    document.getElementById(
        "gameOver"
    ).style.display = "flex";

    const oldRecord =
        Number(
            localStorage.getItem(
                "ngonLuaRecord"
            ) || 0
        );

    if(score > oldRecord){

        localStorage.setItem(
            "ngonLuaRecord",
            score
        );
    }
}


/* ================= MENU ================= */

function backMenu(){

    playing = false;
    paused = false;

    clearInterval(spawnTimer);
    clearInterval(gameTimer);
    clearInterval(moveInterval);

    movingDirection = null;

    bgMusic.pause();
    endMusic.pause();

    obstacles.forEach(
        o => o.remove()
    );

    obstacles = [];

    document.getElementById(
        "pauseScreen"
    ).style.display = "none";

    document.getElementById(
        "gameOver"
    ).style.display = "none";

    play.style.display = "none";
    menu.style.display = "flex";

    document.getElementById(
        "menuRecord"
    ).innerText =
        localStorage.getItem(
            "ngonLuaRecord"
        ) || 0;
}


/* ================= KEYBOARD ================= */

document.addEventListener(
    "keydown",
    function(e){

        if(!playing || paused)
            return;

        if(e.key === "ArrowLeft")
            movePlayer("left");

        if(e.key === "ArrowRight")
            movePlayer("right");

        if(e.key === "ArrowUp")
            movePlayer("up");

        if(e.key === "ArrowDown")
            movePlayer("down");
    }
);


document.addEventListener(
    "keyup",
    function(e){

        if(
            e.key === "ArrowLeft" ||
            e.key === "ArrowRight" ||
            e.key === "ArrowUp" ||
            e.key === "ArrowDown"
        ){

            stopMoving();
        }
    }
);


/* ================= RECORD ================= */

document.getElementById(
    "menuRecord"
).innerText =
    localStorage.getItem(
        "ngonLuaRecord"
    ) || 0;

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
