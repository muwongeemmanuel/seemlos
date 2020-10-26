window.onload = function() {
    addView();
}

function addView() {
    var article_id = document.getElementById('love-story').value;
    url = '/view-story/' + article_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}

    };
    req.open('GET', url, true);
    req.send();
}

function love() {
    var loves = document.getElementById('loveStory').innerHTML;
    var article_id = document.getElementById('love-story').value;
    url = '/love-story/' + article_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}

    };
    new_loves = parseInt(loves) + 1;
    req.open('GET', url, true);
    req.send();
    document.getElementById('loveStory').textContent = new_loves
}

function like() {
    var likes = document.getElementById('likeStory').innerHTML;
    var article_id = document.getElementById('like-story').value;
    url = '/like-story/' + article_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}

    };
    new_likes = parseInt(likes) + 1;
    req.open('GET', url, true);
    req.send();
    document.getElementById('likeStory').textContent = new_likes
}

function dislike() {
    var dislikes = document.getElementById('dislikeStory').innerHTML;
    var article_id = document.getElementById('dislike-story').value;
    url = '/dislike-story/' + article_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}

    };
    new_dislikes = parseInt(dislikes) + 1;
    req.open('GET', url, true);
    req.send();
    document.getElementById('dislikeStory').textContent = new_dislikes
}

function hate() {
    var hates = document.getElementById('hateStory').innerHTML;
    var article_id = document.getElementById('hate-story').value;
    url = '/hate-story/' + article_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}

    };
    new_hates = parseInt(hates) + 1;
    req.open('GET', url, true);
    req.send();
    document.getElementById('hateStory').textContent = new_hates
}