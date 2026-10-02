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

#game {
    width: 100%;
    max-width: 900px;
    height: 850px;
    margin: auto;
    position: relative;
    overflow: hidden;
    background: linear-gradient(#151515, #080808);
}

/* MENU */
#menu {
    position: absolute;
    inset: 0;
    z-index: 50;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background:
        radial-gradient(circle at center, #421000 0%, #160700 45%, #050505 100%);
}

.title {
    font-size: 46px;
    font-weight: bold;
    color: #ff6a00;
    text-shadow:
        0 0 10px #ff3300,
        0 0 25px #ff6600,
        0 0 45px #ff2200;
    text-align: center;
    margin-bottom: 12px;
}

.subtitle {
    font-size: 18px;
    color: #ffd9a8;
    margin-bottom: 35px;
}

.menuButton {
    width: 250px;
    padding: 16px;
    margin: 8px;
    border: none;
    border-radius: 14px;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
    background: linear-gradient(135deg, #ff2d00, #ff8a00);
    color: white;
    box-shadow: 0 5px 18px #ff3c0066;
}

.menuButton:hover {
    transform: scale(1.04);
}

/* ROAD */
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
    animation: roadMove linear
