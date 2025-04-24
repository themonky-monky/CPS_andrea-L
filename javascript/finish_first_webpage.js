let image = ["https://www.earth.com/assets/_next/image/?url=https%3A%2F%2Fcff2.earth.com%2Fuploads%2F2023%2F06%2F02100547%2FMountain-2-1400x850.jpg&w=1200&q=75"]
function hello() {
    let name = window.prompt("What is your name?", "mountain")
    document.getElementById("title").innerHTML = "Hello World!" + name + "!"
}
let count = 0
function change() {
    document.getElementById("img").src = image[count]
    if (count === 2) {
        count = 0
    } else {
        count += 1
    }
}
function highlight() {
    document.getElementById("btn").style.backgroundColor = "pink"
    document.getElementById("title").style.color = "purple"
}
function normal() {
    document.getElementById("btn").style.backgroundColor = "green"
    document.getElementById("title").style.color = "grey"
}
function push() {
    document.getElementById("btn").style.backgroundColor = "red"
    document.getElementById("title").style.color = "orange"
}
function unhighlight() {
    document.getElementById("btn").style.backgroundColor = "black"
    document.getElementById("title").style.color = "white"
}
function changeColor() {
    document.getElementById("title").style.color = "yellow"
    document.getElementById("title").style.backgroundColor = "black"
}
function show() {
    document.getElementById("hidden").style.display = "block"
}
function pop() {
    window.alert("for real. Don't click this!")
}
function more() {
    if (document.getElementById("extra").style.display != "flex") {
        document.getElementById("extra").style.display = "flex"
        document.getElementById("shw").innerHTML = "show less"
    } else {
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML = "show more"
    }
}