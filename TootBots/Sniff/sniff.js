var mastodon = require('mastodon')
var config = require('./config');
var striptags = require('striptags');

var Mastodon = new mastodon(config);
var n = process.argv[2];

var sniffTimeline = function() {
    Mastodon.get('timelines/public', {local: 'yes'}, function(error, data) {
    if (!error) {
      for(var i = 0; i < n; i++){
        var uName = data[i].account['username'];
        var toot = striptags(data[i].content);
        console.log(uName + " tooted this: " + toot + "\n");
        }
    }
    else {
        console.log('Unable To Sniff Local Timeline');
    }
  });
 }

 sniffTimeline();
