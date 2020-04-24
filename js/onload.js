var humanReadable;
var lat;
var lon;

var user = localStorage.getItem('username');

function success(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    // console.log(latitude);
    // console.log(longitude);
    mapboxgl.accessToken = 'pk.eyJ1IjoiZGFwaG5lZG9tYW5zaSIsImEiOiJjazh3YWN5bzMwa2dwM2VsZG5qNjh3c2szIn0.0ymDG-rTv4fEJdNP6V5Dqg';
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [longitude, latitude],
        zoom: 13
    });

    var geocoder = new MapboxGeocoder({
        accessToken: mapboxgl.accessToken,
        mapboxgl: mapboxgl
    });

    //map.addControl(geocoder);
    document.getElementById('geocoder').appendChild(geocoder.onAdd(map));

    map.on('load', function () {
        // listen for the `geocoder.input` event that is triggered when a user
        // makes a selection
        geocoder.on('result', function (ev) {
            var addressResult = ev.result;
            // console.log(addressResult.place_name)
            humanReadable = addressResult.place_name;
            lon = addressResult.center[0]
            lat = addressResult.center[1]
        });
    });
}

function error() {
    // console.log('Unable to retrieve your location');
}

if (!navigator.geolocation) {
    // console.log('Geolocation is not supported by your browser');
} else {
    // console.log('Locating…');
    navigator.geolocation.getCurrentPosition(success, error);
}
const type = "DryCleaning";

$(document).on('submit', 'form', async function(e) {
    e.preventDefault();
    console.log(this);
    // let that = this;
    let formInputs = []
    $('form input').each(function() {
        console.log(this.value);
        formInputs.push(this.value);
    })
    // console.log(formInputs);
    let cardnumber, exipre, cvv;
    [cardnumber, exipre, cvv] = formInputs;
    // console.log(cardnumber, exipre, cvv);
    // console.log(humanReadable);
    let check = []
    formInputs.forEach(e => {
        check.push(e.includes('_'));
        check.push(e.length == 0);
    })
    // console.log(check)
    valid = !check.includes(true) && humanReadable != null;
    if (valid) {
        let dateAdded = new Date(Date.now())
        const order = {
            "serviceType": type,
            "username": user,
            "card": cardnumber,
            "cvv": cvv,
            "expiration": exipre,
            "destination": {
                'lat': lat,
                'lon': lon,
                'humanReadable': humanReadable
            },
            "timeOrderMade": dateAdded.toISOString()
        }
        // console.log(order)

        var url = "https://demand.team22.softwareengineeringii.com/demand/order/req";
        await fetch(url, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            mode: 'no-cors',
            body: JSON.stringify(order)
        }).then(res => {
            // console.log(res.status);
            if (res.status == 200) {
                alert(res.json());
                localStorage.setItem('orderinfo', res.json());
                window.location.assign("https://demand.team22.softwareengineeringii.com/demand-front-end/services/confirmation.html");
            }
            else {
                alert('Something went wrong');
            }
        }).catch(function (error) {
            console.error(error)
        });
    }
})
