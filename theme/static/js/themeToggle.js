const themeToggleButton = document.getElementById('theme-toggle');

const toggle = () => {
    document.body.classList.toggle('dark');

    if (document.body.classList.contains('dark')) {
        themeToggleButton.textContent = '🔆'
    }
    else {
    themeToggleButton.textContent = '🌙'; // Sun icon for light mode
  }
}

themeToggleButton.addEventListener('click', toggle);