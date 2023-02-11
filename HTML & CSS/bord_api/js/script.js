function getData(event) {

    event.preventDefault();
    const fd = new FormData(event.target)

    const but_send = document.getElementById('send_form')
    but_send.setAttribute('disabled', true)

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
        })

        // const pop = document.getElementById('pop_success')
        // pop.removeAttribute('class')
        // pop.setAttribute('class', 'alert alert-success alert-dismissible')})
      .catch((error) => console.error(error))


    document.getElementById('my_form').reset()

    // console.log(retVal)
  }



  function grayLable() {
    lab = document.getElementById('free_lab')

    console.log(lab.value)

    if (lab.style.color == 'black'){
      lab.style.color = 'rgb(188, 188, 188)'}
      else{lab.style.color = 'black'}
  }