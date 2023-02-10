function textAppearance(){
    // document.getElementById('p_daetime').innerHTML = Date()
    // date = new Date()
    document.getElementById('p_daetime').innerHTML = new Date().toLocaleDateString('he-IS')
    // document.getElementById('p_daetime').innerHTML = `${date.getDate()}-${date.getMonth()}-${date.getfullYear()}`
    elem = document.getElementById('p_daetime')
    elem.style.display = 'flex'
    var today = moment(new Date())
    today = today.format("MMMM D, YYYY h:m A")
    // elem.style.padding = '100px'
    // elem.style.color = 'red'
    // date_now = new Date().toString().
    // document.getElementById('p_daetime').innerHTML = 'Hello'
}


// function formSubmitHandler(event) {
            
//     event.preventDefault();
    
//     console.log(event)
//     // form = document.getElementById('my-form')
//     console.log(event.target)
//     fd = new FormData(event.target)
//     const item = document.createElement("li")  //li
//     item.setAttribute('class', 'row')
//     item.style.alignItems = 'center'
//     item.style.marginBottom = '10px'

//     for (const pair of fd.entries()) {
//         console.log(pair)
        
//         if (pair[0] === 'product') {
//             const p = document.createElement("p")  //p
//             p.innerHTML = pair[1]
//             // const list = document.getElementById('products')
//             p.setAttribute('class', 'col')
//             p.style.margin = '0px'
//             item.appendChild(p)
//         }else{
//             if (pair[0] === 'qty'){
//                 const p2 = document.createElement("p") //p2
//                 p2.innerHTML = pair[1]
//                 // const list = document.getElementById('products')
//                 p2.setAttribute('class', 'col')
//                 p2.setAttribute('id', 'qty_id')
//                 p2.style.margin = '0px'
//                 item.appendChild(p2)
//             }

//         }
//         // document.getElementById('my_form').form.reset()
//     }
//     const button_div = document.createElement('div')
//     button_div.setAttribute('class', 'btn-group-vertical')
//     button_div.style.width = 'auto'

//     const plas_button = document.createElement('button')
//     plas_button.setAttribute('class', 'btn btn-outline-secondary')
//     plas_button.setAttribute('type', 'button')
//     plas_button.innerHTML = '+'
//     plas_button.onclick = () => {bu = document.getElementById('qty_id').value;
//                                 document.getElementById('qty_id').innerHTML = bu + 1;}

//     const minus_button = document.createElement('button')
//     minus_button.setAttribute('class', 'btn btn-outline-secondary')
//     minus_button.setAttribute('type', 'button')
//     minus_button.innerHTML = '-'

//     button_div.appendChild(plas_button)
//     button_div.appendChild(minus_button)
//     item.appendChild(button_div)


//     const del = document.createElement('button')
//     del.innerHTML = 'X'
//     del.onclick = (event) => event.target.parentElement.remove()
//     del.setAttribute('class', 'col-sm-3 col_button btn btn-outline-secondary')
//     item.appendChild(del)
//     const list = document.getElementById('products')
//     list.appendChild(item)

//     document.getElementById('my_form').reset()
// }


// function deleteRow(event) {
//     event.target.parentElement.remove()
// }





// <div class="btn-group-vertical" style="width: auto;">
{/* <button type="button" class="btn btn-outline-secondary">+</button>
<button type="button" class="btn btn-outline-secondary">-</button>
</div> */}


function formSubmitHandler(event) {
            
    event.preventDefault();
    
    console.log(event)
    // form = document.getElementById('my-form')
    console.log(event.target)
    fd = new FormData(event.target)
    const item = document.createElement("li")  //li
    item.setAttribute('class', 'row')
    item.style.alignItems = 'center'
    item.style.marginBottom = '10px'

    for (const pair of fd.entries()) {
        console.log(pair)
        
        if (pair[0] === 'product') {
            const p = document.createElement("p")  //p
            p.innerHTML = pair[1]
            // const list = document.getElementById('products')
            p.setAttribute('class', 'col')
            p.style.margin = '0px'
            item.appendChild(p)
        }else{
            if (pair[0] === 'qty'){
                const p2 = document.createElement("span") //p2
                p2.innerHTML = pair[1]
                // const list = document.getElementById('products')
                p2.setAttribute('class', 'col')
                p2.setAttribute('id', 'qty_id')
                p2.style.margin = '0px'
                item.appendChild(p2)
            }

        }
        // document.getElementById('my_form').form.reset()
    }
    const button_div = document.createElement('div')
    button_div.setAttribute('class', 'btn-group-vertical')
    button_div.style.width = 'auto'

    const plas_button = document.createElement('button')
    plas_button.setAttribute('class', 'btn btn-outline-secondary')
    plas_button.setAttribute('type', 'button')
    plas_button.innerHTML = '+'
    // plas_button.onclick = () => {const a = document.getElementById('p_bu')
    // document.getElementById('p_bu').innerHTML++}
    plas_button.setAttribute('onclick', 'plus(this)')

    const minus_button = document.createElement('button')
    minus_button.setAttribute('class', 'btn btn-outline-secondary')
    minus_button.setAttribute('type', 'button')
    minus_button.innerHTML = '-'
    minus_button.setAttribute('onclick', 'minus(this)')

    button_div.appendChild(plas_button)
    button_div.appendChild(minus_button)
    item.appendChild(button_div)


    const del = document.createElement('button')
    del.innerHTML = 'X'
    del.onclick = (event) => event.target.parentElement.remove()
    del.setAttribute('class', 'col-sm-3 col_button btn btn-outline-secondary')
    item.appendChild(del)
    const list = document.getElementById('products')
    list.appendChild(item)

    document.getElementById('my_form').reset()
}


function plus(butn) {
    const parent_item = butn.parentNode.parentNode;
    qty = parent_item.querySelector("span")
    qty.innerHTML++
}

function minus(butn) {
    const parent_item = butn.parentNode.parentNode;
    qty = parent_item.querySelector("span")
    if (qty.innerHTML == 1){
        parent_item.remove()
    } else{
        qty.innerHTML--
    }
        
}

