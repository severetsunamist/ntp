// Initialize and add the map
let map;

const nt_map_marker = document.createElement('img');
nt_map_marker.src = "https://ntproperties.ru/img/baloon.png"
nt_map_marker.style.width = "52px"
nt_map_marker.style.height = "65px"

async function initMap() {
  // The location
  const position = { lat: latitude, lng: longitude };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map
  map = new Map(document.getElementById("map"), {
    zoom: 9,
    center: position,
    mapId: "DEMO_MAP_ID",
    streetViewControl: false,
    mapTypeControl: false
  });

  // The marker
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Локация",
    content: nt_map_marker,
  });
}

initMap();