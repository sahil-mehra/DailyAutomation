// because random things are fun and sometimes little dangerous

// some dependencies
var twitty = require('twit');
var config = require('./config');
var Twitter = new twitty(config);

// finds most recent tweet based on 'q' in parameters
// will not work without q parameter
var randomRetweet = function() {

    var parameters = {
        q: '#programming, #coding',
        result_type: 'recent',
        lang: 'en'
    }

    Twitter.get('search/tweets', parameters, function(error, data) {
        if (!error) {
          // get id of tweet to retweet if no error rises
            var tweetId = data.statuses[0].id_str;
            // tell twitter to retweet based on tweet id
            Twitter.post('statuses/retweet/:id', {
                id: tweetId
            }, function(error, response) {
                // if error during tweeting
                // usually occurs due to duplicating the action, i.e trying to retweet a tweet which has already been retweeted
                if (error) {
                    console.log('Error Occured While Retweeting');
                    process.exit()
                }
                // if no error logs the following
                if (response) {
                    console.log('Retweeted A Random Tweet, Go Check What It Is');
                }
            });
        }
        // in the case program is unable to search/find a tweet to retweet
        else {
          console.log('Unable To Search For Tweet');
        }
    });
}

// retweets when running
randomRetweet();
