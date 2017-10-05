
var twitty = require('twit');
var config = require('./config.js');
var Twitter = new twitty(config);

var parameters = {
  q: '#coding, #programming, #technology',
  count: 10,
  result_type: 'recent',
  lang: 'en'
}

Twitter.get('search/tweets', parameters, function(error, data, response) {
  if(!error){
      let screen_name = data.statuses[0].user.screen_name;
      Twitter.post('friendships/create', {screen_name}, function(error, response){
        if(error){
          console.log(error);
        }
        else {
          console.log('You have just followed',screen_name);
        }
      });
    }
    else {
     console.log(error);
   }
 })
