function copyUrl() {
    let copyText = document.getElementById("short-url");
    copyText.select();
    copyText.setSelectionRange(0, 99999); /*For mobile devices*/
    document.execCommand("copy");
}


$("#copy-btn").click(function () {
    $("div.success").fadeIn(300).delay(1500).fadeOut(900);
});

function checkUrl(event) {
    let value = document.getElementById('url-input').value;
    if (value.length < 5) {
        $("div.alert-warning").fadeIn(300).delay(1500).fadeOut(900);
        event.preventDefault();
        return false;
    }
}
