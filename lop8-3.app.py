import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
page_title="Ngọn lửa rực cháy",
page_icon="🔥",
layout="centered"
)

game = r"""

<!DOCTYPE html>  <html>  
<head>  
<meta charset="UTF-8">  <style>  
* {  
    box-sizing: border-box;  
}  
  
body {  
    margin: 0;  
    background: #080808;  
    color: white;  
    font-family: Arial, sans-serif;  
    overflow: hidden;  
}  
  
#game {  
    width: 100%;  
    max-width: 900px;  
    height: 780px;  
    margin: auto;  
    position: relative;  
    overflow: hidden;  
    background: linear-gradient(#151515, #080808);  
}  
  
/* ================= MENU ================= */  
  
#menu {  
    position: absolute;  
    inset: 0;  
    z-index: 50;  
  
    display: flex;  
    flex-direction: column;  
    justify-content: center;  
    align-items: center;  
  
    padding: 20px;  
  
    background:  
        radial-gradient(  
            circle at center,  
            #5a1600 0%,  
            #260900 45%,  
            #050505 100%  
        );  
}  
  
.title {  
    font-size: 40px;  
    font-weight: bold;  
    color: #ff6a00;  
  
    text-shadow:  
        0 0 10px #ff3300,  
        0 0 25px #ff6600,  
        0 0 45px #ff2200;  
  
    text-align: center;  
    margin-bottom: 8px;  
}  
  
.subtitle {  
    font-size: 17px;  
    color: #ffd9a8;  
    margin-bottom: 14px;  
}  
  
.sectionTitle {  
    font-size: 20px;  
    margin: 9px 0 6px;  
    color: #fff;  
}  
  
/* NHẠC */  
  
.musicBox {  
    display: flex;  
    align-items: center;  
    justify-content: center;  
    gap: 12px;  
  
    padding: 10px 20px;  
  
    border: 2px solid #a84916;  
    border-radius: 18px;  
  
    background: #421500aa;  
  
    margin-bottom: 6px;  
}  
  
.musicButton {  
    border: none;  
    border-radius: 12px;  
  
    padding: 10px 20px;  
  
    background: linear-gradient(  
        135deg,  
        #ffb000,  
        #ff5a00  
    );  
  
    color: white;  
    font-size: 18px;  
    font-weight: bold;  
  
    cursor: pointer;  
}  
  
/* ĐỘ KHÓ */  
  
.difficulty {  
    display: flex;  
    gap: 9px;  
    margin-bottom: 3px;  
}  
  
.diffButton {  
    width: 100px;  
    padding: 12px 5px;  
  
    border: 2px solid #555;  
    border-radius: 15px;  
  
    background: #222;  
    color: white;  
  
    font-size: 18px;  
    font-weight: bold;  
  
    cursor: pointer;  
}  
  
.diffButton.selected {  
    background: linear-gradient(  
        135deg,  
        #ffb000,  
        #ff4b00  
    );  
  
    border-color: #ffd45a;  
  
    box-shadow:  
        0 0 15px #ff6a00;  
}  
  
/* CHỌN XE */  
  
.carChoices {  
    display: flex;  
    gap: 10px;  
    width: 100%;  
    max-width: 600px;  
    margin-bottom: 10px;  
}  
  
.carButton {  
    flex: 1;  
  
    padding: 13px 7px;  
  
    border: 2px solid #555;  
    border-radius: 15px;  
  
    background: #222;  
    color: white;  
  
    font-size: 17px;  
    font-weight: bold;  
  
    cursor: pointer;  
}  
  
.carButton.selected {  
    background: linear-gradient(  
        135deg,  
        #ffb000,  
        #ff4b00  
    );  
  
    border-color: #ffd45a;  
  
    box-shadow:  
        0 0 15px #ff6a00;  
}  
  
/* BẮT ĐẦU */  
  
.startButton {  
    width: 100%;  
    max-width: 620px;  
  
    padding: 17px;  
  
    margin-top: 7px;  
  
    border: none;  
    border-radius: 18px;  
  
    background: linear-gradient(  
        90deg,  
        #ff8a00,  
        #ff0000  
    );  
  
    color: white;  
  
    font-size: 25px;  
    font-weight: bold;  
  
    cursor: pointer;  
  
    box-shadow:  
        0 0 25px #ff3c00aa;  
}  
  
.startButton:hover {  
    transform: scale(1.02);  
}  
  
.recordMenu {  
    margin-top: 12px;  
    font-size: 20px;  
}  
  
/* ================= ROAD ================= */  
  
#road {  
    position: absolute;  
  
    left: 16%;  
    width: 68%;  
  
    top: 0;  
    bottom: 0;  
  
    background:  
        linear-gradient(  
            90deg,  
            #111 0%,  
            #333 4%,  
            #191919 5%,  
            #191919 95%,  
            #333 96%,  
            #111 100%  
        );  
  
    border-left: 5px solid #777;  
    border-right: 5px solid #777;  
}  
  
.lane {  
    position: absolute;  
  
    top: -100px;  
  
    width: 7px;  
    height: 90px;  
  
    background: white;  
  
    opacity: .8;  
  
    animation:  
        roadMove 0.65s linear infinite;  
}  
  
.lane1 {  
    left: 33.33%;  
}  
  
.lane2 {  
    left: 66.66%;  
}  
  
@keyframes roadMove {  
  
    from {  
        transform: translateY(-120px);  
    }  
  
    to {  
        transform: translateY(950px);  
    }  
}  
  
/* ================= PLAYER ================= */  
  
#player {  
    position: absolute;  
  
    width: 65px;  
    height: 105px;  
  
    font-size: 52px;  
  
    display: flex;  
  
    justify-content: center;  
    align-items: center;  
  
    z-index: 20;  
  
    user-select: none;  
  
    transition:  
        transform .05s linear;  
}  
  
/* ================= ENEMY ================= */  
  
.enemy {  
    position: absolute;  
  
    width: 62px;  
    height: 100px;  
  
    font-size: 48px;  
  
    display: flex;  
  
    justify-content: center;  
    align-items: center;  
  
    z-index: 15;  
}  
  
/* ================= TOP BAR ================= */  
  
#topBar {  
    position: absolute;  
  
    top: 0;  
    left: 0;  
    right: 0;  
  
    height: 65px;  
  
    z-index: 40;  
  
    display: flex;  
  
    align-items: center;  
    justify-content: space-between;  
  
    padding: 8px 14px;  
  
    pointer-events: none;  
}  
  
.info {  
    background: #000000aa;  
  
    padding: 8px 13px;  
  
    border-radius: 12px;  
  
    font-weight: bold;  
  
    font-size: 16px;  
}  
  
.topButtons {  
    display: flex;  
    gap: 8px;  
}  
  
#pauseButton,  
#musicGameButton {  
    pointer-events: auto;  
  
    border: none;  
  
    width: 48px;  
    height: 45px;  
  
    border-radius: 12px;  
  
    background: #000000cc;  
  
    color: white;  
  
    font-size: 24px;  
  
    cursor: pointer;  
}  
  
/* ================= PAUSE / GAME OVER ================= */  
  
#pauseScreen,  
#gameOver {  
    position: absolute;  
  
    inset: 0;  
  
    z-index: 45;  
  
    display: none;  
  
    flex-direction: column;  
  
    justify-content: center;  
    align-items: center;  
  
    background: #000000cc;  
}  
  
.panel {  
    background: #171717;  
  
    border: 2px solid #ff5a00;  
  
    border-radius: 20px;  
  
    padding: 30px;  
  
    text-align: center;  
  
    width: 80%;  
    max-width: 380px;  
  
    box-shadow:  
        0 0 30px #ff4d0044;  
}  
  
.panel h2 {  
    color: #ff7417;  
  
    font-size: 30px;  
  
    margin-top: 0;  
}  
  
.panel button {  
    display: block;  
  
    width: 100%;  
  
    padding: 13px;  
  
    margin: 10px 0;  
  
    border: none;  
  
    border-radius: 12px;  
  
    font-size: 17px;  
  
    font-weight: bold;  
  
    cursor: pointer;  
}  
  
.continue {  
    background: #ff7a00;  
    color: white;  
}  
  
.home {  
    background: #333;  
    color: white;  
}  
  
/* ================= MOBILE ================= */  
  
#controls {  
    position: absolute;  
  
    bottom: 20px;  
    left: 0;  
    right: 0;  
  
    z-index: 35;  
  
    display: flex;  
  
    justify-content: center;  
  
    gap: 10px;  
}  
  
.controlBtn {  
    width: 58px;  
    height: 52px;  
  
    border: none;  
  
    border-radius: 14px;  
  
    background: #000000aa;  
  
    color: white;  
  
    font-size: 25px;  
  
    cursor: pointer;  
  
    touch-action: none;  
}  
  
.controlBtn:active {  
    background: #ff4d00;  
}  
  
/* ================= PHONE ================= */  
  
@media (max-width: 600px) {  
  
    #game {  
        height: 780px;  
    }  
  
    #menu {  
        padding: 18px;  
        overflow-y: auto;  
    }  
  
    .title {  
        font-size: 34px;  
        margin-top: 5px;  
    }  
  
    .subtitle {  
        font-size: 16px;  
        margin-bottom: 10px;  
    }  
  
    .musicBox {  
        padding: 9px 16px;  
        margin-bottom: 5px;  
    }  
  
    .musicButton {  
        padding: 9px 17px;  
        font-size: 17px;  
    }  
  
    .sectionTitle {  
        margin: 9px 0 5px;  
    }  
  
    .difficulty {  
        gap: 7px;  
    }  
  
    .diffButton {  
        width: 92px;  
        padding: 11px 3px;  
    }  
  
    .carChoices {  
        gap: 8px;  
        margin-bottom: 8px;  
    }  
  
    .carButton {  
        padding: 12px 4px;  
        font-size: 16px;  
    }  
  
    .startButton {  
        padding: 15px;  
        font-size: 23px;  
        margin-top: 5px;  
    }  
  
    .recordMenu {  
        margin-top: 9px;  
        padding-bottom: 8px;  
    }  
}  
</style>  </head>  <body>  <div id="game">  <!-- ================= MENU ================= -->  <div id="menu">  <div class="title">  
    🔥 NGỌN LỬA<br>  
    RỰC CHÁY 🔥  
</div>  

<div class="subtitle">  
    🏎️ FIRE ROAD RACING 🏎️  
</div>  

<div class="musicBox">  

    <span style="font-size:22px;">  
        🎵 NHẠC  
    </span>  

    <button  
        class="musicButton"  
        onclick="toggleMusic()"  
        id="menuMusic"  
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
        id="redCarButton"  
        onclick="selectCar('red')"  
    >  
        🚗 ĐỎ COOL  
    </button>  

    <button  
        class="carButton"  
        id="yellowCarButton"  
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

</div>  <!-- ================= ROAD ================= -->  <div id="road">  <div class="lane lane1"></div>  
<div class="lane lane2"></div>

</div>  <!-- ================= PLAYER ================= -->  <div id="player">  
    🚗  
</div>  <!-- ================= TOP ================= -->  <div id="topBar">  <div class="info">  

    ❤️ <span id="lives">4</span>  

    &nbsp;&nbsp;  

    ⭐ <span id="score">0</span>  

</div>  

<div class="topButtons">  

    <button  
        id="musicGameButton"  
        onclick="toggleMusic()"  
    >  
        🎵  
    </button>  

    <button  
        id="pauseButton"  
        onclick="openPause()"  
    >  
        ☰  
    </button>  

</div>

</div>  <!-- ================= MOBILE CONTROLS ================= -->  <div id="controls">  <button  
    class="controlBtn"  
    id="up"  
>  
    ⬆️  
</button>  

<button  
    class="controlBtn"  
    id="left"  
>  
    ⬅️  
</button>  

<button  
    class="controlBtn"  
    id="down"  
>  
    ⬇️  
</button>  

<button  
    class="controlBtn"  
    id="right"  
>  
    ➡️  
</button>

</div>  <!-- ================= PAUSE ================= -->  <div id="pauseScreen">  <div class="panel">  

    <h2>  
        ⏸️ TẠM DỪNG  
    </h2>  

    <button  
        class="continue"  
        onclick="resumeGame()"  
    >  
        ▶️ TIẾP TỤC  
    </button>  

    <button  
        class="home"  
        onclick="backToMenu()"  
    >  
        🏠 VỀ MENU CHÍNH  
    </button>  

</div>

</div>  <!-- ================= GAME OVER ================= -->  <div id="gameOver">  <div class="panel">  

    <h2>  
        😔 GAME OVER  
    </h2>  

    <p>  
        Điểm:  
        <b id="finalScore">0</b>  
    </p>  

    <p>  
        Kỷ lục:  
        <b id="record">0</b>  
    </p>  

    <button  
        class="continue"  
        onclick="restartGame()"  
    >  
        🔄 CHƠI LẠI  
    </button>  

    <button  
        class="home"  
        onclick="backToMenu()"  
    >  
        🏠 MENU CHÍNH  
    </button>  

</div>

</div>  </div>  <!-- ================= MUSIC ================= -->  <audio
id="bgMusic"
loop
preload="auto"

> 

<source
    src="https://cdn.jsdelivr.net/gh/honghoasamsunglt2-tech/ngon-lua-ruc-chay@main/music.mp3"
    type="audio/mpeg"
>

</audio>  <script>  
  
const game =  
    document.getElementById("game");  
  
const player =  
    document.getElementById("player");  
  
const menu =  
    document.getElementById("menu");  
  
const pauseScreen =  
    document.getElementById("pauseScreen");  
  
const gameOver =  
    document.getElementById("gameOver");  
  
const scoreText =  
    document.getElementById("score");  
  
const livesText =  
    document.getElementById("lives");  
  
const finalScore =  
    document.getElementById("finalScore");  
  
const recordText =  
    document.getElementById("record");  
  
const menuRecord =  
    document.getElementById("menuRecord");  
  
const bgMusic =  
    document.getElementById("bgMusic");  
  
  
let running = false;  
let paused = false;  
  
let score = 0;  
let lives = 4;  
  
let playerX = 0;  
let playerY = 0;  
  
let enemies = [];  
let enemyTimer = 0;  
  
let difficulty = "easy";  
let selectedCar = "red";  
  
let speed = 4;  
  
let keys = {};  
  
let musicOn = true;  
  
let lastTime = 0;  
  
let record =  
    Number(  
        localStorage.getItem(  
            "ngonLuaRecord"  
        ) || 0  
    );  
  
menuRecord.textContent = record;  
  
  
/* ================= CHỌN XE ================= */  
  
function selectCar(car) {  
  
    selectedCar = car;  
  
    document  
        .getElementById("redCarButton")  
        .classList.remove("selected");  
  
    document  
        .getElementById("yellowCarButton")  
        .classList.remove("selected");  
  
    if (car === "red") {  
  
        document  
            .getElementById("redCarButton")  
            .classList.add("selected");  
  
        player.textContent = "🚗";  
  
    } else {  
  
        document  
            .getElementById("yellowCarButton")  
            .classList.add("selected");  
  
        player.textContent = "🚕";  
    }  
}  
  
  
/* ================= ĐỘ KHÓ ================= */  
  
function selectDifficulty(level) {  
  
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
  
  
    if (level === "easy") {  
  
        speed = 4;  
  
        document  
            .getElementById("easyButton")  
            .classList.add("selected");  
    }  
  
  
    if (level === "medium") {  
  
        speed = 6;  
  
        document  
            .getElementById("mediumButton")  
            .classList.add("selected");  
    }  
  
  
    if (level === "hard") {  
  
        speed = 9;  
  
        document  
            .getElementById("hardButton")  
            .classList.add("selected");  
    }  
}  
  
  
/* ================= BẮT ĐẦU ================= */  
  
function startGame() {  
  
    menu.style.display = "none";  
  
    gameOver.style.display = "none";  
  
    pauseScreen.style.display = "none";  
  
    score = 0;  
  
    lives = 4;  
  
    enemyTimer = 0;  
  
    clearEnemies();  
  
    scoreText.textContent = "0";  
  
    livesText.textContent = "4";  
  
  
    if (selectedCar === "red") {  
  
        player.textContent = "🚗";  
  
    } else {  
  
        player.textContent = "🚕";  
    }  
  
  
    playerX =  
        game.clientWidth / 2 - 32;  
  
    playerY =  
        game.clientHeight - 180;  
  
  
    player.style.left =  
        playerX + "px";  
  
    player.style.top =  
        playerY + "px";  
  
  
    running = true;  
  
    paused = false;  
  
    lastTime = 0;  
  
  
    if (musicOn) {  
  
        bgMusic.currentTime = 0;  
  
        bgMusic.play().catch(  
            () => {}  
        );  
    }  
  
  
    requestAnimationFrame(gameLoop);  
}  
  
  
/* ================= GAME LOOP ================= */  
  
function gameLoop(time) {  
  
    if (!running) return;  
  
  
    if (paused) {  
  
        requestAnimationFrame(  
            gameLoop  
        );  
  
        return;  
    }  
  
  
    let dt =  
        (time - lastTime) / 16.67;  
  
  
    if (!lastTime) {  
  
        dt = 1;  
    }  
  
  
    lastTime = time;  
  
  
    movePlayer(dt);  
  
    moveEnemies(dt);  
  
    spawnEnemy();  
  
  
    score +=  
        0.03 * dt;  
  
  
    scoreText.textContent =  
        Math.floor(score);  
  
  
    requestAnimationFrame(  
        gameLoop  
    );  
}  
  
  
/* ================= DI CHUYỂN XE ================= */  
  
function movePlayer(dt) {  
  
    const amount =  
        7 * dt;  
  
  
    if (  
        keys["ArrowLeft"] ||  
        keys["a"]  
    ) {  
  
        playerX -= amount;  
    }  
  
  
    if (  
        keys["ArrowRight"] ||  
        keys["d"]  
    ) {  
  
        playerX += amount;  
    }  
  
  
    if (  
        keys["ArrowUp"] ||  
        keys["w"]  
    ) {  
  
        playerY -= amount;  
    }  
  
  
    if (  
        keys["ArrowDown"] ||  
        keys["s"]  
    ) {  
  
        playerY += amount;  
    }  
  
  
    const minX =  
        game.clientWidth * 0.16 + 8;  
  
  
    const maxX =  
        game.clientWidth * 0.84 - 70;  
  
  
    const minY = 70;  
  
  
    const maxY =  
        game.clientHeight - 125;  
  
  
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
  
  
/* ================= TẠO XE ĐỊCH ================= */  
  
function spawnEnemy() {  
  
    enemyTimer++;  
  
  
    let spawnRate = 70;  
  
  
    if (difficulty === "medium") {  
  
        spawnRate = 55;  
    }  
  
  
    if (difficulty === "hard") {  
  
        spawnRate = 42;  
    }  
  
  
    if (  
        enemyTimer < spawnRate  
    ) {  
  
        return;  
    }  
  
  
    enemyTimer = 0;  
  
  
    const enemy =  
        document.createElement("div");  
  
  
    enemy.className =  
        "enemy";  
  
  
    if (selectedCar === "red") {  
  
        enemy.textContent = "🚕";  
  
    } else {  
  
        enemy.textContent = "🚗";  
    }  
  
  
    const roadLeft =  
        game.clientWidth * 0.16;  
  
  
    const roadWidth =  
        game.clientWidth * 0.68;  
  
  
    const lane =  
        Math.floor(  
            Math.random() * 3  
        );  
  
  
    const laneWidth =  
        roadWidth / 3;  
  
  
    enemy.x =  
        roadLeft +  
        lane * laneWidth +  
        laneWidth / 2 -  
        31;  
  
  
    enemy.y = -120;  
  
  
    enemy.style.left =  
        enemy.x + "px";  
  
  
    enemy.style.top =  
        enemy.y + "px";  
  
  
    game.appendChild(enemy);  
  
    enemies.push(enemy);  
}  
  
  
/* ================= XE ĐỊCH DI CHUYỂN ================= */  
  
function moveEnemies(dt) {  
  
    for (  
        let i = enemies.length - 1;  
        i >= 0;  
        i--  
    ) {  
  
        const enemy =  
            enemies[i];  
  
  
        enemy.y +=  
            speed * dt;  
  
  
        enemy.style.top =  
            enemy.y + "px";  
  
  
        if (  
            checkCollision(  
                player,  
                enemy  
            )  
        ) {  
  
            enemy.remove();  
  
            enemies.splice(i, 1);  
  
            loseLife();  
  
            continue;  
        }  
  
  
        if (  
            enemy.y >  
            game.clientHeight + 120  
        ) {  
  
            enemy.remove();  
  
            enemies.splice(i, 1);  
        }  
    }  
}  
  
  
/* ================= VA CHẠM ================= */  
  
function checkCollision(a, b) {  
  
    const ar =  
        a.getBoundingClientRect();  
  
    const br =  
        b.getBoundingClientRect();  
  
  
    return !(  
        ar.right < br.left + 10 ||  
        ar.left + 10 > br.right ||  
        ar.bottom < br.top + 10 ||  
        ar.top + 10 > br.bottom  
    );  
}  
  
  
/* ================= MẤT MẠNG ================= */  
  
function loseLife() {  
  
    lives--;  
  
    livesText.textContent =  
        lives;  
  
  
    playLoseSound();  
  
  
    player.style.transform =  
        "scale(1.2)";  
  
  
    setTimeout(() => {  
  
        player.style.transform =  
            "scale(1)";  
  
    }, 150);  
  
  
    if (lives <= 0) {  
  
        endGame();  
    }  
}  
  
  
/* ================= XÓA XE ĐỊCH ================= */  
  
function clearEnemies() {  
  
    enemies.forEach(  
        e => e.remove()  
    );  
  
    enemies = [];  
}  
  
  
/* ================= GAME OVER ================= */  
  
function endGame() {  
  
    running = false;  
  
    bgMusic.pause();  
  
  
    finalScore.textContent =  
        Math.floor(score);  
  
  
    if (  
        Math.floor(score) > record  
    ) {  
  
        record =  
            Math.floor(score);  
  
  
        localStorage.setItem(  
            "ngonLuaRecord",  
            record  
        );  
    }  
  
  
    recordText.textContent =  
        record;  
  
  
    menuRecord.textContent =  
        record;  
  
  
    gameOver.style.display =  
        "flex";  
}  
  
  
/* ================= CHƠI LẠI ================= */  
  
function restartGame() {  
  
    gameOver.style.display =  
        "none";  
  
    startGame();  
}  
  
  
/* ================= TẠM DỪNG ================= */  
  
function openPause() {  
  
    if (!running) return;  
  
  
    paused = true;  
  
  
    pauseScreen.style.display =  
        "flex";  
  
  
    bgMusic.pause();  
}  
  
  
/* ================= TIẾP TỤC ================= */  
  
function resumeGame() {  
  
    paused = false;  
  
  
    pauseScreen.style.display =  
        "none";  
  
  
    if (musicOn) {  
  
        bgMusic.play().catch(  
            () => {}  
        );  
    }  
  
  
    lastTime =  
        performance.now();  
}  
  
  
/* ================= VỀ MENU ================= */  
  
function backToMenu() {  
  
    running = false;  
  
    paused = false;  
  
  
    clearEnemies();  
  
  
    bgMusic.pause();  
  
  
    pauseScreen.style.display =  
        "none";  
  
  
    gameOver.style.display =  
        "none";  
  
  
    menu.style.display =  
        "flex";  
  
  
    menuRecord.textContent =  
        record;  
}  
  
  
/* ================= NHẠC ================= */  
  
function toggleMusic() {  
  
    if (musicOn) {  
  
        musicOn = false;  
  
        bgMusic.pause();  
  
  
        document  
            .getElementById("menuMusic")  
            .textContent = "🔇 TẮT";  
  
  
        document  
            .getElementById("musicGameButton")  
            .textContent = "🔇";  
  
  
    } else {  
  
        musicOn = true;  
  
  
        bgMusic.play().catch(  
            () => {}  
        );  
  
  
        document  
            .getElementById("menuMusic")  
            .textContent = "🔊 BẬT";  
  
  
        document  
            .getElementById("musicGameButton")  
            .textContent = "🎵";  
    }  
}  
  
  
/* ================= BÀN PHÍM ================= */  
  
document.addEventListener(  
    "keydown",  
    function(e) {  
  
        keys[e.key] = true;  
  
  
        if (  
            [  
                "ArrowUp",  
                "ArrowDown",  
                "ArrowLeft",  
                "ArrowRight",  
                " "  
            ].includes(e.key)  
        ) {  
  
            e.preventDefault();  
        }  
  
  
        if (  
            e.key === "Escape" &&  
            running  
        ) {  
  
            if (paused) {  
  
                resumeGame();  
  
            } else {  
  
                openPause();  
            }  
        }  
    }  
);  
  
  
document.addEventListener(  
    "keyup",  
    function(e) {  
  
        keys[e.key] = false;  
    }  
);  
  
  
/* ================= NÚT ĐIỆN THOẠI ================= */  
  
function holdButton(  
    id,  
    key  
) {  
  
    const button =  
        document.getElementById(id);  
  
  
    button.addEventListener(  
        "pointerdown",  
        e => {  
  
            e.preventDefault();  
  
            keys[key] = true;  
        }  
    );  
  
  
    button.addEventListener(  
        "pointerup",  
        e => {  
  
            e.preventDefault();  
  
            keys[key] = false;  
        }  
    );  
  
  
    button.addEventListener(  
        "pointerleave",  
        () => {  
  
            keys[key] = false;  
        }  
    );  
  
  
    button.addEventListener(  
        "pointercancel",  
        () => {  
  
            keys[key] = false;  
        }  
    );  
}  
  
  
holdButton(  
    "up",  
    "ArrowUp"  
);  
  
  
holdButton(  
    "down",  
    "ArrowDown"  
);  
  
  
holdButton(  
    "left",  
    "ArrowLeft"  
);  
  
  
holdButton(  
    "right",  
    "ArrowRight"  
);  
  
  
/* ================= ÂM THANH VA CHẠM ================= */  
  
function playLoseSound() {  
  
    try {  
  
        const ctx =  
            new (  
                window.AudioContext ||  
                window.webkitAudioContext  
            )();  
  
  
        const notes = [  
            392,  
            330,  
            262  
        ];  
  
  
        notes.forEach(  
            (freq, i) => {  
  
                const osc =  
                    ctx.createOscillator();  
  
  
                const gain =  
                    ctx.createGain();  
  
  
                osc.type =  
                    "triangle";  
  
  
                osc.frequency.value =  
                    freq;  
  
  
                osc.connect(gain);  
  
                gain.connect(  
                    ctx.destination  
                );  
  
  
                gain.gain.setValueAtTime(  
                    0.12,  
                    ctx.currentTime +  
                    i * 0.12  
                );  
  
  
                gain.gain  
                    .exponentialRampToValueAtTime(  
                        0.001,  
                        ctx.currentTime +  
                        i * 0.12 +  
                        0.18  
                    );  
  
  
                osc.start(  
                    ctx.currentTime +  
                    i * 0.12  
                );  
  
  
                osc.stop(  
                    ctx.currentTime +  
                    i * 0.12 +  
                    0.2  
                );  
            }  
        );  
  
    } catch(e) {}  
}
</script>
</body>
</html>
"""

components.html(
    game,
    height=800,
    scrolling=False
)
