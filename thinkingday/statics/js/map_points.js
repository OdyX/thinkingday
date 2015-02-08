var iconStyle = new ol.style.Style({
    image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
        anchor: [16, 30],
        anchorXUnits: 'pixels',
        anchorYUnits: 'pixels',
        src: STATIC_URL + "/img/marker.png"
    }))
});

var iconTempStyle = new ol.style.Style({
    image: new ol.style.Icon(/** @type {olx.style.IconOptions} */ ({
        anchor: [16, 30],
        anchorXUnits: 'pixels',
        anchorYUnits: 'pixels',
        src: STATIC_URL + "/img/marker_temp.png"
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

var tempSource = new ol.source.Vector({});

function addTempIcon(point) {
    var iconFeature = new ol.Feature({
        geometry: point,
    });
    tempSource.clear();
    tempSource.addFeature(iconFeature);
}

var tempLayer = new ol.layer.Vector({
    source: tempSource,
    style: iconTempStyle
});

var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        }),
        messagesLayer,
        tempLayer
    ],
    view: new ol.View({
        center: ol.proj.transform([8.22669, 46.80121], 'EPSG:4326', 'EPSG:900913'),
        zoom: 8,
        minZoom: 8,
        maxZoom: 17,
        extent: ol.proj.transformExtent([3, 45, 15, 49], 'EPSG:4326', 'EPSG:900913')
    })
});

var content = $('#messages-content');
var form = $('#form_container');
//var point_field = form.find('#');

function addMessage(message) {
    content.append('<div class="message"><div class="message_infos"><img class="socialaccount-avatar" src="' + message.avatar + '" alt="avatar">' + message.user + '<br><span class="datetime">' + message.datetime + '</span></div><p class="message_text">' + message.message + '</p>');
}

// event on map click => show messages or display form to add one
map.on('click', function(event) {
    var feature = map.forEachFeatureAtPixel(event.pixel,
        function(feature, layer) {
            return feature;
        });
    // feature exist -> return messages
    if (feature && (id = feature.get('id'))) {
        form.hide();
        //point_field.empty();
        tempSource.clear();
        // get messages
        $.ajax({
            url: MESSAGES_URL.replace('_point_id_', id)
        }).done(function (result) {
            if (result) {
                content.empty().show();
                $.each(result.messages, function(item, value) {
                    addMessage(value);
                });
            }
        });
    } else {
        // Return click position to add a new point
        var point = new ol.geom.Point(event.coordinate);
        var coord = ol.proj.transform(point.getCoordinates(), 'EPSG:900913', 'EPSG:4326');
        form.html('SRID=4326;POINT(' + coord[0] + ' ' + coord[1] + ')').show();
        //point_field.html('SRID=4326;POINT(' + coord[0] + ' ' + coord[1] + ')');
        //form.show();
        content.empty().hide();
        addTempIcon(point);
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
