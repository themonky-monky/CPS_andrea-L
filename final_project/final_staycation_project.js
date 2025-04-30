 // JavaScript to toggle the visibility of additional content
        function toggleContent() {
            const content = document.getElementById('extra-content');
            if (content.style.display === 'none') {
                content.style.display = 'block';
            } else {
                content.style.display = 'none';
            }
        }
