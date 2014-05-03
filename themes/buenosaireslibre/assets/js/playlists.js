function random_number()
{
    return Math.round(Math.random() * 1000000);
}

function make_playlist ( $element,playlist, options, success)
{
    if (success === undefined) success = function(){};
    $element.load('/assets/playlist-player.html', function(){
        // Asigno IDs al player y al container
        var n = random_number();
        var id_player = 'player_' + n;
        var id_container = 'container_' + n;

        $element.find('.jquery_jplayer_N').attr('id', id_player);
        $element.find('.jp_container_N').attr('id', id_container);

        //
        var myPlaylist = new jPlayerPlaylist({
            jPlayer: '#' + id_player,
            cssSelectorAncestor: '#' + id_container 
        }, [], $.extend({
            playlistOptions: {
                enableRemoveControls: true
            },
            swfPath: "js",
            supplied: "webmv, ogv, m4v, oga, mp3",
            smoothPlayBar: true,
            keyEnabled: true,
            audioFullScreen: true,
            preload: 'none'
        }, options));
        // Audio mix playlist
        $.getJSON(playlist, function(d) {
            myPlaylist.setPlaylist(d.playlist);
            success();
        });
    });
}
