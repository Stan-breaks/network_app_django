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
            <p class="comment">Comment</p>
            <form  data-url="{%url 'comment'${post.id}%}" onSubmit="comment">
            <input type="text"/>
            <input type="submit" value="Submit Comment" />
            </form>
            <ul>${post.comments}</ul>
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

function comment(event){
    event.preventDefault();
    console.log("comment");
}
document.addEventListener('DOMContentLoaded',load());