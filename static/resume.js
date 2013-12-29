window.onload = function () {
    var categories = document.getElementById("categories").getElementsByTagName("h3");
    
    for (var i = 0; i < categories.length; i++) {
        var cat = categories[i];
        var func = jumpBuilder(cat.innerHTML);
        cat.onclick = func;
        cat.onmouseover = func;
    }
}

function jumpBuilder(id) {
    var elid = id;
    function jumpTo() {
        window.location = '#' + elid;
    }
    return jumpTo;
}
