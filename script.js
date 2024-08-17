let currentLetter = '';
let score = 0;
let lives = 3;
let timeLeft = 30;
let timer;

function startGame() {
    document.getElementById('start-screen').classList.add('hidden');
    document.getElementById('game-screen').classList.remove('hidden');
    score = 0;
    lives = 3;
    timeLeft = 30;
    updateDisplay();
    generateLetter();
    timer = setInterval(updateTime, 1000);
}

function generateLetter() {
    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    currentLetter = letters.charAt(Math.floor(Math.random() * letters.length));
    document.getElementById('letter').innerText = currentLetter;
}

function updateDisplay() {
    document.getElementById('score').innerText = `Score: ${score}`;
    document.getElementById('lives').innerText = `Lives: ${lives}`;
    document.getElementById('time').innerText = `Time: ${timeLeft}`;
}

function updateTime() {
    timeLeft--;
    if (timeLeft <= 0) {
        endGame();
    } else {
        document.getElementById('time').innerText = `Time: ${timeLeft}`;
    }
}

function endGame() {
    clearInterval(timer);
    alert(`Game Over! Final Score: ${score}`);
    document.getElementById('start-screen').classList.remove('hidden');
    document.getElementById('game-screen').classList.add('hidden');
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        startGame();
    } else if (event.key.toUpperCase() === currentLetter) {
        score++;
        generateLetter();
        updateDisplay();  // 점수 업데이트 후 화면 갱신
    } else {
        lives--;
        updateDisplay();  // 목숨 감소 후 화면 갱신
        if (lives <= 0) {
            endGame();
        }
    }
});

// 게임 시작 시점에서 스코어 초기화 및 화면 갱신
document.addEventListener('DOMContentLoaded', () => {
    updateDisplay(); // 초기 화면 갱신
});
