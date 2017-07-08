
// Dependencies
var twitty = require('twit');
var config = require('./config');

// Making a twitty object for connection to the API
var Twitter = new twitty(config);


// function which posts tweet taken as a cl arg
function tweeter() {

  // takes string from command line as the tweet
  var tweet = process.argv[2];

  // tweet gets posted
  Twitter.post('statuses/update', { status: tweet }, tweeted);

  // function to send callback
  function tweeted(error, data, response) {
    if (error) {
      console.log(error);
    } else {
      console.log('You Just Tweeted: ' + data.text);
      process.exit()
    }
  };
}

tweeter();
