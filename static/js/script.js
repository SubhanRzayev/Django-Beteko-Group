
let form = document.getElementById('subscribe-form');

let error_section = document.getElementById('error-list');

form.addEventListener('submit',async function (e) {
    e.preventDefault();
    error_section.innerText = '';
    let form_data = {
        'email': form.email.value
    }
    let response = await fetch('https://beteko.az/api/subscribe/',{
        headers: {
            'content-type': 'application/json',
            "X-CSRFToken" : form.csrfmiddlewaretoken.value
        },
        method: "POST",
        body: JSON.stringify(form_data)
        
    })
    let response_data = await response.json();
    let status = await response.ok;
    if (status==true){
        alert('Ugurla obene oldunuz');
    }
    else{
        for(let error of response_data.email){
            error_section.innerHTML += `<li class="text-danger">${error}</li>`
        }
    }
    
})
    

    $(document).ready(function() {
    $(".dropdown-item").click(function () {
        $(".dropdown-item").removeClass("active");
        // $(".tab").addClass("active"); // instead of this do the below 
        $(this).addClass("active");   
    });
    });