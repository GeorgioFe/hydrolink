function toggleMenu() {
    const menu = document.getElementById('menu');
    const burger = document.getElementById('burger');
    if (menu && burger) {
        menu.classList.toggle('active');
        burger.classList.toggle('active');
    }
}