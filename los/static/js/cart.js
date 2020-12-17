function downloadRec() {
    var item = document.getElementById('epub').value;
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {}
    }
    url = '/download/' + item
    req.open('GET', url, true)
    req.send()
}