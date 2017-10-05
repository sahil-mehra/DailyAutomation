var mastodon = require('mastodon')
var config = require('./config');

var Mastodon = new mastodon(config);

function tooter(){
  var toot = process.argv[2];
  if (toot.length > 500) {
    console.log("That toot is " + toot.length + " characters long. A toot may not exceed a length of 500 characters. Please try again.");
      process.exit()
  }
  else {
    Mastodon.post('statuses', { status: toot}, tooted);
  }

function tooted(error, data, response) {
    if (error) {
      console.log(error);
    } else {
      console.log('You Just Tooted: ' + toot);
      process.exit()
    }
  };
}

tooter();

