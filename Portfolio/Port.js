let home=()=>{
    let about=document.getElementById("home");
    about.scrollIntoView({behavior:"smooth"})
}
let home1=()=>{
    let about=document.getElementById("home");
    about.scrollIntoView({behavior:"smooth"})
}
let about=()=>{
    let about=document.getElementById("about");
    about.scrollIntoView({behavior:"smooth"})
}
let skill=()=>{
    let about=document.getElementById("skill");
    about.scrollIntoView({behavior:"smooth"})
}
let portfolio=()=>{
    let about=document.getElementById("portfolio");
    about.scrollIntoView({behavior:"smooth"})
}
let contact=()=>{
    let about=document.getElementById("contact");
    about.scrollIntoView({behavior:"smooth"})
}

let toggleMenu=()=>{
    document.body.classList.toggle("light-mode");
    let btn=document.getElementsByClassName('button');
    for(let btnEl of btn){
        btnEl.style.color="white"
        btnEl.style.border="white"
        btnEl.style.backgroundColor="transparent"
    }  
}