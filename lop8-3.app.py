import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="Ngọn lửa rực cháy",
    page_icon="🔥",
    layout="centered"
)

# =========================
# ĐỌC NHẠC TỪ REPO
# =========================

def audio_base64(filename):
    try:
        with open(filename, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

music_main = audio_base64("Nhạc game.mp3")
music_end = audio_base64("Nhạc game kết thúc.mp3")

game = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width,
initial-scale=1.0,
maximum-scale=1.0,
user-scalable=no">

<style>

* {{
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #080808;
    font-family: Arial, sans-serif;
}}

body {{
    display: flex;
    justify-content: center;
    align-items: center;
}}

#game {{
    position: relative;
    width: min(430px, 100vw);
    height: min(800px, 100vh);
    overflow: hidden;
    background: #111;
}}

.hidden {{
    display: none !important;
}}

/* =========================
   MENU
========================= */

#menu {{
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at center,
        #5b0909 0%,
        #210505 38%,
        #070707 78%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    z-index: 50;
}}

.title {{
    color: #ff4a00;
    font-size: clamp(34px, 10vw, 54px);
    font-weight: 900;
    font-style: italic;
    text-align: center;
    line-height: 1.05;

    text-shadow:
        0 0 5px #ff0000,
        0 0 15px #ff3300,
        0 0 30px #ff6600;

    animation: heartbeat 1.2s infinite;
}}

@keyframes heartbeat {{
    0%, 100% {{
        transform: scale(1);
    }}
    15% {{
        transform: scale(1.06);
    }}
    30% {{
        transform: scale(1);
    }}
    45% {{
        transform: scale(1.05);
    }}
    60% {{
        transform: scale(1);
    }}
}}

.subtitle {{
    color: #ddd;
    margin-top: 10px;
    margin-bottom: 18px;
    font-size: 15px;
    letter-spacing: 2px;
}}

.musicBox {{
    width: 88%;
    max-width: 330px;
    padding: 12px;
    border-radius: 14px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,100,30,0.5);
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 15px;
}}

button {{
    border: none;
    cursor: pointer;
    font-family: inherit;
}}

.musicButton {{
    background: #222;
    color: white;
    padding: 9px 14px;
    border-radius: 10px;
    font-size: 15px;
}}

.sectionTitle {{
    color: white;
    font-weight: bold;
    margin: 7px;
}}

.difficulty {{
    display: flex;
    gap: 8px;
    margin-bottom: 14px;
}}

.diffButton {{
    padding: 10px 15px;
    border-radius: 10px;
    background: #242424;
    color: white;
    border: 1px solid #555;
}}

.diffButton.selected {{
    background: #e22;
    border-color: #ff5b00;
    box-shadow: 0 0 12px #ff3300;
}}

.cars {{
    display: flex;
    gap: 15px;
    margin-bottom: 18px;
}}

.carButton {{
    width: 100px;
    height: 65px;
    border-radius: 14px;
    background: #242424;
    color: white;
    font-size: 30px;
    border: 2px solid #555;
}}

.carButton.selected {{
    border-color: #ff4500;
    box-shadow: 0 0 15px #ff3300;
}}

.startButton {{
    width: 240px;
    padding: 15px;
    border-radius: 15px;
    background: linear-gradient(90deg,#c90000,#ff4b00);
    color: white;
    font-size: 21px;
    font-weight: bold;
    box-shadow: 0 0 18px #ff3300;
}}

.record {{
    margin-top: 15px;
    color: #ffd36b;
    font-size: 17px;
}}

/* =========================
   GAME
========================= */

#road {{
    position: absolute;
    top: 65px;
    bottom: 0;
    left: 13%;
    right: 13%;
    background:
        repeating-linear-gradient(
            to bottom,
            #383838 0px,
            #383838 38px,
            #444 39px,
            #444 78px
        );
    border-left: 8px solid #555;
    border-right: 8px solid #555;
    overflow: hidden;
}}

.laneLine {{
    position: absolute;
    top: 0;
    bottom: 0;
    width: 5px;
    background: repeating-linear-gradient(
        to bottom,
        #eee 0px,
        #eee 28px,
        transparent 28px,
        transparent 55px
    );
    opacity: 0.8;
}}

.lane1 {{
    left: 33.33%;
}}

.lane2 {{
    left: 66.66%;
}}

#topBar {{
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 65px;
    background: rgba(5,5,5,0.95);
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 13px;
}}

#hearts {{
    color: #ff3333;
    font-size: 21px;
    font-weight: bold;
}}

#score {{
    color: white;
    font-size: 18px;
    font-weight: bold;
}}

#menuBtn {{
    width: 43px;
    height: 43px;
    border-radius: 10px;
    background: #222;
    color: white;
    font-size: 25px;
}}

#gameMusicBtn {{
    position: absolute;
    left: 90px;
    top: 10px;
    z-index: 30;
    background: #222;
    color: white;
    border-radius: 10px;
    padding: 9px;
}}

#player {{
    position: absolute;
    width: 55px;
    height: 82px;
    left: 50%;
    bottom: 25px;
    transform: translateX(-50%);
    z-index: 10;
    font-size: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    user-select: none;
    touch-action: none;
}}

.obstacle {{
    position: absolute;
    width: 54px;
    height: 62px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 43px;
    z-index: 8;
}}

.pothole {{
    font-size: 38px;
}}

.guard {{
    font-size: 42px;
}}

#pauseScreen,
#gameOver {{
    position: absolute;
    inset: 0;
    z-index: 40;
    background: rgba(0,0,0,0.78);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
}}

.pauseTitle {{
    font-size: 38px;
    font-weight: bold;
}}

.pauseButton,
.overButton {{
    margin-top: 12px;
    width: 220px;
    padding: 13px;
    border-radius: 12px;
    background: #d71919;
    color: white;
    font-size: 18px;
}}

#gameOverTitle {{
    font-size: 50px;
    font-weight: 900;
    font-style: italic;
    color: #ff2222;
    text-shadow:
        0 0 10px red,
        0 0 25px orange;
    animation: fallOver 0.8s ease-out;
}}

@keyframes fallOver {{
    0% {{
        transform: translateY(-300px) rotate(-8deg);
    }}
    65% {{
        transform: translateY(25px) rotate(3deg);
    }}
    80% {{
        transform: translateY(-10px) rotate(-2deg);
    }}
    100% {{
        transform: translateY(0) rotate(0);
    }}
}}

.shake {{
    animation: shake 0.35s;
}}

@keyframes shake {{
    0%,100% {{ transform: translateX(0); }}
    25% {{ transform: translateX(-8px); }}
    50% {{ transform: translateX(8px); }}
    75% {{ transform: translateX(-6px); }}
}}

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

    <div class="musicBox">
        <span style="font-size:20px;">🎵 NHẠC</span>

        <button
            class="musicButton"
            onclick="toggleMusic()"
            id="menuMusic">
            🔊 BẬT
        </button>
    </div>

    <div class="sectionTitle">
        ĐỘ KHÓ
    </div>

    <div class="difficulty">

        <button
            class="diffButton selected"
            onclick="selectDifficulty('easy')"
            id="easy">
            DỄ
        </button>

        <button
            class="diffButton"
            onclick="selectDifficulty('medium')"
            id="medium">
            VỪA
        </button>

        <button
            class="diffButton"
            onclick="selectDifficulty('hard')"
            id="hard">
            KHÓ
        </button>

    </div>

    <div class="sectionTitle">
        CHỌN XE
    </div>

    <div class="cars">

        <button
            class="carButton selected"
            onclick="selectCar('red')"
            id="redCar">
            🚗
        </button>

        <button
            class="carButton"
            onclick="selectCar('yellow')"
            id="yellowCar">
            🚕
        </button>

    </div>

    <button
        class="startButton"
        onclick="startGame()">
        🔥 BẮT ĐẦU
    </button>

    <div class="record">
        🏆 KỶ LỤC:
        <span id="menuRecord">0</span>
    </div>

</div>


<!-- ================= TOP BAR ================= -->

<div id="topBar" class="hidden">

    <div id="hearts">
        3❤️
    </div>

    <div id="score">
        0
    </div>

    <button id="gameMusicBtn"
            onclick="toggleMusic()">
        🔊
    </button>

    <button id="menuBtn"
            onclick="openPause()">
        ☰
    </button>

</div>


<!-- ================= ROAD ================= -->

<div id="road" class="hidden">

    <div class="laneLine lane1"></div>
    <div class="laneLine lane2"></div>

    <div id="player">
        🚗
    </div>

</div>


<!-- ================= PAUSE ================= -->

<div id="pauseScreen" class="hidden">

    <div class="pauseTitle">
        ⏸️ TẠM DỪNG
    </div>

    <button class="pauseButton"
            onclick="continueGame()">
        ▶️ TIẾP TỤC
    </button>

    <button class="pauseButton"
            onclick="backToMenu()">
        🏠 VỀ MENU
    </button>

</div>


<!-- ================= GAME OVER ================= -->

<div id="gameOver" class="hidden">

    <div id="gameOverTitle">
        GAME OVER
    </div>

    <div style="font-size:22px;margin-top:10px;">
        Điểm: <span id="finalScore">0</span>
    </div>

    <button class="overButton"
            onclick="startGame()">
        🔄 CHƠI LẠI
    </button>

    <button class="overButton"
            onclick="backToMenu()">
        🏠 MENU CHÍNH
    </button>

</div>


<!-- ================= AUDIO ================= -->

<audio
    id="bgMusic"
    loop>
    <source
        src="data:audio/mpeg;base64,{music_main}"
        type="audio/mpeg">
</audio>

<audio
    id="endMusic">
    <source
        src="data:audio/mpeg;base64,{music_end}"
        type="audio/mpeg">
</audio>


<script>

const menu = document.getElementById("menu");
const road = document.getElementById("road");
const player = document.getElementById("player");
const topBar = document.getElementById("topBar");

const heartsText = document.getElementById("hearts");
const scoreText = document.getElementById("score");

const pauseScreen = document.getElementById("pauseScreen");
const gameOver = document.getElementById("gameOver");

const bgMusic = document.getElementById("bgMusic");
const endMusic = document.getElementById("endMusic");

let difficulty = "easy";
let selectedCar = "red";

let musicOn = true;

let score = 0;
let hearts = 3;

let playing = false;
let paused = false;

let playerX = 50;
let playerY = 75;

let obstacles = [];

let lastTime = 0;
let spawnTimer = 0;

let record =
    Number(localStorage.getItem("ngonLuaRecord")) || 0;

document.getElementById("menuRecord").textContent = record;


/* =========================
   ĐỘ KHÓ
========================= */

function selectDifficulty(level) {{

    difficulty = level;

    document.querySelectorAll(".diffButton")
        .forEach(b => b.classList.remove("selected"));

    document.getElementById(level)
        .classList.add("selected");
}}


/* =========================
   CHỌN XE
========================= */

function selectCar(car) {{

    selectedCar = car;

    document.querySelectorAll(".carButton")
        .forEach(b => b.classList.remove("selected"));

    if (car === "red") {{

        document.getElementById("redCar")
            .classList.add("selected");

        player.textContent = "🚗";

    }} else {{

        document.getElementById("yellowCar")
            .classList.add("selected");

        player.textContent = "🚕";
    }}
}}


/* =========================
   NHẠC
========================= */

function toggleMusic() {{

    musicOn = !musicOn;

    if (musicOn) {{

        document.getElementById("menuMusic")
            .textContent = "🔊 BẬT";

        document.getElementById("gameMusicBtn")
            .textContent = "🔊";

        if (playing && !paused) {{
            bgMusic.play().catch(()=>{{}});
        }}

    }} else {{

        document.getElementById("menuMusic")
            .textContent = "🔇 TẮT";

        document.getElementById("gameMusicBtn")
            .textContent = "🔇";

        bgMusic.pause();
    }}
}}


/* =========================
   BẮT ĐẦU
========================= */

function startGame() {{

    menu.classList.add("hidden");
    pauseScreen.classList.add("hidden");
    gameOver.classList.add("hidden");

    topBar.classList.remove("hidden");
    road.classList.remove("hidden");

    score = 0;
    hearts = 3;

    scoreText.textContent = "0";
    heartsText.textContent = "3❤️";

    playing = true;
    paused = false;

    playerX = 50;
    playerY = 75;

    player.style.left = playerX + "%";
    player.style.top = playerY + "%";
    player.style.bottom = "auto";

    obstacles.forEach(o => o.el.remove());
    obstacles = [];

    lastTime = performance.now();
    spawnTimer = 0;

    endMusic.pause();
    endMusic.currentTime = 0;

    if (musicOn) {{
        bgMusic.currentTime = 0;
        bgMusic.play().catch(()=>{{}});
    }}

    requestAnimationFrame(gameLoop);
}}


/* =========================
   SPAWN XE
========================= */

function spawnObstacle() {{

    const types = [
        "🛻",
        "🚛",
        "🚚",
        "🚧",
        "🕳️"
    ];

    const type =
        types[Math.floor(Math.random() * types.length)];

    const el = document.createElement("div");

    el.className = "obstacle";

    if (type === "🕳️") {{
        el.classList.add("pothole");
    }}

    if (type === "🚧") {{
        el.classList.add("guard");
    }}

    el.textContent = type;

    const lane =
        Math.floor(Math.random() * 3);

    el.style.left =
        (lane * 33.33 + 16.66) + "%";

    el.style.top = "-70px";

    road.appendChild(el);

    obstacles.push({{
        el: el,
        y: -70,
        lane: lane,
        type: type
    }});
}}


/* =========================
   GAME LOOP
========================= */

function gameLoop(time) {{

    if (!playing || paused) return;

    const delta =
        Math.min(time - lastTime, 40);

    lastTime = time;

    let speed;

    if (difficulty === "easy") {{
        speed = 0.18;
    }} else if (difficulty === "medium") {{
        speed = 0.28;
    }} else {{
        // KHÓ = MAX
        speed = 0.50;
    }}

    spawnTimer += delta;

    /*
       TĂNG MẬT ĐỘ VẬT CẢN
       khoảng 80%
    */

    const spawnRate =
        difficulty === "hard" ? 330 :
        difficulty === "medium" ? 480 :
        650;

    if (spawnTimer > spawnRate) {{

        spawnObstacle();

        // khó có thể xuất hiện thêm xe
        if (difficulty === "hard" &&
            Math.random() < 0.8) {{
            spawnObstacle();
        }}

        spawnTimer = 0;
    }}


    obstacles.forEach((o, index) => {{

        o.y += speed * delta;

        o.el.style.top =
            o.y + "px";

        const playerRect =
            player.getBoundingClientRect();

        const obstacleRect =
            o.el.getBoundingClientRect();

        const hit =
            playerRect.left < obstacleRect.right &&
            playerRect.right > obstacleRect.left &&
            playerRect.top < obstacleRect.bottom &&
            playerRect.bottom > obstacleRect.top;

        if (hit) {{

            if (o.type === "🕳️") {{
                endGame();
                return;
            }}

            loseHeart();

            o.el.remove();

            obstacles.splice(index, 1);

            return;
        }}

        if (o.y > road.clientHeight + 100) {{

            o.el.remove();

            obstacles.splice(index, 1);

            score++;

            scoreText.textContent = score;

            if (score > record) {{
                record = score;
                localStorage.setItem(
                    "ngonLuaRecord",
                    record
                );
            }}
        }}
    }});

    requestAnimationFrame(gameLoop);
}}


/* =========================
   MẤT TIM
========================= */

function loseHeart() {{

    hearts--;

    heartsText.textContent =
        hearts + "❤️";

    document.getElementById("game")
        .classList.add("shake");

    setTimeout(() => {{
        document.getElementById("game")
            .classList.remove("shake");
    }}, 350);

    if (hearts <= 0) {{
        endGame();
    }}
}}


/* =========================
   GAME OVER
========================= */

function endGame() {{

    if (!playing) return;

    playing = false;

    bgMusic.pause();

    if (musicOn) {{
        endMusic.currentTime = 0;
        endMusic.play().catch(()=>{{}});
    }}

    document.getElementById("finalScore")
        .textContent = score;

    gameOver.classList.remove("hidden");
}}


/* =========================
   PAUSE
========================= */

function openPause() {{

    if (!playing) return;

    paused = true;

    bgMusic.pause();

    pauseScreen.classList.remove("hidden");
}}

function continueGame() {{

    pauseScreen.classList.add("hidden");

    paused = false;

    if (musicOn) {{
        bgMusic.play().catch(()=>{{}});
    }}

    lastTime = performance.now();

    requestAnimationFrame(gameLoop);
}}


/* =========================
   VỀ MENU
========================= */

function backToMenu() {{

    playing = false;
    paused = false;

    bgMusic.pause();
    endMusic.pause();

    obstacles.forEach(o => o.el.remove());
    obstacles = [];

    pauseScreen.classList.add("hidden");
    gameOver.classList.add("hidden");
    topBar.classList.add("hidden");
    road.classList.add("hidden");

    menu.classList.remove("hidden");

    document.getElementById("menuRecord")
        .textContent = record;
}}


/* =========================
   DI CHUYỂN CHẠM
========================= */

let dragging = false;

road.addEventListener("touchstart", e => {{

    dragging = true;

    movePlayer(e.touches[0]);

}}, {{passive:false}});


road.addEventListener("touchmove", e => {{

    if (!dragging) return;

    e.preventDefault();

    movePlayer(e.touches[0]);

}}, {{passive:false}});


road.addEventListener("touchend", () => {{
    dragging = false;
}});


function movePlayer(touch) {{

    const rect =
        road.getBoundingClientRect();

    let x =
        ((touch.clientX - rect.left)
        / rect.width) * 100;

    let y =
        ((touch.clientY - rect.top)
        / rect.height) * 100;

    // Không cho xe ra ngoài đường

    x = Math.max(10, Math.min(90, x));

    y = Math.max(5, Math.min(90, y));

    playerX = x;
    playerY = y;

    player.style.left =
        playerX + "%";

    player.style.top =
        playerY + "%";
}}


/* =========================
   MOUSE
========================= */

road.addEventListener("mousedown", e => {{
    dragging = true;
    moveMouse(e);
}});

document.addEventListener("mousemove", e => {{
    if (dragging) moveMouse(e);
}});

document.addEventListener("mouseup", () => {{
    dragging = false;
}});

function moveMouse(e) {{

    const rect =
        road.getBoundingClientRect();

    let x =
        ((e.clientX - rect.left)
        / rect.width) * 100;

    let y =
        ((e.clientY - rect.top)
        / rect.height) * 100;

    x = Math.max(10, Math.min(90, x));
    y = Math.max(5, Math.min(90, y));

    playerX = x;
    playerY = y;

    player.style.left =
        playerX + "%";

    player.style.top =
        playerY + "%";
}}

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
