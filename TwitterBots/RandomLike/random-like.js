// I know its called favourite but its called Like everwhere but the API
// So it's like here

var twitty = require('twit');
var config = require('./config');

var Twitter = new twitty(config);

// gets a random tweet based on q parameter and then'likes' it
// q is required for the program to work
var likeTweet = function(){
  var parameters = {
      q: '#programming, #coding', 
      result_type: 'recent',
      lang: 'en'
  }
  
  // find the tweet
  Twitter.get('search/tweets', parameters, function(error,data){

    // find tweets using q value
    var tweet = data.statuses;
    var randomTweet = getRandomTweet(tweet);

    // if tweet is found
    if(typeof randomTweet != 'undefined'){
      // tell twitter to like it
      Twitter.post('favorites/create', {id: randomTweet.id_str}, function(error, response){
        // if error occured when liking the tweet
        if(error){
          console.log('Unable To Like Tweet');
        }
        else{
          console.log('Liked A Tweet, Go Check What It Is');
        }
      });
    }
  });
}

// gets random tweet using Math.random() and the status returned from tweet as an array
function getRandomTweet(array) {
  var i = Math.floor(Math.random() * array.length);
  return array[i];
};

// likes tweet when running
likeTweet();

