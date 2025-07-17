//



const darkModeBtn = document.documentElement("darkModeBtn")
const lightModeBtn = document.documentElement("lightModeBtn")


darkModeBtn.addEventListener("click", ()=> {
    document.documentElement.style.setProperty("--d-background-color", "#black")
})


lightModeBtn.addEventListener("click", ()=> {
    document.documentElement.style.setProperty("--d-background-color", "#white")
})
