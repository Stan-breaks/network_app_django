function load(){
    const posts=document.querySelector('#posts');
    fetch(posts.dataset.url)
    .then(response=>response.json())
    .then(result=>{
       let postHtml=result.map(post=>{
        comments=post.comments.map(comment=>`
            <li>
            <span> ${comment.user} </span><span> ${comment.commenttext} </span><span> ${comment.timestamp} </span>
            </li>
        `).join('');
        return(`
            <div class="post">
0            <h3><strong>${post.user}</strong></h3>
            <a href="#">Edit</a>
            <p>${post.text}</p>
            <p class="time">${post.timestamp}</p>
            <p><i class="fas fa-heart"></i> ${post.likes}</p>
            <p onClick="comment">Comment</p>
            <div id="commentsection" style="display:none;">
            <form>
            <input autofocus=True data-url="{%url 'comment'${post.id}%}"id="commenttext" type="text"/>
            </form>
            <ul>${comments}</ul>
            </div>
            </div>
            `);
    }).join('');
        console.log(postHtml);
        posts.innerHTML=postHtml;
    });
}
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
load();
document.querySelector('#text').value='';
});
function comment(){
    document.querySelector('#commentsection').style.display='block';
    document.querySelector('#commenttext').addEventListener('keydown',(event)=>{
        if(event.key==='Enter'){
        fetch(event.target.dataset.url,{
            method :'POST',
            body: JSON.stringify({
                commenttext:event.target.value
            })
        })
        }
    });
});

document.addEventListener('DOMContentLoaded',load());