var tz = Intl.DateTimeFormat().resolvedOptions().timeZone

function Countdown() {
    const request = new XMLHttpRequest();
    request.open("GET", `/fun/time?tz=${tz}`);
    request.send();
    request.onreadystatechange = (e) => {
        data = JSON.parse(request.responseText)
        document.getElementById('days').innerHTML = data.day;
        document.getElementById('hours').innerHTML = data.hour;
        document.getElementById('minutes').innerHTML = data.min;
        document.getElementById('secs').innerHTML = data.sec;
    };
};
window.onload = function() {
    setInterval(Countdown, 100);
};