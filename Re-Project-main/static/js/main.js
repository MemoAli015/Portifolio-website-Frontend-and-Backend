document.addEventListener('DOMContentLoaded', () => {
    const icon = document.getElementById('side-bar-icon');
    const spans = [
        document.getElementById('span1'),
        document.getElementById('spanid2'),
        document.getElementById('span3')
    ];

    icon.addEventListener('click', () => {
        spans.forEach(span => {
            span.style.display = 'none';
        });
    });
});
