
// dependencies
var twitty = require('twit');
var config = require('./config');
var sentiment = require('sentiment');


// make new twitty object
var Twitter = new twitty(config);

// set total to zero
var total = '0';
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
    var tweet = data[i].text;
    // print out tweet text and it's respective score
    console.log(tweet + " -> " + sentiment(tweet).score);
    
    // add score to total
    total = Number(count) + Number(sentiment(tweet).score);
  }
  // output average sentiment over the last n tweets, where n is the variable numberOfTweets
  console.log("\nAverage Sentiment over the last " + data.length + " tweets: " + total / data.length)
})
