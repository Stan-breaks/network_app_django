
function load(){
    const posts=document.querySelector('#posts');
    console.log(posts.dataset.page)
    fetch(`${posts.dataset.url}?page=${parseInt(posts.dataset.page)}`)
    .then(response=>response.json())
    .then(result=>{
       let postHtml=result.map(post=>{
        return(`
            <div class="post">
            <h3><a href="profile/${post.user}"<strong>${post.user}</strong></a></h3>
            <p>${post.text}</p>
            <p class="time">${post.timestamp}</p>
            <p><i class="fas fa-heart" onClick="like(event,${post.id})"></i> ${post.likes}</p>
            </div>
            `);
    }).join('');
        console.log(postHtml);
        posts.innerHTML+=postHtml;
    });
}

var liked;
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
    load();
});
document.querySelector('#text').value='';
});
function nextpage(){
    var post=document.querySelector('#posts')
    var page=parseInt(post.dataset.page)+1
    post.dataset.page=page
}
document.addEventListener('DOMContentLoaded',load);
function like(event,post_id){
    fetch(`like/${post_id}`,{
        method:'POST',
        body:JSON.stringify({
            liked:liked
        })
    })
    .then(response=>response.json())
    .then(result=>{
        console.log(result)
        load()
    });
    window.onscroll=()=>{
        if(window.scrollY+window.innerHeight>=document.body.offsetHeight){
            if(document.querySelector('#posts').dataset.page<2){
                document.querySelector('#posts').innerHTML+=`<button class="btn btn-primary" onclick="nextpage()">See more</button>`
            }
        }
       }
}
