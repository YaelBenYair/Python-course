
window.onload = () => {
    let current_second = localStorage.getItem('current')
    if (current_second > 0) {
        // alert(`You have an incomplete countdown timer that has been started on ${localStorage.getItem('pretty-current-time')}`)
        startTimer(parseInt(current_second))
    }
}



function startTimer(event) {
    if (typeof event === 'number') {
        console.log(event)
        ti1 = localStorage.getItem('current-time')
        ti = new Date().getTime() / 1000
        console.log(parseInt((ti - ti1) / 1000))
        t = (ti - ti1) / 1000
        t = Math.ceil(t)
        console.log(t)
        second = event - t
        console.log(second)
        event = document.getElementById('but-ton')
    }else{
        event = document.getElementById('but-ton')
        second = document.getElementById('second-input').value
    }
    locStorage = second
    localStorage.setItem('current', locStorage)

    // let current_second = 

    console.log('seting timer for', second)
    // document.getElementById('counter').innerText = second

    event.setAttribute('disabled', true)
    document.getElementById("counter").innerHTML = second
    const d = new Date();
    document.getElementById("time-counter").innerHTML = d.toLocaleTimeString()
    // document.getElementById("time-counter").innerHTML = d.toLocaleString()
    localStorage.setItem('current-time', new Date().getTime() / 1000)
    localStorage.setItem('pretty-current-time', d.toLocaleTimeString())

    myTimer = setInterval(() => {
        const d = new Date();
        // document.getElementById("time-counter").innerHTML = new Date().toLocaleDateString('he-IS')
        document.getElementById("time-counter").innerHTML = d.toLocaleTimeString();
        document.getElementById("counter").innerHTML--;
        locStorage--
        localStorage.setItem('current', locStorage)

    }, 1000)
    setTimeout(() => {
        event.removeAttribute('disabled')
        document.getElementById('second-input').value = ""
        clearInterval(myTimer)}, second * 1000)
        
}


function onEnter(event) {
    console.log(event.keyCode)
    // alert("You pressed a key inside the input field")
    if (event.keyCode == 13) {
        startTimer(document.getElementById('but-ton'))
    }
    
}