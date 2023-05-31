$(document).ready(function () {

    function addData(name) {
        let list = document.getElementById("names");
        let li = document.createElement("li");
        li.innerHTML = name;
        list.appendChild(li);
    }

    function saveData(name) {
        $.post( "/save", {
      name: name
    }, function(err, req, resp){
      window.location.reload();
    });
    }
    $("#localSave").click(function () {
        let el = document.getElementById('in1');
        addData(el.value);
        el.value="";
    });

    $("#globalSave").click(function () {
        let el = document.getElementById('in1');
        saveData(el.value);
        window.location.reload();
    });
});