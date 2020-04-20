var humanReadable;
var lat;
var long;

mapboxgl.accessToken = 'pk.eyJ1IjoiZGFwaG5lZG9tYW5zaSIsImEiOiJjazh3YWN5bzMwa2dwM2VsZG5qNjh3c2szIn0.0ymDG-rTv4fEJdNP6V5Dqg';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-77.0091, 38.8899],
  zoom: 13
});

var geocoder = new MapboxGeocoder({
  accessToken: mapboxgl.accessToken,
  mapboxgl: mapboxgl
});

//map.addControl(geocoder);
document.getElementById('geocoder').appendChild(geocoder.onAdd(map));

map.on('load', function() {
  // listen for the `geocoder.input` event that is triggered when a user
  // makes a selection
  geocoder.on('result', function(ev) {
    var addressResult = ev.result;
    console.log(addressResult.place_name)
    humanReadable = addressResult.place_name;
    long = addressResult.center[0]
    lat = addressResult.center[1]
    useLongLats(long, lat)
    console.log(lat)
    console.log(long)
  });
});

//  this is just a skeleton for a callback function to use your async data
// i just set some lat long variables to put something in here but you can do anything with the lat longs you pass in
// should work for any requests you make too
function useLongLats(long, lat) {
  address_lat = lat
  address_long = long


  //  make requests in here??
}




const type = "Dry_Cleaning";

let clickedOnSubmitOrder = () => {
  // console.log(lat);
  // console.log(long);
  // console.log(humanReadable);
    let username = document.getElementById('username').value;
    let newCardNumber = document.getElementById('card').value;
    let newCVV = document.getElementById('cvv').value;
    let newExpirationDate = document.getElementById('expiration').value;
    // if (username.length == 0 || newCardNumber.length == 0 || newCVV.length == 0 || newExpirationDate.length == 0 || newDestinationAddress.length == 0) {
        // alert("Please fill in all the required information.");
    // }
    // else {
    let dateAdded = new Date(Date.now())
     const order = {
            "serviceType" : type,
            "username" : username,
            "card" : newCardNumber,
            "cvv" : newCVV,
            "expiration" : newExpirationDate,
            "destination" : {
              'lat' : lat,
              'lon' : long,
              'humanReadable' : humanReadable
            },
            "timeOrderMade" : dateAdded.toISOString()
      }
      console.log(order)
      const options = {
            method: "POST",
            headers: {
                'Content-Type' : 'application/json'
            },
            mode: 'no-cors',
            body: JSON.stringify(order)
      }
      fetch("https://demand.team22.softwareengineeringii.com/orderHandler", options).then(function(response) {
            console.log(response.status);
            if (response.status == 200) {
                window.location.assign("https://demand.team22.softwareengineeringii.com/demand-front-end/services/confirmation.html");
            }
            else {
                alert("There is no username tied to that account!");
            }
      }).catch(function(error) {
           console.error(error)
           });


      // }
   }
