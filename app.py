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

body{
    margin:0;
    overflow:hidden;
    font-family:Arial,sans-serif;
    background:black;
    color:white;
}

.slide{
    position:absolute;
    inset:0;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:40px;
    transition:opacity 0.6s ease;
}

.hidden-slide{
    opacity:0;
    pointer-events:none;
}

.glass{
    background:rgba(255,255,255,0.1);
    backdrop-filter:blur(20px);
    border:1px solid rgba(255,255,255,0.2);
}

.star{
    position:absolute;
    background:white;
    border-radius:50%;
    animation:blink 3s infinite;
}

@keyframes blink{
    0%{opacity:0.2;}
    50%{opacity:1;}
    100%{opacity:0.2;}
}

.arrow-btn{
    position:absolute;
    top:50%;
    transform:translateY(-50%);
    width:80px;
    height:80px;
    border-radius:50%;
    border:1px solid rgba(255,255,255,0.2);
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(20px);
    color:white;
    font-size:35px;
    cursor:pointer;
    transition:0.3s;
    z-index:100;
}

.arrow-btn:hover{
    background:rgba(255,255,255,0.2);
    transform:translateY(-50%) scale(1.1);
}

.left-btn{
    left:30px;
}

.right-btn{
    right:30px;
}

.dots{
    position:absolute;
    bottom:35px;
    left:50%;
    transform:translateX(-50%);
    display:flex;
    gap:10px;
    padding:12px 20px;
    border-radius:999px;
    background:rgba(0,0,0,0.2);
    backdrop-filter:blur(10px);
}

.dot{
    width:12px;
    height:12px;
    border-radius:50%;
    background:rgba(255,255,255,0.4);
    transition:0.3s;
}

.active-dot{
    width:40px;
    border-radius:999px;
    background:hotpink;
}

</style>

</head>

<body>

<div id="stars"></div>

<!-- PASSWORD SCREEN -->

<div id="lockScreen"
class="w-screen h-screen flex items-center justify-center relative z-10">

<div class="glass rounded-3xl p-10 w-[420px] text-center shadow-2xl">

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

<!-- MAIN SLIDER -->

<div id="slider" class="hidden">

<div class="slide bg-gradient-to-br from-pink-500 via-purple-500 to-indigo-500">

<div class="text-8xl mb-8">🎂</div>

<h1 class="text-7xl font-bold mb-6">
🎉 Happy Birthday Shreya 🎉
</h1>

<p class="text-2xl max-w-4xl">
Today was the day on which you were born, everybody in your family doesn't supports you but don't you worry as I am always with you to help you in every possible way as i can. You are the best thing that have haappend to me as you have heard my stupd jokes and also you have held me in my bad time so a big thanks to you.
</p>

</div>

<div class="slide hidden-slide bg-gradient-to-br from-purple-600 via-fuchsia-500 to-pink-500">

<div class="text-8xl mb-8">💖</div>

<h1 class="text-7xl font-bold mb-6">
✨ Special Message ✨
</h1>

<p class="text-2xl max-w-4xl">
You are one of the most gorgeous person i have met. And i don't want you to make yourself feel like you don't have aa place to be feel free always remember that I am with you and you can share everything with me. Not everone is going to support you but celebrate your bday by yourself.
</p>

</div>

<div class="slide hidden-slide bg-gradient-to-br from-indigo-600 via-blue-500 to-cyan-400">

<div class="text-8xl mb-8">🏆</div>

<h1 class="text-7xl font-bold mb-6">
🎮 Birthday Quest Complete 🎮
</h1>

<p class="text-2xl max-w-4xl">
Congratulations! You unlocked the secret birthday world. You have to make you day as good as possible and have to tell me what have you done on the beautiful day.
</p>

</div>

<div class="slide hidden-slide bg-gradient-to-br from-rose-500 via-orange-400 to-yellow-300">

<div class="text-8xl mb-8">🎁</div>

<h1 class="text-7xl font-bold mb-6">
🌸 Final Surprise 🌸
</h1>

<p class="text-2xl max-w-4xl">
God May turn every dream your into reality. Have the best birthday ever!
</p>

</div>

<button class="arrow-btn left-btn" onclick="prevSlide()">
❮
</button>

<button class="arrow-btn right-btn" onclick="nextSlide()">
❯
</button>

<div class="dots" id="dots"></div>

</div>

<script>

const password = 'shreya';

const originalSlider =
document.getElementById('slider').innerHTML;

let tapCount = 0;

function checkPassword(){

const input =
document.getElementById('passwordInput')
.value
.toLowerCase();

if(input === password){

document.getElementById('lockScreen').style.display='none';

document.getElementById('slider').classList.remove('hidden');

document.getElementById('slider').innerHTML = `

<div class="absolute inset-0 overflow-hidden bg-gradient-to-br from-pink-500 via-fuchsia-500 to-purple-700">

<!-- Glow Effects -->

<div class="absolute -top-40 -left-40 w-[700px] h-[700px] bg-yellow-300/30 rounded-full blur-[180px] animate-pulse"></div>

<div class="absolute bottom-0 right-0 w-[800px] h-[800px] bg-pink-300/20 rounded-full blur-[200px] animate-pulse"></div>

<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[900px] h-[900px] bg-white/10 rounded-full blur-[250px]"></div>

<!-- Floating Emojis -->

<div class="absolute top-20 left-20 text-6xl animate-bounce">
🎈
</div>

<div class="absolute top-40 right-32 text-7xl animate-pulse">
🎂
</div>

<div class="absolute bottom-32 left-40 text-6xl animate-bounce">
🎊
</div>

<div class="absolute bottom-20 right-20 text-7xl animate-pulse">
✨
</div>

<!-- Main Content -->

<div id="giftScene"
class="absolute inset-0 flex flex-col items-center justify-center z-10 text-center px-10">

<h1
class="text-8xl font-black leading-none bg-gradient-to-r from-yellow-200 via-white to-pink-200 bg-clip-text text-transparent">

Your Surprise Awaits

</h1>

<p
class="mt-8 text-2xl tracking-[6px] uppercase text-white/80">

Tap The Gift To Unlock

</p>

<!-- Gift -->

<div class="relative mt-20">

<div class="absolute inset-0 rounded-full bg-pink-500/40 blur-[120px] animate-pulse"></div>

<div
id="giftBox"
onclick="tapGift()"
class="relative text-[300px] cursor-pointer select-none transition-all duration-300 hover:scale-110 active:scale-95">

🎁

</div>

</div>

<!-- Progress -->

<div class="mt-20 w-[500px]">

<div
class="h-3 rounded-full overflow-hidden bg-white/10 border border-white/10">

<div
id="progressBar"
class="h-full rounded-full bg-gradient-to-r from-yellow-300 via-pink-400 to-purple-500 transition-all duration-300"
style="width:0%">
</div>

</div>

<p
id="tapCounter"
class="mt-6 text-center text-xl tracking-[4px] text-white/80 uppercase">

Energy Building...

</p>

</div>

</div>

</div>

`;

}

else{

document.getElementById('errorText')
.classList.remove('hidden');

}

}

function tapGift(){

tapCount++;

const gift =
document.getElementById('giftBox');

const progress =
document.getElementById('progressBar');

const counter =
document.getElementById('tapCounter');

progress.style.width =
`${tapCount * 5}%`;

gift.style.transform =
`scale(${1 + tapCount * 0.02}) rotate(${Math.sin(tapCount) * 10}deg)`;

counter.innerText =
`Power Level : ${tapCount * 5}%`;

if(tapCount > 20){

document.getElementById('giftScene').innerHTML = `

<div class="absolute inset-0 overflow-hidden">

<!-- Fireworks -->
<div id="crackerContainer"></div>

<!-- Main Content -->

<div class="absolute inset-0 flex flex-col items-center justify-center z-10 text-center px-10">

<!-- Big Emoji -->

<div
class="text-[260px] animate-bounce drop-shadow-[0_0_120px_rgba(255,255,255,0.9)]">

🎉

</div>

<!-- Title -->

<h1
class="mt-4 text-8xl font-black leading-none bg-gradient-to-r from-yellow-200 via-white to-pink-200 bg-clip-text text-transparent">

Happy Birthday

</h1>

<h2
class="mt-4 text-7xl font-black tracking-[8px] uppercase text-white">

Shreya

</h2>

<!-- Subtitle -->

<p
class="mt-10 text-2xl tracking-[6px] uppercase text-white/80">

Your Premium Birthday Experience Is Ready

</p>

<!-- Button -->

<button
onclick="startSlides()"
class="group relative overflow-hidden mt-16 rounded-full px-16 py-7 text-2xl font-bold uppercase tracking-[6px] text-white transition-all duration-500 hover:scale-110">

<span
class="absolute inset-0 bg-gradient-to-r from-yellow-300 via-pink-400 to-purple-500">
</span>

<span
class="absolute inset-0 blur-2xl opacity-60 bg-gradient-to-r from-yellow-300 via-pink-400 to-purple-500">
</span>

<span class="relative z-10">
Enter Birthday World ✨
</span>

</button>

</div>

</div>

`;

createFireworks();

}

}

function createFireworks(){

const container =
document.getElementById('crackerContainer');

for(let i=0;i<120;i++){

const cracker =
document.createElement('div');

cracker.style.position='absolute';

cracker.style.width='10px';

cracker.style.height='10px';

cracker.style.borderRadius='50%';

cracker.style.background =
`hsl(${Math.random()*360},100%,50%)`;

cracker.style.left='50%';

cracker.style.top='50%';

const x =
(Math.random()-0.5)*3000;

const y =
(Math.random()-0.5)*3000;

cracker.animate([
{
transform:'translate(0,0)',
opacity:1
},
{
transform:`translate(${x}px,${y}px)`,
opacity:0
}
],{
duration:3000,
easing:'ease-out'
});

container.appendChild(cracker);

}

}

function startSlides(){

document.getElementById('slider').innerHTML =
originalSlider;

updateSlides();

}

let currentSlide = 0;

function updateSlides(){

const slides =
document.querySelectorAll('.slide');

slides.forEach((slide,index)=>{

slide.classList.toggle(
'hidden-slide',
index !== currentSlide
);

});

const dotsContainer =
document.getElementById('dots');

dotsContainer.innerHTML='';

slides.forEach((_,index)=>{

const dot =
document.createElement('div');

dot.classList.add('dot');

if(index === currentSlide){

dot.classList.add('active-dot');

}

dotsContainer.appendChild(dot);

});

}

function nextSlide(){

const slides =
document.querySelectorAll('.slide');

currentSlide =
(currentSlide + 1) % slides.length;

updateSlides();

}

function prevSlide(){

const slides =
document.querySelectorAll('.slide');

currentSlide =
(currentSlide - 1 + slides.length) % slides.length;

updateSlides();

}

document.addEventListener('keydown',(e)=>{

if(e.key === 'ArrowRight'){

nextSlide();

}

if(e.key === 'ArrowLeft'){

prevSlide();

}

});

updateSlides();

const starsContainer =
document.getElementById('stars');

for(let i=0;i<80;i++){

const star =
document.createElement('div');

star.classList.add('star');

const size =
Math.random()*4;

star.style.width=`${size}px`;

star.style.height=`${size}px`;

star.style.left=`${Math.random()*100}%`;

star.style.top=`${Math.random()*100}%`;

star.style.animationDelay=
`${Math.random()*3}s`;

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