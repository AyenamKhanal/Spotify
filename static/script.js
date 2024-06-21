$(document).ready(function() {
    function refreshTopTracks() {
        var timePeriod = $("#tracks-time-period").val();
        $.ajax({
            url: topTracksUrl,
            type: "GET",
            data: { period: timePeriod },
            success: function(data) {
                var topTracksHtml = "";
                data.tracks.forEach(function(track, index) {
                    topTracksHtml += "<li>" + track + "<img src='" + data.covers[index] + "' alt='' class='home-images'></li>";
                });
                $("#top-tracks-list").html(topTracksHtml);
            },
            error: function(error) {
                console.error("Error fetching top tracks:", error);
            }
        });
    }

    function refreshTopArtists() {
        var timePeriod = $("#artists-time-period").val();
        $.ajax({
            url: topArtistsUrl,
            type: "GET",
            data: { period: timePeriod },
            success: function(data) {
                var topArtistsHtml = "";
                data.artists.forEach(function(artist, index) {
                    topArtistsHtml += "<li>" + artist + "<img src='" + data.artists_profile_pics[index] + "' alt='' class='home-images'></li>";
                });
                $("#top-artists-list").html(topArtistsHtml);
            },
            error: function(error) {
                console.error("Error fetching top artists:", error);
            }
        });
    }

    // Set up click event handlers for the buttons
    $("#refresh-tracks-button").click(refreshTopTracks);
    $("#refresh-artists-button").click(refreshTopArtists);

    // Initial load with default period (monthly)
    refreshTopTracks();
    refreshTopArtists();
});
