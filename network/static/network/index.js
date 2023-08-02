function load(){
    const posts=document.querySelector('#posts');
    fetch(posts.dataset.url)
    .then(response=>response.json())
    .then(result=>{
       let postHtml=result.map(post=>{
        var comments=post.comments.map(comment=>`
            <li>
            <span> ${comment.user} </span><span> ${comment.commenttext} </span><span> ${comment.timestamp} </span>
            </li>
        `).join('');
        return(`
            <div class="post">
           <h3><strong>${post.user}</strong></h3>
            <a href="#">Edit</a>
            <p>${post.text}</p>
            <p class="time">${post.timestamp}</p>
            <p><i class="fas fa-heart"></i> ${post.likes}</p>
            <p class="comment"onClick="${load_comments}">Comment</p>
            <div class="commentsection" style="display:none;">
            <form>
            <input autofocus=True data-url="{%url 'comment'${post.id}%}" onKeyDown="${comment}" type="text"/>
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
function load_comments(event){
console.log(event)
};
function comment(event){
        if(event.key==='Enter'){
        fetch(event.target.dataset.url,{
            method :'POST',
            body: JSON.stringify({
                commenttext:event.target.value
            })
        })
}
}
document.addEventListener('DOMContentLoaded',load());