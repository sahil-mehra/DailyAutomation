
// Dependencies
var twitty = require('twit');
var config = require('./config');
var sentiment = require('sentiment');
const readline = require('readline');

// Pulling all my twitter account info from another file
var config = require('./config.js');

// Making a twitty object for connection to the API
var Twitter = new twitty(config);


// function which posts tweet taken as a cl arg
function tweeter() {

  // takes string from command line as the tweet
  var tweet = process.argv[2];
  
  // test to see if it is under 140 characters long
  if (tweet.length > 140) {
    console.log("That tweet is " + tweet.length + " characters long. A tweet may not exceed a length of 140 characters. Please try again.");
      process.exit()
  }

  // get setiment json data, and split it into score and comparative score
  var getSentiment = sentiment(tweet);
  var score = getSentiment.score;
  var comparative = getSentiment.comparative;

  // set up reader for user input
  const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  // return score and comparative and ask if the user still wants to send the tweet
  reader.question("This tweet has a score of " + score + " and a comparative score of " + comparative + " do you still want to send it?: ", (answer) => {

    if (answer == "yes" || answer == "y") {
      // Post the tweet!
      Twitter.post('statuses/update', { status: tweet }, tweeted);
    } else{
      console.log("Tweet not sent.")
    process.exit()
  }
    reader.close();
  });

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
