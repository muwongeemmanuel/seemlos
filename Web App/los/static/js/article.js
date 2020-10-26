window.onload = function() {
    AddView();
    initAll();
}

var loveArticle
var dislikeArticle
var likeArticle
var hateArticle

function initAll() {
    loveArticle = document.getElementById('like-article')
    loveArticle.onclick = add_love;
    likeArticle = document.getElementById('love-article')
    likeArticle.onclick = add_like;
    dislikeArticle = document.getElementById('dislike-article')
    dislikeArticle.onclick = add_dislike;
    hateArticle = document.getElementById('hate-article')
    hateArticle.onclick = add_hate;
    comArticle = document.getElementById('combut')
    comArticle.onclick = addcomment;
}


// ****Working on article quick reactions****

function AddView() {
    var article_id = document.getElementById('love-article').value;
    url = '/view-article/' + article_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}

    };
    req.open('GET', url, true);
    req.send();
}

function add_love() {
    var loves = document.getElementById('like-article').value;
    var likes = document.getElementById('likes').innerHTML;
    url = ('/like-article/' + loves);
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {

        }
    };
    new_likes = parseInt(likes) + 1
    req.open('GET', url, true)
    req.send();
    document.getElementById('likes').textContent = new_likes
}

function add_like() {
    var article_id = document.getElementById('love-article').value;
    var loves = document.getElementById('love').innerHTML;
    url = ('/love-article/' + article_id);
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}
    };
    new_love = parseInt(loves) + 1
    req.open('GET', url, true)
    req.send();
    document.getElementById('love').textContent = new_love
}


function add_dislike() {
    var article_id = document.getElementById('dislike-article').value;
    var dislikes = document.getElementById('dislikes').innerHTML;
    url = ('/dislike-article/' + article_id)
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {

        }
    };
    new_dislikes = parseInt(dislikes) + 1
    req.open('GET', url, true)
    req.send()
    document.getElementById('dislikes').textContent = new_dislikes
}

function add_hate() {
    var article_id = document.getElementById('dislike-article').value;
    var hates = document.getElementById('hates').innerHTML;
    url = ('/hate-article/' + article_id)
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {

        }
    };
    new_hates = parseInt(hates) + 1
    req.open('GET', url, true)
    req.send()
    document.getElementById('hates').textContent = new_hates
}

function addcomment() {
    var article_id = document.getElementById('dislike-article').value;
    var comment = document.getElementById('comment').value;
    var block_to_insert
    var container_block
    block_to_insert = document.createElement("div");
    block_to_insert.innerHTML = (comment)
    url = ('/comment-article/' + article_id + '/' + comment)
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {

        }
    };
    req.open('GET', url, true)
    req.send()
    container_block = document.getElementById("commented")
    container_block.append(block_to_insert)
}