from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shreya Birthday Surprise</title>

    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body {
            margin: 0;
            overflow: hidden;
            font-family: Arial, sans-serif;
            background: black;
            color: white;
        }

        .slide {
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 40px;
            transition: opacity 0.5s ease;
        }

        .hidden-slide {
            opacity: 0;
            pointer-events: none;
        }

        .glass {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255,255,255,0.2);
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: blink 3s infinite;
        }

        @keyframes blink {
            0% { opacity: 0.2; }
            50% { opacity: 1; }
            100% { opacity: 0.2; }
        }

        .arrow-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 70px;
            height: 70px;
            border-radius: 50%;
            border: 1px solid rgba(255,255,255,0.2);
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(20px);
            color: white;
            font-size: 30px;
            cursor: pointer;
            transition: 0.3s;
        }

        .arrow-btn:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-50%) scale(1.1);
        }

        .left-btn {
            left: 25px;
        }

        .right-btn {
            right: 25px;
        }

        .dots {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
            padding: 10px 20px;
            border-radius: 50px;
            background: rgba(0,0,0,0.2);
            backdrop-filter: blur(10px);
        }

        .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: rgba(255,255,255,0.4);
        }

        .active-dot {
            width: 35px;
            border-radius: 50px;
            background: hotpink;
        }
    </style>
</head>
<body>

<div id="stars"></div>

<div id="lockScreen" class="w-screen h-screen flex items-center justify-center relative z-10">
    <div class="glass rounded-3xl p-10 w-[400px] text-center shadow-2xl">
        <h1 class="text-5xl font-bold mb-6 text-pink-400">
            🔐 Birthday Vault
        </h1>

        <p class="text-gray-300 mb-4">
            Enter the secret password
        </p>

        <div class="glass rounded-2xl p-4 mb-5">
            🔍 Hint: It's the birthday girl's name
        </div>

        <input
            id="passwordInput"
            type="password"
            placeholder="Enter Password"
            class="w-full p-4 rounded-2xl bg-black/30 border border-white/20 outline-none mb-4"
        >

        <button
            onclick="checkPassword()"
            class="w-full p-4 rounded-2xl bg-gradient-to-r from-pink-500 to-purple-600 text-xl font-bold"
        >
            Unlock Surprise ✨
        </button>

        <p id="errorText" class="text-red-400 mt-4 hidden">
            Wrong Password!
        </p>
    </div>
</div>

<div id="slider" class="hidden">

    <div class="slide bg-gradient-to-br from-pink-500 via-purple-500 to-indigo-500">
        <div class="text-8xl mb-8">🎂</div>
        <h1 class="text-7xl font-bold mb-6">🎉 Happy Birthday Shreya 🎉</h1>
        <p class="text-2xl max-w-4xl">
            Today is all about you! Hope your day is filled with happiness and unforgettable memories.
        </p>
    </div>

    <div class="slide hidden-slide bg-gradient-to-br from-purple-600 via-fuchsia-500 to-pink-500">
        <div class="text-8xl mb-8">💖</div>
        <h1 class="text-7xl font-bold mb-6">✨ Special Message ✨</h1>
        <p class="text-2xl max-w-4xl">
            You are one of the most amazing people ever. Keep smiling and shining always.
        </p>
    </div>

    <div class="slide hidden-slide bg-gradient-to-br from-indigo-600 via-blue-500 to-cyan-400">
        <div class="text-8xl mb-8">🏆</div>
        <h1 class="text-7xl font-bold mb-6">🎮 Birthday Quest Complete 🎮</h1>
        <p class="text-2xl max-w-4xl">
            Congratulations! You unlocked the secret birthday world.
        </p>
    </div>

    <div class="slide hidden-slide bg-gradient-to-br from-rose-500 via-orange-400 to-yellow-300">
        <div class="text-8xl mb-8">🎁</div>
        <h1 class="text-7xl font-bold mb-6">🌸 Final Surprise 🌸</h1>
        <p class="text-2xl max-w-4xl">
            May every dream you have turn into reality. Have the best birthday ever!
        </p>
    </div>

    <button class="arrow-btn left-btn" onclick="prevSlide()">❮</button>
    <button class="arrow-btn right-btn" onclick="nextSlide()">❯</button>

    <div class="dots" id="dots"></div>
</div>

<script>
    const password = 'shreya';

    function checkPassword() {
        const input = document.getElementById('passwordInput').value.toLowerCase();

        if (input === password) {
            document.getElementById('lockScreen').style.display = 'none';
            document.getElementById('slider').classList.remove('hidden');
        } else {
            document.getElementById('errorText').classList.remove('hidden');
        }
    }

    const slides = document.querySelectorAll('.slide');
    const dotsContainer = document.getElementById('dots');

    let currentSlide = 0;

    function updateSlides() {
        slides.forEach((slide, index) => {
            slide.classList.toggle('hidden-slide', index !== currentSlide);
        });

        dotsContainer.innerHTML = '';

        slides.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('dot');

            if (index === currentSlide) {
                dot.classList.add('active-dot');
            }

            dotsContainer.appendChild(dot);
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        updateSlides();
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        updateSlides();
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') {
            nextSlide();
        }

        if (e.key === 'ArrowLeft') {
            prevSlide();
        }
    });

    updateSlides();

    // Stars Background
    const starsContainer = document.getElementById('stars');

    for (let i = 0; i < 70; i++) {
        const star = document.createElement('div');
        star.classList.add('star');

        const size = Math.random() * 4;

        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 3}s`;

        starsContainer.appendChild(star);
    }
</script>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
