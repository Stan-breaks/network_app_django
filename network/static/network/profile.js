document.addEventListener('DOMContentLoaded',()=>{
    var user=document.querySelector('h2').textContent
    document.querySelector('#follow').addEventListener('click',()=>{
        fetch(`follow/${user}`,{
            method:'POST',
            body:JSON.stringify({
                follow:true
            })
        })
        .then(response=>response.json())
        .then(result=>{
            console.log(result)
        })
        setTimeout(function() {
            location.reload();
        }, 1000);
    })
})