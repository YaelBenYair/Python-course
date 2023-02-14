function getData(event) {

    event.preventDefault();
    const fd = new FormData(event.target)

    const but_send = document.getElementById('send_form')
    but_send.setAttribute('disabled', true)
    but_send.innerText = 'Loading..'
    // const span_a = document.getElementById('spiner-span')
    // span_a.removeAttribute('class')
    // span_a.setAttribute('class', 'spinner-border spinner-border-sm')
    const span_a = document.createElement('span')
    span_a.setAttribute('class', 'spinner-border spinner-border-sm')
    but_send.appendChild(span_a)

    let count = 0
    
    const queryParam = {}

    for (const pair of fd.entries()) {
      count++
      if (pair[0] === 'participants'){
        if (pair[1] == 0){
          pair.remove
          count--
      }else{
        queryParam.participants = pair[1]
      }
    }
      if (pair[0] === 'price') {
        if (pair[1] === 'yes') {
          queryParam.price = 0
          
        }else{
          queryParam.price = 1
        }
      }  

      if (pair[0] === 'type') {
        queryParam.type = pair[1]
      }

    }
    if (count === 0) {
      mark = '/'
    }else{
      mark = '?'
    }
    console.log(mark)
    console.log(queryParam)

    fetch("https://www.boredapi.com/api/activity" + mark + new URLSearchParams(queryParam))
      .then((response) => response.json())
      .then((json) => {
        console.log(json)

        but_send.removeAttribute('disabled')
        but_send.innerText = 'Send'
        // span_a.removeAttribute('class')
        // span_a.setAttribute('class', 'spinner-border spinner-border-sm invisible')

        if (json.error == undefined){

          p1 = document.getElementById('p_1')
          p1.innerHTML = ''
          p1.removeAttribute('class')

          ul = document.getElementById('activity_list')

          const con = document.createElement('li')
          con.setAttribute('class', 'row')
          con.innerHTML = json.activity
          con.style.marginBottom = '10px'
          con.style.borderBottom = '2px solid #f2eeeb'

          const p = document.createElement('p')
          p.setAttribute('class', 'col')

          const but = document.createElement('button')
          but.setAttribute('class', 'col-sm-3 col_button btn btn-outline-secondary')
          but.innerHTML = 'X'
          but.style.width = 'auto'
          but.style.border = 'none'

          but.onclick = (event) => event.target.parentElement.remove()

          con.appendChild(p)
          con.appendChild(but)
          ul.appendChild(con)
        }else{
          p1 = document.getElementById('p_1')
          p1.innerHTML = json.error
          p1.setAttribute('class', 'mx-auto shadow-sm p-4 mb-4 bg-white container-sm border')
          p1.style.color = 'red'
        }
        })

        // const pop = document.getElementById('pop_success')
        // pop.removeAttribute('class')
        // pop.setAttribute('class', 'alert alert-success alert-dismissible')})
      .catch((error) => console.error(error))


    document.getElementById('my_form').reset()
    document.getElementById('rangeval').innerHTML = 0

    // console.log(retVal)
  }



  function grayLable() {
    lab = document.getElementById('free_lab')

    console.log(lab.value)

    if (lab.style.color == 'black'){
      lab.style.color = 'rgb(188, 188, 188)'}
      else{lab.style.color = 'black'}
  }