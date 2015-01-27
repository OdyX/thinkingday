var iconStyle = new ol.style.Style({
    image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
        anchor: [0.5, 46],
        anchorXUnits: 'fraction',
        anchorYUnits: 'pixels',
        opacity: 1,
        src: STATIC_URL + "/img/marker.png"
    }))
});

var iconFeatures = [];

var messagesSource = new ol.source.Vector({});

function addIcon(message) {
    var iconFeature = new ol.Feature({
        geometry: new ol.geom.Point(ol.proj.transform([message.x, message.y], 'EPSG:4326', 'EPSG:900913')),
        id: message.id
    });
    messagesSource.addFeature(iconFeature);
}

$.ajax({
    url: POINTS_URL
}).done(function(result) {
    if (result)
        $.each(result.data, function(item, value) {
            addIcon(value);
        });
});

var messagesLayer = new ol.layer.Vector({
    source: messagesSource,
    style: iconStyle
});

var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        }),
        messagesLayer
    ],
    view: new ol.View({
        center: ol.proj.transform([8.22669, 46.80121], 'EPSG:4326', 'EPSG:900913'),
        zoom: 8,
        minZoom: 8,
        maxZoom: 17
    })
});

function addMessage(message) {
    $('#messages-content').append(message.text);
}

// display popup on click
map.on('click', function(evt) {
    var feature = map.forEachFeatureAtPixel(evt.pixel,
        function(feature, layer) {
            return feature;
        });
    if (feature) {
        var id = feature.get('id');
        $.ajax({
            url: MESSAGES_URL.replace('_point_id_', id)
        }).done(function (result) {
            if (result)
                $.each(result.data, function(item, value) {
                    addMessage(value);
                });
        });
    }
});

// change mouse cursor when over marker
$(map.getViewport()).on('mousemove', function(e) {
    var target = document.getElementById(map.getTarget());
    var pixel = map.getEventPixel(e.originalEvent);
    var hit = map.forEachFeatureAtPixel(pixel, function(feature, layer) {
        return true;
    });
    if (hit) {
        target.style.cursor = 'pointer';
    } else {
        target.style.cursor = '';
    }
});
