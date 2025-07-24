//


const button2 = document.getElementById("button2")
const button3 = document.getElementById("button3")


button2.addEventListener("click", ()=>{
    document.documentElement.style.setProperty("--color", "#00007d")
})


button3.addEventListener("click", ()=>{
    document.documentElement.style.setProperty("--bkg-col", "#000000ff")
})