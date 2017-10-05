import tweepy


def send(tweet):
    config = tweepy.OAuthHandler('api-key', 'api-secret')
    config.set_access_token('token', 'token-secret')
    api_key = tweepy.API(config)
    status = api_key.update_status(tweet)
    return "Tweet Sent: " + tweet


def format_top_artist_tweet(artist, plays):
    tweet = "James' LastFM Bot: My Most Listened To Artist is "
    tweet += artist + " (" + plays + " plays) #lastfm #python #bots #music"
    return tweet


def format_top_album_tweet(artist, album, plays):
    tweet = "James' LastFM Bot: My Most Listened To Album is "
    tweet += artist + " (" + plays + " plays) #lastfm #python #bots #music"
    return tweet

def format_recent_track_tweet(track, artist):
    tweet = "James' LastFM Bot: The Most Recent Track I Played is "
    tweet += track + " by " + artist + " #lastfm #python #bots #music"
    return tweet


def show_draft(tweet):
    print(tweet)
    return


def main():
    print("tweettweet is for lastfm python script usage only.")
if __name__ == '__main__':
    main()
