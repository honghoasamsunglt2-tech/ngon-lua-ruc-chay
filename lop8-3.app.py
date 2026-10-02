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
# ĐỌC FILE NHẠC
# =========================
music_file = "Nhạc game 1 (1).m4a"

if os.path.exists(music_file):
    with open(music_file, "rb") as f:
        music_data = base64.b64encode(f.read()).decode()
    music_src = f"data:audio/mp4;base64,{music_data}"
else:
    music_src = ""

# =========================
# GAME
# =========================
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
    height: 800px;
    max-height: 100vh;
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
    z-index: 50;
    background:
        radial-gradient(circle at center, #351000 0%, #090909 65%);
    color: white;
    text-align: center;
    padding: 45px 20px;
}}

.title {{
    margin-top: 20px;
    font-size: 42px;
    font-weight: 1000;
    line-height: 1.05;
    color: #ff7a00;
    text-shadow:
        0 0 5px #ffea00,
        0 0 15px #ff5e00,
        0 0 30px #ff2600,
        0 0 55px #ff0000;
    animation: fire 1s infinite alternate;
}}

@keyframes fire {{
    from {{
        transform: scale(1);
        text-shadow:
            0 0 5px #ffea00,
            0 0 15px #ff5e00,
            0 0 30px #ff2600;
    }}
    to {{
        transform: scale(1.03);
        text-shadow:
            0 0 10px #fff000,
            0 0 25px #ff7b00,
            0 0 45px #ff2100;
    }}
}}

.menu-box {{
    margin-top: 35px;
}}

.menu-label {{
    font-size: 19px;
    font-weight: bold;
    margin: 16px 0 8px;
}}

.option-row {{
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
}}

.option {{
    border: 2px solid #555;
    background: #202020;
    color: white;
    padding: 12px 18px;
    border-radius: 14px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
}}

.option.selected {{
    border-color: #ff7b00;
    background: #512000;
    box-shadow: 0 0 15px #ff5e00;
}}

#startBtn {{
    margin-top: 28px;
    width: 85%;
    padding: 17px;
    border: none;
    border-radius: 18px;
    background: linear-gradient(135deg, #ff8a00, #ff2600);
    color: white;
    font-size: 23px;
    font-weight: 1000;
    box-shadow: 0 0 25px #ff4d00;
    cursor: pointer;
}}

.musicBtn {{
    margin-top: 18px;
    border: 2px solid #777;
    background: #191919;
    color: white;
    padding: 10px 20px;
    border-radius: 14px;
    font-weight: bold;
}}

/* =========================
   GAME HUD
========================= */

#hud {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 12px;
    pointer-events: none;
}}

#pauseBtn {{
    pointer-events: auto;
    width: 50px;
    height: 50px;
    border: none;
    border-radius: 14px;
    background: rgba(0,0,0,.75);
    color: white;
    font-size: 27px;
}}

#score {{
    font-size: 22px;
    font-weight: 1000;
    color: white;
    text-shadow: 0 2px 5px black;
}}

#lives {{
    font-size: 23px;
    letter-spacing: 2px;
    white-space: nowrap;
}}

/* =========================
   ROAD
========================= */

#road {{
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 74%;
    height: 100%;
    background: #181818;
    border-left: 9px solid #555;
    border-right: 9px solid #555;
    overflow: hidden;
}}

.guardrail {{
    position: absolute;
    top: 0;
    width: 15px;
    height: 100%;
    z-index: 5;
    background:
        repeating-linear-gradient(
            0deg,
            #eeeeee 0px,
            #eeeeee 25px,
            #e63900 25px,
            #e63900 50px
        );
    box-shadow: 0 0 8px #000;
}}

.guardrail.left {{
    left: 0;
}}

.guardrail.right {{
    right: 0;
}}

.lane-line {{
    position: absolute;
    top: -100px;
    width: 7px;
    height: 100px;
    background: white;
    opacity: .8;
}}

#line1 {{
    left: 33.33%;
}}

#line2 {{
    left: 66.66%;
}}

/* =========================
   CARS
========================= */

.car {{
    position: absolute;
    font-size: 52px;
    width: 62px;
    height: 65px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
    user-select: none;
}}

#player {{
    bottom: 135px;
}}

.enemy {{
    top: -90px;
}}

/* =========================
   CONTROLS
========================= */

#controls {{
    position: absolute;
    bottom: 15px;
    left: 0;
    width: 100%;
    z-index: 30;
    display: flex;
    justify-content: center;
    gap: 14px;
}}

.control {{
    width: 70px;
    height: 62px;
    border: none;
    border-radius: 18px;
    background: rgba(0,0,0,.82);
    color: white;
    font-size: 32px;
    box-shadow: 0 4px 10px black;
}}

.control:active {{
    transform: scale(.9);
    background: #333;
}}

/* =========================
   PAUSE
========================= */

#pauseMenu,
#gameOver {{
    position: absolute;
    inset: 0;
    z-index: 100;
    background: rgba(0,0,0,.88);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    text-align: center;
}}

.popup {{
    width: 82%;
    padding: 28px 20px;
    border-radius: 22px;
    background: #191919;
    border: 2px solid #555;
    box-shadow: 0 0 30px #000;
}}

.popup h2 {{
    margin-top: 0;
    font-size: 30px;
}}

.popup button {{
    width: 90%;
    padding: 14px;
    margin: 8px;
    border: none;
    border-radius: 14px;
    font-size: 18px;
    font-weight: bold;
}}

.continue {{
    background: #ff7b00;
    color: white;
}}

.exit {{
    background: #444;
    color: white;
}}

#finalScore {{
    font-size: 25px;
    color: #ffd000;
    font-weight: bold;
}}

</style>
</head>

<body>

<div id="game">

    <!-- MENU -->
    <div id="menu">

        <div class="title">
            🔥 NGỌN LỬA<br>RỰC CHÁY 🔥
        </div>

        <div class="menu-box">

            <div class="menu-label">⚡ Độ khó</div>

            <div class="option-row">
                <button class="option selected"
                        onclick="setDifficulty('easy', this)">
                    DỄ
                </button>

                <button class="option"
                        onclick="setDifficulty('medium', this)">
                    VỪA
                </button>

                <button class="option"
                        onclick="setDifficulty('hard', this)">
                    KHÓ
                </button>
            </div>

            <div class="menu-label">🚗 Chọn xe</div>

            <div class="option-row">
                <button class="option selected"
                        onclick="selectCar('🚗', this)">
                    🚗 ĐỎ COOL
                </button>

                <button class="option"
                        onclick="selectCar('🚕', this)">
                    🚕 VÀNG
                </button>
            </div>

            <button id="startBtn" onclick="startGame()">
                🔥 BẮT ĐẦU CHƠI 🔥
            </button>

            <br>

            <button class="musicBtn" onclick="toggleMusic()">
                🎵 Nhạc: <span id="musicStatus">BẬT</span>
            </button>

        </div>
    </div>


    <!-- HUD -->
    <div id="hud" class="hidden">

        <button id="pauseBtn" onclick="pauseGame()">
            ☰
        </button>

        <div id="score">
            ⭐ 0
        </div>

        <div id="lives">
            ❤️❤️❤️❤️
        </div>

    </div>


    <!-- ROAD -->
    <div id="road" class="hidden">

        <div class="guardrail left"></div>
        <div class="guardrail right"></div>

        <div id="line1" class="lane-line"></div>
        <div id="line2" class="lane-line"></div>

        <div id="player" class="car">🚗</div>

    </div>


    <!-- CONTROLS -->
    <div id="controls" class="hidden">

        <button class="control"
                ontouchstart="move('up')"
                onclick="move('up')">
            ⬆️
        </button>

        <button class="control"
                ontouchstart="move('left')"
                onclick="move('left')">
            ⬅️
        </button>

        <button class="control"
                ontouchstart="move('down')"
                onclick="move('down')">
            ⬇️
        </button>

        <button class="control"
                ontouchstart="move('right')"
                onclick="move('right')">
            ➡️
        </button>

    </div>


    <!-- PAUSE -->
    <div id="pauseMenu" class="hidden">

        <div class="popup">

            <h2>⏸️ TẠM DỪNG</h2>

            <button class="continue"
                    onclick="resumeGame()">
                ▶️ Tiếp tục
            </button>

            <button class="exit"
                    onclick="backToMenu()">
                🚪 Thoát
            </button>

        </div>

    </div>


    <!-- GAME OVER -->
    <div id="gameOver" class="hidden">

        <div class="popup">

            <h2>💥 GAME OVER 💥</h2>

            <div id="finalScore">
                Điểm: 0
            </div>

            <br>

            <button class="continue"
                    onclick="restartGame()">
                🔄 Chơi lại
            </button>

            <button class="exit"
                    onclick="backToMenu()">
                🏠 Về menu
            </button>

        </div>

    </div>


    <!-- MUSIC -->
    <audio id="bgMusic"
           loop
           preload="auto">
        <source src="{music_src}" type="audio/mp4">
    </audio>

</div>


<script>

const road = document.getElementById("road");
const player = document.getElementById("player");
const scoreText = document.getElementById("score");
const livesText = document.getElementById("lives");
const bgMusic = document.getElementById("bgMusic");

let difficulty = "easy";
let playerCar = "🚗";

let speed = 4;

let score = 0;
let lives = 4;

let gameRunning = false;
let paused = false;

let playerLane = 1;
let playerX = 0;

let enemies = [];
let enemyTimer = null;

let animationId = null;

let musicOn = true;

let bestScore =
    Number(localStorage.getItem("ngonLuaBestScore") || 0);


/* =========================
   ĐỘ KHÓ
========================= */

function setDifficulty(level, btn) {{

    difficulty = level;

    document.querySelectorAll(".option").forEach(b => {{
        if (
            b.innerText.includes("DỄ") ||
            b.innerText.includes("VỪA") ||
            b.innerText.includes("KHÓ")
        ) {{
            b.classList.remove("selected");
        }}
    }});

    btn.classList.add("selected");

    if (level === "easy") speed = 4;
    if (level === "medium") speed = 6;
    if (level === "hard") speed = 9;
}}


/* =========================
   CHỌN XE
========================= */

function selectCar(car, btn) {{

    playerCar = car;

    document.querySelectorAll(".option").forEach(b => {{
        if (
            b.innerText.includes("ĐỎ COOL") ||
            b.innerText.includes("VÀNG")
        ) {{
            b.classList.remove("selected");
        }}
    }});

    btn.classList.add("selected");

    player.innerText = car;
}}


/* =========================
   NHẠC
========================= */

function toggleMusic() {{

    musicOn = !musicOn;

    document.getElementById("musicStatus").innerText =
        musicOn ? "BẬT" : "TẮT";

    if (!musicOn) {{
        bgMusic.pause();
    }}
}}


function startMusic() {{

    if (!musicOn) return;

    bgMusic.currentTime = 0;

    bgMusic.play().catch(() => {{}});
}}


function stopMusic() {{

    bgMusic.pause();
    bgMusic.currentTime = 0;
}}


/* =========================
   BẮT ĐẦU
========================= */

function startGame() {{

    document.getElementById("menu")
        .classList.add("hidden");

    road.classList.remove("hidden");
    document.getElementById("hud")
        .classList.remove("hidden");

    document.getElementById("controls")
        .classList.remove("hidden");

    document.getElementById("gameOver")
        .classList.add("hidden");

    score = 0;
    lives = 4;

    playerLane = 1;

    enemies.forEach(e => e.el.remove());
    enemies = [];

    updateHUD();

    player.style.bottom = "135px";

    positionPlayer();

    gameRunning = true;
    paused = false;

    startMusic();

    spawnEnemy();

    animationId = requestAnimationFrame(gameLoop);
}}


/* =========================
   VỊ TRÍ XE
========================= */

function positionPlayer() {{

    const roadWidth = road.clientWidth;

    const laneWidth = roadWidth / 3;

    playerX =
        laneWidth * playerLane +
        laneWidth / 2 -
        player.offsetWidth / 2;

    player.style.left = playerX + "px";
}}


/* =========================
   ĐIỀU KHIỂN
========================= */

function move(direction) {{

    if (!gameRunning || paused) return;

    const step = 22;

    let left =
        parseFloat(player.style.left || playerX);

    let bottom =
        parseFloat(player.style.bottom || 135);

    if (direction === "left") {{
        left -= step;
    }}

    if (direction === "right") {{
        left += step;
    }}

    if (direction === "up") {{
        bottom += step;
    }}

    if (direction === "down") {{
        bottom -= step;
    }}

    const maxLeft =
        road.clientWidth - player.offsetWidth - 15;

    left = Math.max(15, Math.min(maxLeft, left));

    bottom = Math.max(125, Math.min(610, bottom));

    player.style.left = left + "px";
    player.style.bottom = bottom + "px";
}}


/* =========================
   PHÍM BÀN PHÍM
========================= */

document.addEventListener("keydown", function(e) {{

    if (e.key === "ArrowLeft" || e.key.toLowerCase() === "a")
        move("left");

    if (e.key === "ArrowRight" || e.key.toLowerCase() === "d")
        move("right");

    if (e.key === "ArrowUp" || e.key.toLowerCase() === "w")
        move("up");

    if (e.key === "ArrowDown" || e.key.toLowerCase() === "s")
        move("down");

    if (e.key === "Escape") {{

        if (paused) {{
            resumeGame();
        }} else {{
            pauseGame();
        }}

    }}

}});


/* =========================
   TẠO XE
========================= */

function spawnEnemy() {{

    if (!gameRunning || paused) return;

    const enemy = document.createElement("div");

    enemy.className = "car enemy";

    const types = [
        "🚙",
        "🚕",
        "🚓",
        "🚗",
        "🚘"
    ];

    enemy.innerText =
        types[Math.floor(Math.random() * types.length)];

    const lane =
        Math.floor(Math.random() * 3);

    const laneWidth =
        road.clientWidth / 3;

    const x =
        lane * laneWidth +
        laneWidth / 2 -
        31;

    enemy.style.left = x + "px";
    enemy.style.top = "-90px";

    road.appendChild(enemy);

    enemies.push({{
        el: enemy,
        scored: false
    }});

    let nextTime;

    if (difficulty === "easy") {{
        nextTime = 1300;
    }} else if (difficulty === "medium") {{
        nextTime = 950;
    }} else {{
        nextTime = 700;
    }}

    enemyTimer = setTimeout(spawnEnemy, nextTime);
}}


/* =========================
   VA CHẠM
========================= */

function collision(a, b) {{

    const r1 = a.getBoundingClientRect();
    const r2 = b.getBoundingClientRect();

    return !(
        r1.right < r2.left + 8 ||
        r1.left > r2.right - 8 ||
        r1.bottom < r2.top + 8 ||
        r1.top > r2.bottom - 8
    );
}}


/* =========================
   MẤT MẠNG
========================= */

function loseLife() {{

    lives--;

    updateHUD();

    // hiệu ứng rung
    document.getElementById("game")
        .animate(
            [
                {{ transform: "translateX(-8px)" }},
                {{ transform: "translateX(8px)" }},
                {{ transform: "translateX(-5px)" }},
                {{ transform: "translateX(0)" }}
            ],
            {{
                duration: 250
            }}
        );

    if (lives <= 0) {{
        endGame();
    }}
}}


/* =========================
   GAME LOOP
========================= */

function gameLoop() {{

    if (!gameRunning) return;

    if (!paused) {{

        enemies.forEach((enemy, index) => {{

            let top =
                parseFloat(enemy.el.style.top);

            top += speed;

            enemy.el.style.top = top + "px";


            // Va chạm xe
            if (
                !enemy.hit &&
                collision(player, enemy.el)
            ) {{

                enemy.hit = true;

                enemy.el.remove();

                enemies.splice(index, 1);

                loseLife();

                return;
            }}


            // Đi qua xe -> cộng điểm
            if (
                !enemy.scored &&
                top > road.clientHeight
            ) {{

                enemy.scored = true;

                score++;

                updateHUD();

                enemy.el.remove();

                enemies.splice(index, 1);
            }}

        }});

        // Đụng rào chắn
        checkGuardrail();

    }}

    animationId =
        requestAnimationFrame(gameLoop);
}}


/* =========================
   RÀO CHẮN
========================= */

function checkGuardrail() {{

    const p =
        player.getBoundingClientRect();

    const r =
        road.getBoundingClientRect();

    const margin = 12;

    if (
        p.left <= r.left + margin ||
        p.right >= r.right - margin
    ) {{

        if (!player.guardHit) {{

            player.guardHit = true;

            loseLife();

            setTimeout(() => {{
                player.guardHit = false;
            }}, 800);
        }}

    }}
}}


/* =========================
   HUD
========================= */

function updateHUD() {{

    scoreText.innerText =
        "⭐ " + score;

    let hearts = "";

    for (let i = 0; i < 4; i++) {{
        hearts +=
            i < lives ? "❤️" : "🖤";
    }}

    livesText.innerText = hearts;
}}


/* =========================
   TẠM DỪNG
========================= */

function pauseGame() {{

    if (!gameRunning) return;

    paused = true;

    bgMusic.pause();

    document.getElementById("pauseMenu")
        .classList.remove("hidden");
}}


function resumeGame() {{

    paused = false;

    document.getElementById("pauseMenu")
        .classList.add("hidden");

    if (musicOn) {{
        bgMusic.play().catch(() => {{}});
    }}
}}


/* =========================
   THOÁT VỀ MENU
========================= */

function backToMenu() {{

    gameRunning = false;
    paused = false;

    clearTimeout(enemyTimer);

    stopMusic();

    enemies.forEach(e => e.el.remove());

    enemies = [];

    document.getElementById("pauseMenu")
        .classList.add("hidden");

    document.getElementById("gameOver")
        .classList.add("hidden");

    document.getElementById("hud")
        .classList.add("hidden");

    document.getElementById("controls")
        .classList.add("hidden");

    road.classList.add("hidden");

    document.getElementById("menu")
        .classList.remove("hidden");
}}


/* =========================
   GAME OVER
========================= */

function endGame() {{

    gameRunning = false;

    clearTimeout(enemyTimer);

    stopMusic();

    if (score > bestScore) {{

        bestScore = score;

        localStorage.setItem(
            "ngonLuaBestScore",
            bestScore
        );
    }}

    document.getElementById("finalScore").innerText =
        "⭐ Điểm: " + score +
        "\\n🏆 Kỷ lục: " + bestScore;

    document.getElementById("gameOver")
        .classList.remove("hidden");
}}


/* =========================
   CHƠI LẠI
========================= */

function restartGame() {{

    document.getElementById("gameOver")
        .classList.add("hidden");

    startGame();
}}

</script>

</body>
</html>
"""

components.html(
    game,
    height=800,
    scrolling=False
)
