function submitForm() {
    const name = document.getElementById("fieldName").value
    const age = document.getElementById("fieldAge").value
    const age_parsed = parseInt(age)

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (this.status == 200) {
            const btnSend = document.getElementById("btnUploadAvatar")
            btnSend.disabled = false
            console.log()
        }
    }
    xhr.open("POST", "/customer/insert", true);
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');

    var j = {
        "name": name,
        "age": age_parsed,
        "avatar": "/static/sample_pet.png"
    };
    xhr.send(JSON.stringify(j));
}
