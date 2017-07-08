
// dependencies
var twitty = require('twit');
var config = require('./config');

// make new twitty object
var Twitter = new twitty(config);

// takes a command line argument
// the last n tweets made by the screen_name
var numberOfTweets = process.argv[2];

// won't work without both screen_name and count values
var parameters = {
  screen_name: '_TheyCallMeMac_',
  count: numberOfTweets
};

// function logs the text from the tweets collected
Twitter.get('statuses/user_timeline', parameters , function(error, data) {
  for (var i = 0; i < data.length ; i++) {
    console.log("\n" + data[i].text);
  }
})
