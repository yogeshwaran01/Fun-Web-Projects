var btn = document.getElementById('btn')
var date = document.getElementById('date_p')
var mess = document.getElementById('message')

btn.onclick = () => {
    var date_val = date.value;
    var date_ = new Date(date_val)
    var now_year = new Date().getFullYear()
    if (date_.getFullYear() >= now_year) {
        alert("Future Year not Allowed")
    }
    else {
        var api = `/tools/age?date=${date_val}`
        location.href = api
    }
}