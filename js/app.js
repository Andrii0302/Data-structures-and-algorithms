document.addEventListener('DOMContentLoaded', function() {
    const restartButton = document.getElementById('restart-btn');
    restartButton.addEventListener('click', function() {
        restartGame();
    });

    // Function to handle key presses
    document.addEventListener('keydown', function(event) {
        if (gameOver) return; 

        let key = '';
        switch(event.key) {
            case 'ArrowUp':
                key = 'up';
                break;
            case 'ArrowDown':
                key = 'down';
                break;
            case 'ArrowLeft':
                key = 'left';
                break;
            case 'ArrowRight':
                key = 'right';
                break;
            default:
                // Ignore other keys
                return;
        }

        // Send key to server
        fetch('http://127.0.0.1:5000/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                key: key
            })
        }).then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        }).then(data => {
            if (data && data.matrix) {
                displayMatrixAsHtml(data.matrix);
                if (data.status === 'You won!' || data.status === 'LOST') {
                    gameOver = true;
                    alert(data.status === 'You won!' ? 'Congratulations! You won!' : 'Game Over! You lost!');
                }
            } else {
                console.error('Matrix data is missing');
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    });

    let gameOver = false;

    function restartGame() {
        fetch('http://127.0.0.1:5000/restart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(res => {
            if (res.ok) {
                return res.json();
            } else {
                throw new Error('Network response was not ok.');
            }
        }).then(data => {
            if (data && data.matrix) {
                displayMatrixAsHtml(data.matrix);
                gameOver = false; // Reset game over state
            } else {
                console.error('Matrix data is missing');
            }
        }).catch(error => {
            console.error('Error:', error);
        });
    }

    function displayMatrixAsHtml(matrix) {
        const table = document.getElementById('matrix');
        if (!table) {
            console.error('Table not found.');
            return;
        }

        while (table.firstChild) {
            table.removeChild(table.firstChild);
        }

        for (let i = 0; i < matrix.length; i++) {
            const row = document.createElement('tr');
            for (let j = 0; j < matrix[i].length; j++) {
                const cell = document.createElement('td');
                cell.textContent = matrix[i][j];
                row.appendChild(cell);
            }
            table.appendChild(row);
        }
    }
});
