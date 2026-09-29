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

#menu {
    width: 100%;
    min-height: 850px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: radial-gradient(circle, #401500, #080808 65%);
}

.title {
    font-size: 42px;
    font-weight: 900;
    color: #ff8c00;
    text-shadow: 0 0 18px #ff4500;
    text-align: center;
}

.subtitle {
    margin: 8px 0 18px;
    color: #ffd27a;
    font-weight: bold;
}

.musicBox {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 18px;
    padding: 9px 16px;
    border-radius: 14px;
    background: rgba(255,120,0,.15);
    border: 1px solid #ff8c00;
    color: #ffd27a;
    font-weight: bold;
}

.musicBox button {
    padding: 8px 14px;
    border-radius: 10px;
    background: #292929;
    color: white;
    border: 2px solid #777;
    cursor: pointer;
    font-weight: bold;
}

.musicBox button.on {
    background: linear-gradient(#ffb300,#ff5e00);
    border-color: #ffe5a0;
}

.diff,
.cars {
    display: flex;
    gap: 12px;
    margin: 8px;
}

.diff button,
.cars button {
    padding: 12px 18px;
    border-radius: 12px;
    border: 2px solid #555;
    background: #202020;
    color: white;
    font-weight: bold;
    cursor: pointer;
}

.diff button.selected,
.cars button.selected {
    background: linear-gradient(#ffb300,#ff5e00);
    border-color: #ffe6a0;
}

#startBtn {
    margin-top: 22px;
    padding: 15px 45px;
    border: none;
    border-radius: 15px;
    font-size: 20px;
    font-weight: 900;
    color: white;
    background: linear-gradient(90deg,#ff8c00,#ff2400);
    box-shadow: 0 0 20px #ff4500;
    cursor: pointer;
}

#game {
    display: none;
    position: relative;
    width: 100%;
    height: 850px;
    overflow: hidden;
    background: #111;
}

#road {
    position: absolute;
    inset: 0;
    background: linear-gradient(#303030,#171717);
    clip-path: polygon(35% 0%,65% 0%,100% 100%,0% 100%);
}

.laneLine {
    position: absolute;
    top: 0;
    width: 4px;
    height: 100%;
    background: repeating-linear-gradient(
        to bottom,
        white 0,
        white 35px,
        transparent 35px,
        transparent 70px
    );
    opacity: .7;
}

.laneLine.leftLane {
    left: 35%;
    transform: skewX(-10deg);
}

.laneLine.rightLane {
    left: 65%;
    transform: skewX(10deg);
}

#hud {
    position: absolute;
    top: 15px;
    left: 15px;
    right: 15px;
    display: flex;
    justify-content: space-between;
    z-index: 20;
    font-size: 20px;
    font-weight: bold;
}

#player {
    position: absolute;
    bottom: 80px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 60px;
    z-index: 10;
    user-select: none;
}

.obstacle {
    position: absolute;
    font-size: 48px;
    z-index: 8;
}

#steering {
    position: absolute;
    bottom: 15px;
    left: 50%;
    transform: translateX(-50%);
    width: 95px;
    height: 95px;
    border-radius: 50%;
    border: 7px solid #aaa;
    background: #222;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 45px;
    z-index: 30;
    user-select: none;
    touch-action: none;
}

#gameOver {
    display: none;
    position: absolute;
    inset: 0;
    z-index: 50;
    background: rgba(0,0,0,.9);
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

#gameOver h1 {
    color: #ff4b00;
    font-size: 40px;
}

#restartBtn,
#menuBtn {
    padding: 12px 25px;
    margin: 6px;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    cursor: pointer;
}
</style>
</head>

<body>

<div id="menu">

    <div class="title">
        🔥 NGỌN LỬA RỰC CHÁY 🔥
    </div>

    <div class="subtitle">
        🏁 FIRE ROAD RACING 🏁
    </div>

    <div class="musicBox">
        <span>🎵 NHẠC</span>
        <button id="musicBtn" class="on" onclick="toggleMusic()">
            🔊 BẬT
        </button>
    </div>

    <div>ĐỘ KHÓ</div>

    <div class="diff">
        <button id="easy" class="selected"
            onclick="setDifficulty('easy')">DỄ</button>

        <button id="medium"
            onclick="setDifficulty('medium')">VỪA</button>

        <button id="hard"
            onclick="setDifficulty('hard')">KHÓ</button>
    </div>

    <div>CHỌN XE</div>

    <div class="cars">
        <button id="red" class="selected"
            onclick="setCar('🚗')">
            🚗 ĐỎ COOL
        </button>

        <button id="pink"
            onclick="setCar('🚘')">
            🚘 HỒNG DỄ THƯƠNG
        </button>
    </div>

    <button id="startBtn" onclick="startGame()">
        🔥 BẮT ĐẦU 🔥
    </button>

    <div style="margin-top:20px">
        🏆 KỶ LỤC:
        <span id="record">0</span>
    </div>

</div>


<div id="game">

    <div id="road"></div>

    <div class="laneLine leftLane"></div>
    <div class="laneLine rightLane"></div>

    <div id="hud">
        <div id="lives">❤️❤️❤️❤️</div>
        <div>🔥 Điểm: <span id="score">0</span></div>
    </div>

    <div id="player">🚗</div>

    <div id="steering">↔️</div>

    <div id="gameOver">

        <div style="font-size:70px;">😔</div>

        <h1>🔥 GAME OVER 🔥</h1>

        <div>
            Điểm:
            <span id="finalScore">0</span>
        </div>

        <div>
            Kỷ lục:
            <span id="finalRecord">0</span>
        </div>

        <button id="restartBtn" onclick="startGame()">
            🔄 CHƠI LẠI
        </button>

        <button id="menuBtn" onclick="backToMenu()">
            🏠 MENU
        </button>

    </div>

</div>


<audio id="bgMusic" loop preload="auto">
    <source src="stay-with-me.mp3" type="audio/mpeg">
</audio>


<script>

let difficulty = "easy";
let car = "🚗";

let playing = false;
let lives = 4;
let score = 0;
let playerX = 50;
let obstacles = [];
let spawnTimer = 0;
let speed = 4;

let musicOn = true;

const bgMusic =
    document.getElementById("bgMusic");

let record = Number(
    localStorage.getItem("fireRoadRecord") || 0
);

document.getElementById("record").innerText = record;


function toggleMusic() {

    musicOn = !musicOn;

    const btn =
        document.getElementById("musicBtn");

    if (musicOn) {

        btn.innerText = "🔊 BẬT";
        btn.classList.add("on");

        if (playing) {
            bgMusic.play().catch(() => {});
        }

    } else {

        btn.innerText = "🔇 TẮT";
        btn.classList.remove("on");

        bgMusic.pause();
    }
}


function setDifficulty(value) {

    difficulty = value;

    document
        .querySelectorAll(".diff button")
        .forEach(b => b.classList.remove("selected"));

    document
        .getElementById(value)
        .classList.add("selected");
}


function setCar(value) {

    car = value;

    document
        .querySelectorAll(".cars button")
        .forEach(b => b.classList.remove("selected"));

    if (value === "🚗") {
        document
            .getElementById("red")
            .classList.add("selected");
    } else {
        document
            .getElementById("pink")
            .classList.add("selected");
    }
}


const lanes = [25,50,75];


function getLaneX(lane,y) {

    const progress =
        Math.min(y / 850, 1);

    if (lane === 0)
        return 36 - progress * 14;

    if (lane === 1)
        return 50;

    return 64 + progress * 14;
}


function createObstacle(lane = null) {

    if (lane === null) {
        lane = Math.floor(Math.random() * 3);
    }

    const el =
        document.createElement("div");

    el.className = "obstacle";

    const cars = ["🚧","🚙","🛻","🚕"];

    el.innerText =
        cars[Math.floor(Math.random() * cars.length)];

    el.lane = lane;
    el.y = -80;

    document
        .getElementById("game")
        .appendChild(el);

    obstacles.push(el);
}


function createSideObstacles() {
    createObstacle(0);
    createObstacle(2);
}


function startGame() {

    document.getElementById("menu").style.display = "none";
    document.getElementById("game").style.display = "block";
    document.getElementById("gameOver").style.display = "none";

    lives = 4;
    score = 0;
    playerX = 50;
    spawnTimer = 0;

    obstacles.forEach(o => o.remove());
    obstacles = [];

    document.getElementById("score").innerText = score;
    document.getElementById("lives").innerText = "❤️❤️❤️❤️";
    document.getElementById("player").innerText = car;

    if (difficulty === "easy") speed = 4;
    if (difficulty === "medium") speed = 5.5;
    if (difficulty === "hard") speed = 7;

    playing = true;

    if (musicOn) {
        bgMusic.currentTime = 0;
        bgMusic.volume = 0.55;
        bgMusic.play().catch(() => {});
    }

    requestAnimationFrame(gameLoop);
}


function gameLoop() {

    if (!playing) return;

    spawnTimer++;

    let spawnRate = 65;

    if (difficulty === "medium")
        spawnRate = 52;

    if (difficulty === "hard")
        spawnRate = 42;

    if (spawnTimer > spawnRate) {

        spawnTimer = 0;

        if (
            difficulty !== "easy" &&
            Math.random() < 0.35
        ) {
            createSideObstacles();
        } else {
            createObstacle();
        }
    }


    obstacles.forEach((o,index) => {

        o.y += speed;

        o.x =
            getLaneX(o.lane,o.y);

        o.style.top = o.y + "px";
        o.style.left = o.x + "%";
        o.style.transform = "translateX(-50%)";


        if (
            o.y > 690 &&
            o.y < 790 &&
            Math.abs(o.x - playerX) < 8
        ) {

            o.remove();

            obstacles.splice(index,1);

            loseLife();

            return;
        }


        if (o.y > 900) {

            o.remove();

            obstacles.splice(index,1);

            score++;

            document
                .getElementById("score")
                .innerText = score;
        }
    });


    document.getElementById("player").style.left =
        playerX + "%";

    requestAnimationFrame(gameLoop);
}


const steering =
    document.getElementById("steering");

let dragging = false;
let lastX = 0;


steering.addEventListener("pointerdown", e => {

    dragging = true;
    lastX = e.clientX;

    steering.setPointerCapture(e.pointerId);
});


steering.addEventListener("pointermove", e => {

    if (!dragging) return;

    const diff = e.clientX - lastX;

    lastX = e.clientX;

    playerX += diff * 0.16;

    playerX =
        Math.max(19,Math.min(81,playerX));
});


steering.addEventListener("pointerup", () => {
    dragging = false;
});


document.addEventListener("keydown", e => {

    if (!playing) return;

    if (e.key === "ArrowLeft")
        playerX -= 3;

    if (e.key === "ArrowRight")
        playerX += 3;

    playerX =
        Math.max(19,Math.min(81,playerX));
});


function loseLife() {

    lives--;

    let hearts = "";

    for (let i = 0; i < lives; i++)
        hearts += "❤️";

    document.getElementById("lives").innerText = hearts;

    if (lives <= 0)
        gameOver();
}


function playLoseSound() {

    if (!musicOn) return;

    const AudioContext =
        window.AudioContext ||
        window.webkitAudioContext;

    if (!AudioContext) return;

    const ctx = new AudioContext();

    const notes = [392,330,262];

    notes.forEach((freq,i) => {

        const osc = ctx.createOscillator();
        const gain = ctx.createGain();

        osc.type = "triangle";
        osc.frequency.value = freq;

        const start =
            ctx.currentTime + i * 0.28;

        gain.gain.setValueAtTime(
            0.0001,start
        );

        gain.gain.exponentialRampToValueAtTime(
            0.15,start + 0.03
        );

        gain.gain.exponentialRampToValueAtTime(
            0.0001,start + 0.25
        );

        osc.connect(gain);
        gain.connect(ctx.destination);

        osc.start(start);
        osc.stop(start + 0.27);
    });
}


function gameOver() {

    playing = false;

    bgMusic.pause();

    playLoseSound();

    if (score > record) {

        record = score;

        localStorage.setItem(
            "fireRoadRecord",
            record
        );
    }

    document.getElementById("finalScore").innerText = score;
    document.getElementById("finalRecord").innerText = record;
    document.getElementById("record").innerText = record;

    document.getElementById("gameOver").style.display = "flex";
}


function backToMenu() {

    playing = false;

    bgMusic.pause();

    document.getElementById("game").style.display = "none";
    document.getElementById("menu").style.display = "flex";
}

</script>

</body>
</html>
"""

components.html(
    game,
    height=850,
    scrolling=False
)
