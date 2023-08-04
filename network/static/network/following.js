document.addEventListener('click',()=>{
    function like(url){
        fetch(url,{
            method:'POST',
            body:JSON.stringify({
                liked:true
            })
        })
        .then(response=>response.json())
        .then(result=>{
            console.log(result)
            setTimeout(function() {
                location.reload();
            }, 500);
        });
    }
    const heartIcons = document.querySelectorAll(".fas");
    heartIcons.forEach(icon => {
        icon.addEventListener("click",(event)=>{
            const likeurl= event.target.dataset.url;
            like(likeurl)
        });
    });
})