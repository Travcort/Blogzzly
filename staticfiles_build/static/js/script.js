document.addEventListener('DOMContentLoaded', function () {

    // Current Theme
    const currentTheme = localStorage.getItem('theme');

    // Apply the Default Browser theme
    if (currentTheme) {
        document.documentElement.classList.toggle('dark', currentTheme === 'dark');
    }

    // Theme Toggle
    const themeToggleButton = document.getElementById('theme-toggle');

    const toggleTheme = () => {
        const darkMode =  document.body.classList.toggle('dark');
        localStorage.setItem('theme', darkMode ? 'dark' : 'light');

        if (document.body.classList.contains('dark')) {
            themeToggleButton.textContent = '🔆';
        }
        else {
            themeToggleButton.textContent = '🌙';
        }
    }

    // Event delegation because of the drawer
    document.addEventListener('click', (event) => {
        if (event.target && event.target.id === 'theme-toggle') {
            toggleTheme();
        }
    });

    // Drawer
    const drawer = document.getElementById("drawer-navigation");
    const toggleButton = document.getElementById("drawer-toggle");
    const closeButton = document.getElementById("drawer-close");

    const toggleDrawer = () => {
        const isHidden = drawer.classList.contains('-translate-x-full');
        drawer.classList.toggle('-translate-x-full');
        toggleButton.setAttribute('aria-expande', !isHidden);
    }

    toggleButton.addEventListener('click', toggleDrawer); // Opening
    closeButton.addEventListener('click', toggleDrawer); // Closing

})