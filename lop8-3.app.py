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
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {
    box-sizing: border-box;
    user-select: none;
    -webkit-user-select: none;
}

body {
    margin: 0;
    background: #050505;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

#game {
    position: relative;
    width: 100%;
    max-width: 720px;
    height: 820px;
    margin: auto;
    overflow: hidden;
    background: linear-gradient(#10233b, #69b8d9 45%, #252525 45%);
}

/* ================= MENU ================= */

#menu {
    position: absolute;
    inset: 0;
    z-index: 20;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background:
        radial-gradient(circle at center, #321000 0%, #080808 60%);
    color: white;
}

.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    color: #ffcc33;
    text-shadow:
        0 0 5px #ff6600,
        0 0 15px #ff3300,
        3px 3px 0 #4b0900;
    margin-bottom: 10px;
}

.subtitle {
    color: #ffb347;
    font-size: 17px;
    margin-bottom: 25px;
    letter-spacing: 3px;
}

.flames {
    position: absolute;
    top: 20px;
    width: 100%;
    display: flex;
    justify-content: space-between;
    padding: 0 18px;
    font-size: 55px;
    filter: drop-shadow(0 0 12px #ff4500);
}

.card {
    width: 86%;
    padding: 20px;
    border-radius: 22px;
    background: rgba(20,20,20,.88);
    border: 2px solid #ff8c00;
    box-shadow: 0 0 25px rgba(255,80,0,.4);
    text-align: center;
}

.label {
    color: #ffd27a;
    font-size: 18px;
    margin-bottom: 10px;
}

button {
    border: none;
    cursor: pointer;
    font-weight: bold;
}

.diff button,
.car button {
    margin: 5px;
    padding: 12px 18px;
    border-radius: 12px;
    background: #292929;
    color: white;
    border: 2px solid #777;
}

.diff button.selected,
.car button.selected {
    background: linear-gradient(#ffb300, #ff5e00);
    border-color: #ffe5a0;
    color: #180900;
}

.start {
    margin-top: 20px;
    padding: 17px 65px;
    border-radius: 18px;
    font-size: 25px;
    color: white;
    background: linear-gradient(#ffb300,#ff3500);
    box-shadow: 0 0 18px #ff5e00;
}

.record {
    margin-top: 18px;
    color: #ffd86b;
    font-size: 17px;
}

/* ================= GAME ================= */

#hud {
    position: absolute;
    z-index: 10;
    top: 10px;
    left: 10px;
    right: 10px;
    display: flex;
    justify-content: space-between;
    color: white;
    font-weight: bold;
    font-size: 18px;
    text-shadow: 2px 2px 3px black;
}

#road {
    position: absolute;
    left: 12%;
    width: 76%;
    height: 100%;
    background: #303030;
    clip-path: polygon(37% 0%, 63% 0%, 100% 100%, 0% 100%);
    overflow: hidden;
}

.roadLine {
    position: absolute;
    width: 7px;
    height: 65px;
    background: white;
    left: 50%;
    transform: translateX(-50%);
    opacity: .85;
}

.edge {
    position: absolute;
    top: 0;
    width: 8px;
    height: 100%;
    background: #eeeeee;
}

.edge.left {
    left: 17%;
    transform: rotate(9deg);
}

.edge.right {
    right: 17%;
    transform: rotate(-9deg);
}

#objects {
    position: absolute;
    inset: 0;
}

.obstacle {
    position: absolute;
    font-size: 48px;
    transform: translate(-50%, -50%);
    filter: drop-shadow(0 5px 4px black);
}

#player {
    position: absolute;
    z-index: 8;
    bottom: 130px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 95px;
    filter: drop-shadow(0 7px 5px black);
    transition: left .08s linear;
}

#steering {
    position: absolute;
    z-index: 15;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 115px;
    height: 115px;
    border-radius: 50%;
    border: 12px solid #111;
    background: radial-gradient(circle,#444 0 28%,#171717 30% 100%);
    box-shadow:
        0 0 0 4px #777,
        0 0 15px #000;
    touch-action: none;
}

#steering::before,
#steering::after {
    content: "";
    position: absolute;
    background: #111;
}

#steering::before {
    width: 75px;
    height: 10px;
    top: 40px;
    left: 8px;
}

#steering::after {
    width: 10px;
    height: 75px;
    left: 40px;
    top: 8px;
}

#hint {
    position: absolute;
    bottom: 143px;
    width: 100%;
    text-align: center;
    color: white;
    font-size: 13px;
    opacity: .7;
}

/* ================= FIRE ================= */

.fireSide {
    position: absolute;
    z-index: 5;
    bottom: 30px;
    font-size: 50px;
    animation: fire 0.6s infinite alternate;
    filter: drop-shadow(0 0 10px #ff4d00);
}

.fireSide.left {
    left: 5px;
}

.fireSide.right {
    right: 5px;
}

@keyframes fire {
    from { transform: scale(.9) translateY(3px); }
    to { transform: scale(1.08) translateY(-5px); }
}

/* ================= GAME OVER ================= */

#over {
    display: none;
    position: absolute;
    z-index: 30;
    inset: 0;
    background: rgba(0,0,0,.84);
    color: white;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
}

#over h1 {
    color: #ff8c00;
    font-size: 42px;
}

.retry {
    padding: 15px 45px;
    background: linear-gradient(#ffb300,#ff4000);
    border-radius: 15px;
    font-size: 20px;
    color: white;
}

@media(max-width:500px) {
    #game {
        height: 100vh;
        min-height: 650px;
    }

    .title {
        font-size: 38px;
    }
}
</style>
</head>

<body>

<div id="game">

    <!-- MENU -->
    <div id="menu">

        <div class="flames">
            <span>🔥</span>
            <span>🔥</span>
        </div>

        <div class="title">NGỌN LỬA<br>RỰC CHÁY</div>
        <div class="subtitle">🏁 FIRE ROAD RACING 🏁</div>

        <div class="card">

            <div class="label">CHỌN ĐỘ KHÓ</div>

            <div class="diff">
                <button id="easy" class="selected" onclick="difficulty('easy')">
                    DỄ
                </button>

                <button id="medium" onclick="difficulty('medium')">
                    VỪA
                </button>

                <button id="hard" onclick="difficulty('hard')">
                    KHÓ
                </button>
            </div>

            <br>

            <div class="label">CHỌN XE</div>

            <div class="car">
                <button id="redCar" class="selected" onclick="chooseCar('red')">
                    🚗 ĐỎ COOL
                </button>

                <button id="pinkCar" onclick="chooseCar('pink')">
                    💗 HỒNG DỄ THƯƠNG
                </button>
            </div>

            <button class="start" onclick="startGame()">
                BẮT ĐẦU
            </button>

            <div class="record">
                🏆 KỶ LỤC: <span id="record">0</span>
            </div>

        </div>
    </div>

    <!-- HUD -->
    <div id="hud">
        <div>❤️ <span id="lives">4</span></div>
        <div>🏆 <span id="score">0</span></div>
    </div>

    <!-- ROAD -->
    <div id="road">

        <div class="edge left"></div>
        <div class="edge right"></div>

        <div id="objects"></div>

    </div>

    <div id="player">🚗</div>

    <div class="fireSide left">🔥</div>
    <div class="fireSide right">🔥</div>

    <div id="hint">
        Kéo hoặc chạm vào tay lái để điều khiển
    </div>

    <div id="steering"></div>

    <!-- GAME OVER -->
    <div id="over">
        <h1>🔥 GAME OVER 🔥</h1>
        <p>Điểm của bạn: <b id="finalScore">0</b></p>
        <p>Kỷ lục: <b id="finalRecord">0</b></p>
        <button class="retry" onclick="backToMenu()">
            CHƠI LẠI
        </button>
    </div>

</div>


<script>

let selectedDifficulty = "easy";
let selectedCar = "red";

let speed = 4;
let lives = 4;
let score = 0;

let playerX = 50;
let playing = false;

let objects = [];
let spawnTimer = 0;

let record = Number(localStorage.getItem("fireRoadRecord") || 0);

document.getElementById("record").innerText = record;


/* ================= SETTINGS ================= */

function difficulty(level) {

    selectedDifficulty = level;

    document.querySelectorAll(".diff button")
        .forEach(b => b.classList.remove("selected"));

    document.getElementById(level)
        .classList.add("selected");
}


function chooseCar(car) {

    selectedCar = car;

    document.querySelectorAll(".car button")
        .forEach(b => b.classList.remove("selected"));

    if(car === "red") {
        document.getElementById("redCar")
            .classList.add("selected");
    } else {
        document.getElementById("pinkCar")
            .classList.add("selected");
    }
}


/* ================= START ================= */

function startGame() {

    if(selectedDifficulty === "easy") {
        speed = 4;
    }

    if(selectedDifficulty === "medium") {
        speed = 6;
    }

    if(selectedDifficulty === "hard") {
        speed = 8;
    }

    lives = 4;
    score = 0;
    playerX = 50;

    objects = [];

    document.getElementById("lives").innerText = lives;
    document.getElementById("score").innerText = score;

    document.getElementById("menu").style.display = "none";
    document.getElementById("over").style.display = "none";

    document.getElementById("player").innerText =
        selectedCar === "red" ? "🚗" : "💗🚙";

    playing = true;

    requestAnimationFrame(gameLoop);
}


/* ================= SPAWN ================= */

function createObstacle() {

    const obj = document.createElement("div");

    obj.className = "obstacle";

    let types = ["🚘", "🚙", "🚧", "⚠️", "🛑", "🚦"];

    obj.innerText =
        types[Math.floor(Math.random() * types.length)];

    let x = 28 + Math.random() * 44;

    obj.style.left = x + "%";
    obj.style.top = "-70px";

    document.getElementById("objects").appendChild(obj);

    objects.push({
        element: obj,
        x: x,
        y: -70,
        counted: false
    });
}


/* ================= LOOP ================= */

function gameLoop() {

    if(!playing) return;

    spawnTimer++;

    if(spawnTimer > Math.max(35, 80 - speed * 5)) {

        createObstacle();

        spawnTimer = 0;
    }


    objects.forEach((o, index) => {

        o.y += speed;

        o.element.style.top = o.y + "px";


        /* SCORE */

        if(!o.counted && o.y > 470) {

            o.counted = true;

            score++;

            document.getElementById("score")
                .innerText = score;
        }


        /* COLLISION */

        if(
            o.y > 560 &&
            o.y < 690 &&
            Math.abs(o.x - playerX) < 10
        ) {

            loseLife();

            o.element.remove();

            objects.splice(index, 1);
        }


        /* REMOVE */

        if(o.y > 850) {

            o.element.remove();

            objects.splice(index, 1);
        }

    });

    requestAnimationFrame(gameLoop);
}


/* ================= LIFE ================= */

function loseLife() {

    lives--;

    document.getElementById("lives")
        .innerText = lives;

    if(lives <= 0) {

        gameOver();
    }
}


/* ================= GAME OVER ================= */

function gameOver() {

    playing = false;

    if(score > record) {

        record = score;

        localStorage.setItem(
            "fireRoadRecord",
            record
        );
    }

    document.getElementById("finalScore")
        .innerText = score;

    document.getElementById("finalRecord")
        .innerText = record;

    document.getElementById("over")
        .style.display = "flex";
}


/* ================= MENU ================= */

function backToMenu() {

    objects.forEach(o => o.element.remove());

    objects = [];

    document.getElementById("over")
        .style.display = "none";

    document.getElementById("menu")
        .style.display = "flex";

    document.getElementById("record")
        .innerText = record;
}


/* ================= STEERING ================= */

const wheel = document.getElementById("steering");

let steering = false;

wheel.addEventListener("pointerdown", e => {

    steering = true;

    wheel.setPointerCapture(e.pointerId);
});


wheel.addEventListener("pointerup", e => {

    steering = false;
});


wheel.addEventListener("pointermove", e => {

    if(!steering || !playing) return;

    let rect = wheel.getBoundingClientRect();

    let center =
        rect.left + rect.width / 2;

    let diff =
        e.clientX - center;

    playerX += diff * 0.08;

    playerX =
        Math.max(25, Math.min(75, playerX));

    document.getElementById("player")
        .style.left = playerX + "%";
});


/* ================= TOUCH SCREEN ================= */

document.addEventListener("touchmove", e => {

    if(!playing) return;

}, {passive:true});


/* ================= KEYBOARD ================= */

document.addEventListener("keydown", e => {

    if(!playing) return;

    if(e.key === "ArrowLeft") {

        playerX -= 3;
    }

    if(e.key === "ArrowRight") {

        playerX += 3;
    }

    playerX =
        Math.max(25, Math.min(75, playerX));

    document.getElementById("player")
        .style.left = playerX + "%";
});

</script>

</body>
</html>
"""

components.html(game, height=850, scrolling=False)
