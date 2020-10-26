function loveItem() {
    var loves = document.getElementById('love').innerHTML;
    var item_id = document.getElementById('love-item').value;
    url = '/love-item/' + item_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}
    };
    req.open('GET', url, true);
    req.send();
    new_loves = parseInt(loves) + 1;
    document.getElementById('love').textContent = new_loves;
}

function likeItem() {
    var loves = document.getElementById('likes').innerHTML;
    var item_id = document.getElementById('like-item').value;
    url = '/like-item/' + item_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}
    };
    req.open('GET', url, true);
    req.send();
    new_loves = parseInt(loves) + 1;
    document.getElementById('likes').textContent = new_loves;
}

function dislikeItem() {
    var dislikes = document.getElementById('dislikes').innerHTML;
    var item_id = document.getElementById('dislike-item').value;
    url = '/dislike-item/' + item_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}
    };
    req.open('GET', url, true);
    req.send();
    new_loves = parseInt(dislikes) + 1;
    document.getElementById('dislikes').textContent = new_loves;
}

function hateItem() {
    var dislikes = document.getElementById('hates').innerHTML;
    var item_id = document.getElementById('hate-item').value;
    url = '/hate-item/' + item_id
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}
    };
    req.open('GET', url, true);
    req.send();
    new_loves = parseInt(dislikes) + 1;
    document.getElementById('hates').textContent = new_loves;
}

function wishlist() {
    var item_id = document.getElementById('love-item').value;
    var title = document.getElementById('bookTitle').innerText;
    url = '/add-wishlist/' + item_id;
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}
    };
    req.open('GET', url, true);
    req.send();
    alert(title + ' was successfully added to your wishlist!')
}

function alertSign() {
    alert('You need to sign into your account first')
}

function cartlist() {
    var item_id = document.getElementById('love-item').value;
    var title = document.getElementById('bookTitle').innerHTML;
    url = '/add-to-cart/' + item_id + '/add'
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200); {}
    };
    req.open('GET', url, true);
    req.send();
    alert(title + ' was successfully added to your wishlist!')
}