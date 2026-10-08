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

html,body{
    margin:0;
    padding:0;
    background:#050505;
    overflow:hidden;
    font-family:Arial,sans-serif;
}

#game{
    width:100%;
    max-width:430px;
    height:780px;
    margin:auto;
    position:relative;
    overflow:hidden;
    background:
        radial-gradient(circle at center,#321000,#080808 70%);
}

/* ================= MENU ================= */

#menu{
    position:absolute;
    inset:0;
    z-index:100;

    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;

    padding:20px;

    background:
        radial-gradient(
            circle,
            #631700 0%,
            #280700 45%,
            #050505 100%
        );
}

.title{
    font-size:43px;
    font-weight:900;
    font-style:italic;
    text-align:center;

    color:#ff4a00;

    text-shadow:
        0 0 5px #ff0000,
        0 0 12px #ff2600,
        0 0 25px #ff5100,
        0 0 45px #ff1800;

    animation:heartbeat 1.5s infinite;

    line-height:1.05;
    margin-bottom:10px;
}

@keyframes heartbeat{
    0%{transform:scale(1);}
    15%{transform:scale(1.08);}
    30%{transform:scale(1);}
    45%{transform:scale(1.06);}
    60%{transform:scale(1);}
    100%{transform:scale(1);}
}

.subtitle{
    color:#ffc7a1;
    font-size:15px;
    font-style:italic;
    margin-bottom:22px;
}

.musicBox{
    display:flex;
    align-items:center;
    gap:12px;

    background:#3b1000dd;
    border:2px solid #a93200;
    border-radius:18px;

    padding:10px 16px;
    margin-bottom:18px;

    box-shadow:0 0 15px #ff330055;
}

.musicButton{
    border:none;
    border-radius:12px;
    padding:9px 18px;

    background:linear-gradient(
        135deg,
        #ff9d00,
        #ff2600
    );

    color:white;
    font-size:17px;
    font-weight:bold;
}

.sectionTitle{
    color:white;
    font-size:19px;
    font-weight:bold;
    margin:8px 0;
}

.difficulty{
    display:flex;
    gap:8px;
    margin-bottom:14px;
}

.diffButton{
    width:95px;
    padding:11px 4px;

    border:2px solid #555;
    border-radius:14px;

    background:#222;
    color:white;

    font-size:16px;
    font-weight:bold;
}

.diffButton.selected{
    background:linear-gradient(
        135deg,
        #ffad00,
        #ff2700
    );

    border-color:#ffd36a;

    box-shadow:0 0 18px #ff4300;
}

.carChoices{
    display:flex;
    gap:10px;
    width:100%;
    max-width:330px;
    margin-bottom:18px;
}

.carButton{
    flex:1;
    padding:13px 5px;

    border:2px solid #555;
    border-radius:15px;

    background:#222;
    color:white;

    font-size:16px;
    font-weight:bold;
}

.carButton.selected{
    background:linear-gradient(
        135deg,
        #ffad00,
        #ff2700
    );

    border-color:#ffd36a;

    box-shadow:0 0 18px #ff4300;
}

.startButton{
    width:100%;
    max-width:340px;

    padding:16px;

    border:none;
    border-radius:18px;

    background:linear-gradient(
        90deg,
        #ff8a00,
        #e90000
    );

    color:white;

    font-size:23px;
    font-weight:900;

    box-shadow:0 0 25px #ff300077;
}

.recordMenu{
    margin-top:16px;

    background:#00000077;
    padding:8px 18px;

    border-radius:14px;

    font-size:18px;
}

/* ================= TOP BAR ================= */

#topBar{
    position:absolute;

    top:0;
    left:0;
    right:0;

    height:62px;

    z-index:50;

    display:flex;
    align-items:center;
    justify-content:space-between;

    padding:7px 10px;

    pointer-events:none;

    background:#050505ee;
}

.leftInfo{
    display:flex;
    gap:7px;
    align-items:center;
}

.infoBox{
    background:#000000cc;

    border-radius:13px;

    padding:8px 11px;

    font-size:17px;
    font-weight:bold;
}

.topRight{
    display:flex;
    gap:7px;
    align-items:center;
}

.topButton{
    pointer-events:auto;

    width:45px;
    height:42px;

    border:none;
    border-radius:11px;

    background:#000000cc;

    color:white;

    font-size:23px;
}

/* ================= ROAD ================= */

#road{
    position:absolute;

    left:10%;
    width:80%;

    /*
       ĐƯỜNG ĐUA NGẮN LẠI
       để nhìn thấy cả top bar + nút điều khiển
    */
    top:70px;
    height:525px;

    background:
        linear-gradient(
            90deg,
            #202020,
            #353535 3%,
            #191919 4%,
            #191919 96%,
            #353535 97%,
            #202020
        );

    border-left:5px solid #777;
    border-right:5px solid #777;

    overflow:hidden;
}

/* 3 LÀN */

.laneLine{
    position:absolute;

    top:-120px;

    width:5px;
    height:75px;

    background:white;

    opacity:.75;

    animation:
        roadMove .65s linear infinite;
}

.laneLine.one{
    left:33.33%;
}

.laneLine.two{
    left:66.66%;
}

@keyframes roadMove{
    from{
        transform:translateY(-120px);
    }

    to{
        transform:translateY(700px);
    }
}

/* ================= PLAYER ================= */

#player{
    position:absolute;

    width:65px;
    height:75px;

    font-size:52px;

    display:flex;
    justify-content:center;
    align-items:center;

    z-index:30;

    touch-action:none;

    filter:drop-shadow(
        0 5px 5px #000
    );
}

/* ================= OBSTACLE ================= */

.obstacle{
    position:absolute;

    width:62px;
    height:70px;

    display:flex;
    justify-content:center;
    align-items:center;

    font-size:43px;

    z-index:20;
}

.pothole{
    font-size:48px;
}

/* ================= NÚT DI CHUYỂN ================= */

#controls{
    position:absolute;

    left:0;
    right:0;

    bottom:18px;

    height:125px;

    z-index:60;

    display:flex;
    justify-content:center;
    align-items:center;

    pointer-events:auto;
}

.controlPad{
    width:180px;
    height:115px;

    position:relative;
}

.moveButton{
    position:absolute;

    width:55px;
    height:48px;

    border:2px solid #ff4b16;
    border-radius:13px;

    background:#170d0acc;

    color:white;

    font-size:25px;
    font-weight:bold;

    box-shadow:
        0 0 12px #ff350055;

    touch-action:none;
}

.moveButton:active{
    background:#ff4b16;
    transform:scale(.94);
}

.up{
    top:0;
    left:62px;
}

.down{
    bottom:0;
    left:62px;
}

.left{
    top:34px;
    left:0;
}

.right{
    top:34px;
    right:0;
}

/* ================= PAUSE ================= */

#pauseScreen{
    position:absolute;

    inset:0;

    z-index:80;

    display:none;

    align-items:center;
    justify-content:center;

    background:#000000cc;
}

.panel{
    width:82%;
    max-width:350px;

    background:#171717;

    border:2px solid #ff4d00;

    border-radius:20px;

    padding:25px;

    text-align:center;

    box-shadow:0 0 35px #ff300055;
}

.panel h2{
    color:#ff6417;
    font-size:29px;
}

.panel button{
    width:100%;

    padding:13px;

    margin-top:10px;

    border:none;
    border-radius:12px;

    font-size:17px;
    font-weight:bold;
}

.resume{
    background:#ff6a00;
    color:white;
}

.home{
    background:#333;
    color:white;
}

/* ================= GAME OVER ================= */

#gameOver{
    position:absolute;

    inset:0;

    z-index:90;

    display:none;

    align-items:center;
    justify-content:center;

    background:#000000bd;
}

/*
   GAME OVER LUÔN RƠI VÀO CHÍNH GIỮA
*/

.gameOverPanel{
    width:100%;
    text-align:center;

    display:flex;
    flex-direction:column;
    align-items:center;

    animation:
        fallGameOver
        .9s
        cubic-bezier(.2,1.6,.4,1)
        forwards;
}

@keyframes fallGameOver{

    0%{
        transform:
            translateY(-500px)
            rotate(-10deg);

        opacity:0;
    }

    45%{
        transform:
            translateY(30px)
            rotate(7deg);

        opacity:1;
    }

    60%{
        transform:
            translateY(-18px)
            rotate(-5deg);
    }

    75%{
        transform:
            translateY(10px)
            rotate(3deg);
    }

    88%{
        transform:
            translateY(-4px)
            rotate(-1deg);
    }

    100%{
        transform:
            translateY(0)
            rotate(0);
    }
}

.gameOverTitle{
    font-size:48px;

    font-weight:900;

    color:#ff2a00;

    font-style:italic;

    text-shadow:
        0 0 8px #ff0000,
        0 0 20px #ff4300,
        0 0 35px #ff0000;

    animation:
        shake
        .15s
        .9s
        6;
}

@keyframes shake{

    0%{
        transform:translateX(0);
    }

    25%{
        transform:translateX(-9px);
    }

    50%{
        transform:translateX(9px);
    }

    75%{
        transform:translateX(-7px);
    }

    100%{
        transform:translateX(0);
    }
}

.scoreFinal{
    color:white;

    font-size:20px;

    margin:12px 0 18px;
}

.gameOverButtons{
    display:flex;
    justify-content:center;
    gap:8px;
}

.gameOverButton{
    border:none;

    border-radius:13px;

    padding:13px 20px;

    font-size:16px;

    font-weight:bold;
}

.again{
    background:#ff6500;
    color:white;
}

.menuBack{
    background:#333;
    color:white;
}

/* ================= RESPONSIVE ================= */

@media(max-width:600px){

    #game{
        height:780px;
    }

    .title{
        font-size:38px;
    }

}

</style>
</head>

<body>

<div id="game">

<!-- ================= MENU ================= -->

<div id="menu">

    <div class="title">
        🔥 NGỌN LỬA<br>
        RỰC CHÁY 🔥
    </div>

    <div class="subtitle">
        🏎️ FIRE ROAD RACING 🏎️
    </div>

    <div class="musicBox">

        <span>🎵 NHẠC</span>

        <button
            class="musicButton"
            id="menuMusic"
            onclick="toggleMusic()"
        >
            🔊 BẬT
        </button>

    </div>

    <div class="sectionTitle">
        ĐỘ KHÓ
    </div>

    <div class="difficulty">

        <button
            class="diffButton selected"
            id="easyButton"
            onclick="selectDifficulty('easy')"
        >
            DỄ
        </button>

        <button
            class="diffButton"
            id="mediumButton"
            onclick="selectDifficulty('medium')"
        >
            VỪA
        </button>

        <button
            class="diffButton"
            id="hardButton"
            onclick="selectDifficulty('hard')"
        >
            KHÓ
        </button>

    </div>

    <div class="sectionTitle">
        CHỌN XE
    </div>

    <div class="carChoices">

        <button
            class="carButton selected"
            id="redCar"
            onclick="selectCar('red')"
        >
            🚗 ĐỎ
        </button>

        <button
            class="carButton"
            id="yellowCar"
            onclick="selectCar('yellow')"
        >
            🚕 VÀNG
        </button>

    </div>

    <button
        class="startButton"
        onclick="startGame()"
    >
        BẮT ĐẦU 🔥
    </button>

    <div class="recordMenu">
        🏆 KỶ LỤC:
        <span id="menuRecord">0</span>
    </div>

</div>


<!-- ================= ROAD ================= -->

<div id="road">

    <div class="laneLine one"></div>
    <div class="laneLine two"></div>

</div>


<!-- ================= PLAYER ================= -->

<div id="player">
    🚗
</div>


<!-- ================= TOP BAR ================= -->

<div id="topBar">

    <div class="infoBox">
    <span id="lives">3❤️</span>
</div>

        <div class="infoBox">

            🎵

            <button
                id="gameMusic"
                onclick="toggleMusic()"
                style="
                border:none;
                background:none;
                color:white;
                font-size:18px;
                "
            >
                🔊
            </button>

        </div>

    </div>

    <div class="topRight">

        <div class="infoBox">
            ⭐ <span id="score">0</span>
        </div>

        <button
            class="topButton"
            onclick="openPause()"
        >
            ☰
        </button>

    </div>

</div>


<!-- ================= NÚT DI CHUYỂN ================= -->

<div id="controls">

    <div class="controlPad">

        <button
            class="moveButton up"
            id="upBtn"
        >
            ↑
        </button>

        <button
            class="moveButton left"
            id="leftBtn"
        >
            ←
        </button>

        <button
            class="moveButton right"
            id="rightBtn"
        >
            →
        </button>

        <button
            class="moveButton down"
            id="downBtn"
        >
            ↓
        </button>

    </div>

</div>


<!-- ================= PAUSE ================= -->

<div id="pauseScreen">

    <div class="panel">

        <h2>
            ⏸️ TẠM DỪNG
        </h2>

        <button
            class="resume"
            onclick="resumeGame()"
        >
            ▶️ TIẾP TỤC
        </button>

        <button
            class="home"
            onclick="backToMenu()"
        >
            🏠 MENU CHÍNH
        </button>

    </div>

</div>


<!-- ================= GAME OVER ================= -->

<div id="gameOver">

    <div class="gameOverPanel">

        <div class="gameOverTitle">
            GAME OVER
        </div>

        <div class="scoreFinal">

            ⭐ Điểm:
            <b id="finalScore">0</b>

            <br>

            🏆 Kỷ lục:
            <b id="finalRecord">0</b>

        </div>

        <div class="gameOverButtons">

            <button
                class="gameOverButton again"
                onclick="restartGame()"
            >
                🔄 CHƠI LẠI
            </button>

            <button
                class="gameOverButton menuBack"
                onclick="backToMenu()"
            >
                🏠 VỀ MENU
            </button>

        </div>

    </div>

</div>


<!-- ================= AUDIO ================= -->

<audio
    id="bgMusic"
    loop
    preload="auto"
>

    <source
        src="https://raw.githubusercontent.com/honghoasamsunglt2-tech/ngon-lua-ruc-chay/main/Nh%E1%BA%A1c%20game.mp3"
        type="audio/mpeg"
    >

</audio>


<audio
    id="loseMusic"
    preload="auto"
>

    <source
        src="https://raw.githubusercontent.com/honghoasamsunglt2-tech/ngon-lua-ruc-chay/main/Nh%E1%BA%A1c%20game%20k%E1%BA%BFt%20th%C3%BAc.mp3"
        type="audio/mpeg"
    >

</audio>


<script>

/* ================= BIẾN ================= */

const game =
    document.getElementById("game");

const road =
    document.getElementById("road");

const player =
    document.getElementById("player");

const menu =
    document.getElementById("menu");

const pauseScreen =
    document.getElementById("pauseScreen");

const gameOver =
    document.getElementById("gameOver");

const bgMusic =
    document.getElementById("bgMusic");

const loseMusic =
    document.getElementById("loseMusic");

const livesText =
    document.getElementById("lives");

const scoreText =
    document.getElementById("score");

const menuRecord =
    document.getElementById("menuRecord");

const finalScore =
    document.getElementById("finalScore");

const finalRecord =
    document.getElementById("finalRecord");


let running = false;
let paused = false;

let lives = 3;
let score = 0;

let playerX = 0;
let playerY = 0;

let obstacles = [];

let spawnTimer = 0;

let difficulty = "easy";
let selectedCar = "red";

let speed = 3.5;

let musicOn = true;

let dragging = false;

let record =
    Number(
        localStorage.getItem(
            "ngonLuaRecord"
        ) || 0
    );

menuRecord.textContent = record;


/* ================= NÚT GIỮ ================= */

let movingLeft = false;
let movingRight = false;
let movingUp = false;
let movingDown = false;


/* ================= XE ================= */

function selectCar(car){

    selectedCar = car;

    document
        .getElementById("redCar")
        .classList.remove("selected");

    document
        .getElementById("yellowCar")
        .classList.remove("selected");


    if(car === "red"){

        document
            .getElementById("redCar")
            .classList.add("selected");

        player.textContent = "🚗";

    }else{

        document
            .getElementById("yellowCar")
            .classList.add("selected");

        player.textContent = "🚕";
    }
}


/* ================= ĐỘ KHÓ ================= */

function selectDifficulty(level){

    difficulty = level;

    document
        .getElementById("easyButton")
        .classList.remove("selected");

    document
        .getElementById("mediumButton")
        .classList.remove("selected");

    document
        .getElementById("hardButton")
        .classList.remove("selected");


    if(level === "easy"){

        speed = 3.5;

        document
            .getElementById("easyButton")
            .classList.add("selected");
    }


    if(level === "medium"){

        speed = 5.5;

        document
            .getElementById("mediumButton")
            .classList.add("selected");
    }


    if(level === "hard"){

        speed = 12;

        document
            .getElementById("hardButton")
            .classList.add("selected");
    }
}


/* ================= BẮT ĐẦU ================= */

function startGame(){

    menu.style.display = "none";

    gameOver.style.display = "none";

    pauseScreen.style.display = "none";

    lives = 3;
    score = 0;
    spawnTimer = 0;

    clearObstacles();

    livesText.textContent = "3";
    scoreText.textContent = "0";


    player.textContent =
        selectedCar === "red"
        ? "🚗"
        : "🚕";


    playerX =
        game.clientWidth / 2 - 32;


    playerY =
        480;


    player.style.left =
        playerX + "px";

    player.style.top =
        playerY + "px";


    running = true;
    paused = false;


    if(musicOn){

        bgMusic.currentTime = 0;

        bgMusic.play().catch(
            () => {}
        );
    }


    requestAnimationFrame(
        gameLoop
    );
}


/* ================= GAME LOOP ================= */

function gameLoop(){

    if(!running)
        return;


    if(paused){

        requestAnimationFrame(
            gameLoop
        );

        return;
    }


    movePlayerByButtons();

    moveObstacles();

    spawnObstacle();


    score += 0.03;

    scoreText.textContent =
        Math.floor(score);


    requestAnimationFrame(
        gameLoop
    );
}


/* ================= DI CHUYỂN XE ================= */

function movePlayerByButtons(){

    const moveSpeed = 6;


    if(movingLeft)
        playerX -= moveSpeed;

    if(movingRight)
        playerX += moveSpeed;

    if(movingUp)
        playerY -= moveSpeed;

    if(movingDown)
        playerY += moveSpeed;


    const minX =
        game.clientWidth * 0.10 + 5;

    const maxX =
        game.clientWidth * 0.90 - 70;


    /*
       XE CHỈ ĐI TRONG PHẦN ĐƯỜNG
    */

    playerX =
        Math.max(
            minX,
            Math.min(
                maxX,
                playerX
            )
        );


    /*
       KHÔNG CHO XE ĐI VÀO TOP BAR
       HOẶC KHU VỰC NÚT
    */

    const minY = 75;

    const maxY = 520;


    playerY =
        Math.max(
            minY,
            Math.min(
                maxY,
                playerY
            )
        );


    player.style.left =
        playerX + "px";

    player.style.top =
        playerY + "px";
}


/* ================= NÚT GIỮ ================= */

function setupMoveButton(
    id,
    direction
){

    const button =
        document.getElementById(id);


    button.addEventListener(
        "pointerdown",
        function(e){

            e.preventDefault();

            if(direction === "left")
                movingLeft = true;

            if(direction === "right")
                movingRight = true;

            if(direction === "up")
                movingUp = true;

            if(direction === "down")
                movingDown = true;
        }
    );


    button.addEventListener(
        "pointerup",
        function(e){

            e.preventDefault();

            if(direction === "left")
                movingLeft = false;

            if(direction === "right")
                movingRight = false;

            if(direction === "up")
                movingUp = false;

            if(direction === "down")
                movingDown = false;
        }
    );


    button.addEventListener(
        "pointercancel",
        function(){

            if(direction === "left")
                movingLeft = false;

            if(direction === "right")
                movingRight = false;

            if(direction === "up")
                movingUp = false;

            if(direction === "down")
                movingDown = false;
        }
    );


    button.addEventListener(
        "pointerleave",
        function(){

            if(direction === "left")
                movingLeft = false;

            if(direction === "right")
                movingRight = false;

            if(direction === "up")
                movingUp = false;

            if(direction === "down")
                movingDown = false;
        }
    );
}


setupMoveButton(
    "leftBtn",
    "left"
);

setupMoveButton(
    "rightBtn",
    "right"
);

setupMoveButton(
    "upBtn",
    "up"
);

setupMoveButton(
    "downBtn",
    "down"
);


/* ================= TẠO CHƯỚNG NGẠI ================= */

function spawnObstacle(){

    spawnTimer++;


    let rate = 75;


    if(difficulty === "medium")
        rate = 55;


    if(difficulty === "hard")
        rate = 38;


    if(spawnTimer < rate)
        return;


    spawnTimer = 0;


    const obstacle =
        document.createElement("div");


    obstacle.className =
        "obstacle";


    const random =
        Math.random();


    if(random < 0.20){

        obstacle.textContent = "🛻";
        obstacle.dataset.type =
            "vehicle";

    }else if(random < 0.40){

        obstacle.textContent = "🚛";
        obstacle.dataset.type =
            "vehicle";

    }else if(random < 0.60){

        obstacle.textContent = "🚚";
        obstacle.dataset.type =
            "vehicle";

    }else if(random < 0.82){

        obstacle.textContent = "🚧";
        obstacle.dataset.type =
            "barrier";

    }else{

        obstacle.textContent = "🕳️";

        obstacle.classList.add(
            "pothole"
        );

        obstacle.dataset.type =
            "pothole";
    }


    const roadLeft =
        game.clientWidth * 0.10;

    const roadWidth =
        game.clientWidth * 0.80;


    const lane =
        Math.floor(
            Math.random() * 3
        );


    const laneWidth =
        roadWidth / 3;


    obstacle.x =
        roadLeft +
        lane * laneWidth +
        laneWidth / 2 -
        31;


    obstacle.y =
        75;


    obstacle.style.left =
        obstacle.x + "px";

    obstacle.style.top =
        obstacle.y + "px";


    game.appendChild(
        obstacle
    );


    obstacles.push(
        obstacle
    );
}


/* ================= DI CHUYỂN CHƯỚNG NGẠI ================= */

function moveObstacles(){

    for(
        let i =
        obstacles.length - 1;
        i >= 0;
        i--
    ){

        const obstacle =
            obstacles[i];


        obstacle.y += speed;


        obstacle.style.top =
            obstacle.y + "px";


        if(
            checkCollision(
                player,
                obstacle
            )
        ){

            const type =
                obstacle.dataset.type;


            obstacle.remove();

            obstacles.splice(
                i,
                1
            );


            if(
                type === "pothole"
            ){

                endGame();

                return;
            }


            loseLife();

            continue;
        }


        if(
            obstacle.y >
            560
        ){

            obstacle.remove();

            obstacles.splice(
                i,
                1
            );
        }
    }
}


/* ================= VA CHẠM ================= */

function checkCollision(a,b){

    const ar =
        a.getBoundingClientRect();

    const br =
        b.getBoundingClientRect();


    return !(
        ar.right - 10 <
        br.left + 10 ||

        ar.left + 10 >
        br.right - 10 ||

        ar.bottom - 10 <
        br.top + 10 ||

        ar.top + 10 >
        br.bottom - 10
    );
}


/* ================= MẤT TIM ================= */

function loseLife(){

    lives--;

    livesText.textContent =
        lives;


    player.style.transform =
        "scale(1.25)";


    setTimeout(
        () => {

            player.style.transform =
                "scale(1)";

        },
        180
    );


    if(lives <= 0){

        endGame();
    }
}


/* ================= XÓA ================= */

function clearObstacles(){

    obstacles.forEach(
        obstacle =>
            obstacle.remove()
    );

    obstacles = [];
}


/* ================= GAME OVER ================= */

function endGame(){

    if(!running)
        return;


    running = false;


    movingLeft = false;
    movingRight = false;
    movingUp = false;
    movingDown = false;


    bgMusic.pause();


    if(musicOn){

        loseMusic.currentTime = 0;

        loseMusic.play().catch(
            () => {}
        );
    }


    const final =
        Math.floor(score);


    finalScore.textContent =
        final;


    if(final > record){

        record = final;

        localStorage.setItem(
            "ngonLuaRecord",
            record
        );
    }


    finalRecord.textContent =
        record;

    menuRecord.textContent =
        record;


    /*
       RESET ANIMATION
       để mỗi lần Game Over
       đều rơi lại từ trên xuống
    */

    const panel =
        document.querySelector(
            ".gameOverPanel"
        );


    panel.style.animation = "none";

    void panel.offsetWidth;

    panel.style.animation =
        "fallGameOver .9s cubic-bezier(.2,1.6,.4,1) forwards";


    gameOver.style.display =
        "flex";
}


/* ================= CHƠI LẠI ================= */

function restartGame(){

    loseMusic.pause();

    loseMusic.currentTime = 0;

    gameOver.style.display =
        "none";

    startGame();
}


/* ================= PAUSE ================= */

function openPause(){

    if(!running)
        return;


    paused = true;

    movingLeft = false;
    movingRight = false;
    movingUp = false;
    movingDown = false;

    bgMusic.pause();

    pauseScreen.style.display =
        "flex";
}


/* ================= TIẾP TỤC ================= */

function resumeGame(){

    paused = false;

    pauseScreen.style.display =
        "none";


    if(musicOn){

        bgMusic.play().catch(
            () => {}
        );
    }
}


/* ================= VỀ MENU ================= */

function backToMenu(){

    running = false;

    paused = false;

    movingLeft = false;
    movingRight = false;
    movingUp = false;
    movingDown = false;

    clearObstacles();

    bgMusic.pause();

    loseMusic.pause();

    pauseScreen.style.display =
        "none";

    gameOver.style.display =
        "none";

    menu.style.display =
        "flex";

    menuRecord.textContent =
        record;
}


/* ================= ÂM NHẠC ================= */

function toggleMusic(){

    musicOn =
        !musicOn;


    const menuButton =
        document.getElementById(
            "menuMusic"
        );

    const gameButton =
        document.getElementById(
            "gameMusic"
        );


    if(!musicOn){

        bgMusic.pause();

        loseMusic.pause();

        menuButton.textContent =
            "🔇 TẮT";

        gameButton.textContent =
            "🔇";

    }else{

        menuButton.textContent =
            "🔊 BẬT";

        gameButton.textContent =
            "🔊";


        if(running && !paused){

            bgMusic.play().catch(
                () => {}
            );
        }
    }
}


/* ================= KÉO XE ================= */

player.addEventListener(
    "pointerdown",
    function(e){

        if(!running || paused)
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

        if(
            !dragging ||
            !running ||
            paused
        )
            return;


        const rect =
            game.getBoundingClientRect();


        playerX =
            e.clientX -
            rect.left -
            32;


        playerY =
            e.clientY -
            rect.top -
            38;


        const minX =
            game.clientWidth * 0.10 + 5;

        const maxX =
            game.clientWidth * 0.90 - 70;


        playerX =
            Math.max(
                minX,
                Math.min(
                    maxX,
                    playerX
                )
            );


        playerY =
            Math.max(
                75,
                Math.min(
                    520,
                    playerY
                )
            );


        player.style.left =
            playerX + "px";

        player.style.top =
            playerY + "px";
    }
);


player.addEventListener(
    "pointerup",
    function(){

        dragging = false;
    }
);


player.addEventListener(
    "pointercancel",
    function(){

        dragging = false;
    }
);


/* ================= KHỞI TẠO ================= */

selectCar("red");

selectDifficulty("easy");

</script>

</body>
</html>
"""

components.html(
    game,
    height=800,
    scrolling=False
)
