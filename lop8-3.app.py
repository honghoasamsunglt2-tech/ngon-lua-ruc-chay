stay-with-me.mp3
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
    background:
        radial-gradient(circle at center, #3b1500, #090909 65%);
}

.title {
    font-size: 42px;
    font-weight: 900;
    color: #ff8c00;
    text-shadow: 0 0 15px #ff4500;
    text-align: center;
}

.subtitle {
    margin-top: 5px;
    margin-bottom: 18px;
    color: #ffd27a;
    font-weight: bold;
}

.musicBox {
    display: flex;
    align-items: center;
    justify-content: center;
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

button {
    cursor: pointer;
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
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
    background:
        linear-gradient(#303030,#171717);
    clip-path: polygon(
        35% 0%,
        65% 0%,
        100% 100%,
        0% 100%
    );
}

.laneLine {
    position: absolute;
    top: 0;
    width: 4px;
    height: 100%;
    background: repeating-linear-gradient(
        to bottom,
        white 0px,
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
            onclick="setDifficulty('easy')">
            DỄ
        </button>

        <button id="medium"
            onclick="setDifficulty('medium')">
            VỪA
        </button>

        <button id="hard"
            onclick="setDifficulty('hard')">
            KHÓ
        </button>
    </div>

    <div>CHỌN XE</div>

    <div class="cars">
        <button id="red" class="selected"
            onclick="setCar('🚗')">
            🚗 ĐỎ COOL
        </button>

        <button id="pink"
            onclick="setCar('💗')">
            💗 HỒNG DỄ THƯƠ
