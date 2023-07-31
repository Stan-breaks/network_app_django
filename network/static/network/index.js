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
    console.log(result)
});
});

document.addEventListener('DOMContentLoaded',()=>{
const posts=document.querySelector('#posts');
    fetch(posts.dataset.url)
    .then(response=>response.json())
    .then(result=>{
       let postHtml=result.map(post=>`
            <div class="post">
            <h3><strong>${post.user}</strong></h3>
            <a href="#">Edit</a>
            <p>${post.text}</p>
            <p class="time">${post.timestamp}</p>
            <p><i class="fas fa-heart"></i> ${post.likes}</p>
            <p class="comment">Comment</p>
            </div>
            `).join('');
        console.log(postHtml);
        posts.innerHTML=postHtml;
    })
});