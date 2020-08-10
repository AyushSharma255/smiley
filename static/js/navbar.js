const navBarBurger = document.querySelector("a.navbar-burger")

navBarBurger.addEventListener("click", () => {
    navBarBurger.classList.toggle("is-active")
    let navBar = document.querySelector("div.navbar-menu")
    navBar.classList.toggle("is-active")
})