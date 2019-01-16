var xTing = (function() {
	var moji_obj = null, 
		moji_list = [":)", ";)", ":(", "|)", "|(", ";(", ":)"],
		MOJI_HAPPY = 0,
		MOJI_SAD = 2,
		current_motion = MOJI_HAPPY,
		media_obj = null,
		speaking = false,
		speaker_timer = null;

	function media_playing_callback(e) {
		app.log( 'xTing - media_playing_callback status: ' + JSON.stringify(e) );
		if ( e == Media.MEDIA_STOPPED && speaking ) {
			media_obj.play();
		}
	}

	return {
		init: function() {
			app.log( 'xTing - init.' );
			moji_obj = document.getElementById("xTingMoji");
			media_obj = new Media("file:///android_asset/www/wav/robot.mp3", function(){
				app.log( 'xTing - init - create media object success.' );
			}, function(e) {
				app.log( 'xTing - init - create media object failed - ' + JSON.stringify(e) );
			}, media_playing_callback);
		},

		start_speak: function() {
			var tmp_idx,
				tmr_callback = function() {
					if ( tmp_idx >= moji_list.length ) {
						tmp_idx = 0;
					}
					moji_obj.innerText = moji_list[tmp_idx];
					tmp_idx++;
					speaker_timer = setTimeout(tmr_callback, 200);	
				};
			
			if (moji_obj) {
				tmp_idx = 0;
				this.stop_speak();
				media_obj.play();
				speaker_timer = setTimeout(tmr_callback, 200);	
			}

			speaking = true;
		},

		stop_speak: function() {
			if (speaker_timer) {
				clearTimeout(speaker_timer);
				speaker_timer = null;
				media_obj.stop();
				moji_obj.innerText = moji_list[MOJI_HAPPY];
			}

			speaking = false;
		}
	};
}());

function auto_test() {
	setTimeout(function() {
		xTing.stop_speak();
	}, 20000);

	xTing.start_speak();
}

var app = {
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicitly call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

		app.log('Received Event: ' + id);

		xTing.init();
		auto_test();
	},

	log: function(msg) {
		console.log('-xTing- ' + msg);
	}
};

app.initialize();
