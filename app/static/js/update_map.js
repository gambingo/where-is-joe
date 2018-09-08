$.getJSON("static/json/location.json", function(data) {
 var  lat = data["lat"]
      lng = data["lng"]
      ts = data["ts"]
      city = data["city"]
      state = data["state"]
      country = data["country"]

  // Map
  var map = L.map('map', {maxZoom: 13}).setView([lat, lng], 13);
  var mapbox_public_token="pk.eyJ1Ijoiam9lZ2FtYmlubyIsImEiOiJjamxmdm5maWIxMTIzM3ByczkxcHJqYnY4In0.O_j3x2BT_oEd_mFBPG3x_A";

  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: 'mapbox.streets',
      accessToken: mapbox_public_token
  }).addTo(map);

  // My Face
  var myFace = L.icon({
    iconUrl: 'static/img/joe.gif',

    iconSize:     [60, 60], // size of the icon
    iconAnchor:   [30, 30], // point of the icon which will correspond to marker's location
    popupAnchor:  [-30, -30] // point from which the popup should open relative to the iconAnchor
  });

  L.marker([lat, lng], {icon: myFace}).addTo(map);

  // Text Box
  var info = `Joe was last seen in ${city}, ${state}.`;
  console.log(info);

  L.Control.Info = L.Control.extend({
    // options: {position: 'topright']},
    onAdd: function(map) {
      var div = L.DomUtil.create('div', 'info');
      div.innerHTML = info;
      return div
    },
    onRemove: function(map) {
      //Nothing here
    }
  });

  L.control.info = function(options) {
    return new L.Control.Info(options);
  };

  L.control.info({position: 'topright'}).addTo(map);
});
