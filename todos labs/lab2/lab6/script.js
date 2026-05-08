const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');


const img = new Image();
img.src = 'pacman.png'; 
img.onload = () => {
    drawImageAtMousePosition(0, 0);
};

function drawImageAtMousePosition(x, y) {
    const imgWidth = 50;
    const imgHeight = 50;
    const posX = x - imgWidth / 2;
    const posY = y - imgHeight / 2;

    const maxX = canvas.width - imgWidth;
    const maxY = canvas.height - imgHeight;
    const constrainedX = Math.min(Math.max(0, posX), maxX);
    const constrainedY = Math.min(Math.max(0, posY), maxY);

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.drawImage(img, constrainedX, constrainedY, imgWidth, imgHeight);
}

canvas.addEventListener('mousemove', (event) => {
    const rect = canvas.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;
    drawImageAtMousePosition(mouseX, mouseY);
});


