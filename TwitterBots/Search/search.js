// searches the last n tweets which contain a specific hashtag and conducts sentiment analysis
// over the n tweets and generate the topics average sentiment.

// some dependencies
var sentiment = require('sentiment');
var twitty = require('twit');
var config = require('./config');
var Twitter = new twitty(config);

// finds most recent tweet based on 'q' in parameters
// will not work without q parameter
var searchTweets = function() {

    var parameters = {
        q: '#' + process.argv[2],
        result_type: 'recent',
        lang: 'en',
        count: '' + process.argv[3]
    }
    // searches tweets including provided hashtag
    Twitter.get('search/tweets', parameters, function(error, data) {
        if (!error) {
          var avgSentiment = 0;
          var counter = parseInt(parameters['count'])
          for(var i = 0; i < counter; i++){
            // conducts sentiment analysis on each tweet found in given range
            var result = data.statuses[i].text;
            var getSentiment = sentiment(result);
            var score = getSentiment.score;
            avgSentiment = avgSentiment + score;
            }
            console.log("The average sentiment of the last " + parameters['count'] + " tweets containing " + parameters['q'] + " is " + avgSentiment);
        }
        else {
            console.log('Unable To Perform Search');
        }
    });
}

// search those tweets
searchTweets();
