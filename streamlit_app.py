import streamlit as st
import streamlit.components.v1 as components

# Page Config
st.set_page_config(page_title="Bala Appreciation Station", page_icon="👑")

# The "Engine" - HTML/JS/CSS
bala_app_html = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Bungee&display=swap');
        body {
            background: #0e1117;
            color: white;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            padding: 20px;
        }
        h1 { font-family: 'Bungee', cursive; color: #ff4b4b; font-size: 2.5rem; text-shadow: 2px 2px #000; }
        .btn-container { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; max-width: 400px; margin: 0 auto; }
        button {
            padding: 15px; border-radius: 10px; border: none; cursor: pointer;
            background: #262730; color: white; font-size: 1.2rem; transition: 0.2s;
        }
        button:hover { background: #3e404e; transform: scale(1.05); }
        .legendary {
            grid-column: span 2;
            background: linear-gradient(45deg, #ff4b4b, #ff7e5f);
            font-weight: bold; margin-top: 10px;
        }
        #score-box { font-size: 1.5rem; margin: 20px 0; color: #f0f2f6; }
    </style>
</head>
<body>
    <h1>👑 BALA 👑</h1>
    <div id="score-box">Appreciation Level: <span id="val">0</span></div>
    
    <div class="btn-container">
        <button onclick="cheer('👏', 1)">👏 Clap</button>
        <button onclick="cheer('🔥', 5)">🔥 Lit</button>
        <button onclick="cheer('🙌', 10)">🙌 Respect</button>
        <button onclick="cheer('💎', 20)">💎 GOAT</button>
        <button class="legendary" onclick="legendary()">📣 LEGENDARY CHEER 📣</button>
    </div>

    <script>
        let score = 0;
        const cheerAudio = new Audio('https://www.myinstants.com/media/sounds/cheer.mp3');

        function cheer(emoji, pts) {
            score += pts;
            document.getElementById('val').innerText = score;
            confetti({ particleCount: 15, spread: 50, origin: { y: 0.8 }, colors: ['#ff4b4b'] });
        }

        function legendary() {
            score += 1000;
            document.getElementById('val').innerText = score;
            cheerAudio.play();
            confetti({ particleCount: 200, spread: 100, origin: { y: 0.6 } });
        }
    </script>
</body>
</html>
"""

# Streamlit UI
st.title("The Official Bala Hype Machine")
st.write("Click the buttons below to send Bala some well-deserved appreciation.")

# Inject the HTML App
components.html(bala_app_html, height=500)

st.divider()
st.info("Pro-tip: Keep clicking the Legendary button until the neighbors complain about the cheering.")