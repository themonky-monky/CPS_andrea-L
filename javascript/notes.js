let images = ["https://static01.nyt.com/images/2024/11/26/multimedia/moana2-1-zlqt/moana2-1-zlqt-mediumSquareAt3X.jpg"
    ]
function hello(){
    let name = window.prompt("What is your name?", "Koro sensei")
    document.getElementById("title").innerHTML = "Hello World!"
    + name + "!"
}

count = 0
function change(){
    document.getElementById("img").src = image [count]
    if(count === 2) {
        count = 0
    }else{
        count +=1
    }
}

function highlight(){
    document.getElementById("btn").style.backgroundColor = "orange"
    document.getElementById("title").style.color = "black"
}

function normal(){
    document.getElementById("btn").style.backgroundColor = "gray"
    document.getElementById("title").style.color = "black"
}

function push(){
    document.getElementById("btn").style.backgroundColor = "green"
    document.getElementById("title").style.color = "black"
}

function
unhighlight(){
    document.getElementById("btn").style.backgroundColor = "white"
    document.getElementById("title").style.color = "white"
}

function 
changeColor(){
    document.getElementById("title").style.color = "red"
    document.getElementById("title").style.backgroundColor = "black"
}

function show(){
    document.getElementById("hidden").style.display = "block"
}

function pop(){
    window.alert("for real. Don't click this!")
}

function more(){
    if(document.getElementById("extra").style.display != "flex"){
    ducument.getElementById("extra").style.display = "flex"
    document.getElementById("shw").innerHTML = "show less"
 }else{
        document.getElementById("extra").style.display = "none"
        document.getElementById("shw").innerHTML = "show more"
    }
}