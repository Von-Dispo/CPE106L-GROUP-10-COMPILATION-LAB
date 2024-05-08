db = connect( " localhost : 27017 /musicDatabase" )

db.artists.insertOne({
Artistld: 1,
Name: "Sample Artist" ,
Albums: [1] // This would be an array of Albumlds associated with this artist
});

db.albums.insertOne({
Albumld: 1,
Title: "Sample Album",
Artistld : 1, //This references the Artistld from the artists collection
Tracks: [1] //This would be an array of Tracklds associated with this album
});

db. tracks. insertOne({
Trackld : 1,
Name: "Sample Track",
Albumld : 1, // This references the Albumld from the albums collection
MediaTypeId : 1,
Genreld : 1,
Composer: "Sample Composer",
Milliseconds : 250000,
Bytes : 1024000,
UnitPrice: 0.99
});
