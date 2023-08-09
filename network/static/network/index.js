
document.querySelector('#btn').addEventListener('click',(event)=>{
    event.preventDefault();
fetch(event.target.dataset.url,{
    method:'POST',
    body: JSON.stringify({
        text:document.querySelector('#text').value
    })
})
.then(response=>response.json())
.then(result=>{
    console.log(result);
});
setTimeout(function() {
    location.reload();
}, 500);
});

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
    });
    setTimeout(function() {
        location.reload();
    }, 500);
}
const heartIcons = document.querySelectorAll(".fas");
heartIcons.forEach(icon => {
    icon.addEventListener("click",(event)=>{
        const likeurl= event.target.dataset.url;
        like(likeurl)
    });
});