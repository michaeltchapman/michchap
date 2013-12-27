window.onload = function () {
    var categories = document.getElementById("categories").getElementsByTagName("h3");
    var repos = document.getElementById("personal").getElementsByTagName("div");
    
    for (var i = 0; i < categories.length; i++) {
        var cat = categories[i];
        var func = jumpBuilder(cat.innerHTML);
        cat.onclick = func;
        cat.onmouseover = func;
    }

    for (var i = 0; i < repos.length; i++) {
        var repo = repos[i];
        var func = descriptionBuilder(repo.id);
        repo.onmouseover = func;
        repo.onmouseout = func;
        repo.onclick = func;
    }
}

function jumpBuilder(id) {
    var elid = id;
    function jumpTo() {
        window.location = '#' + elid;
    }
    return jumpTo;
}

function descriptionBuilder(name) {
    var repoName = name;
    function toggle() {
    	var element = document.getElementById("personal_description_" + repoName);
        if (element.style.display == 'block') {
             element.style.display = 'none';
        } else {
            element.style.display = 'block';
        }
    }
    return toggle
}
