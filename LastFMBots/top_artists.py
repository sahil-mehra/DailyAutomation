import urllib.request
import json
import sys
import tweeter


def show_top_artists(limit,link):
    display = "Top " + str(limit) + " Most Listened To Artists:"

    i = 0
    while i < int(limit):
        top_artists = urllib.request.urlopen(link).read()
        top_artists_json = json.loads(top_artists.decode())

        artist = top_artists_json['topartists']['artist'][i]['name']
        plays = top_artists_json['topartists']['artist'][i]['playcount']

        display += ('\n' + str(i+1) + ". " + artist + " (" + plays + " plays)")
        i = i + 1

    return display


def tweet_top_artist(limit,link):

    top_artists = urllib.request.urlopen(link).read()
    top_artists_json = json.loads(top_artists.decode())

    artist = top_artists_json['topartists']['artist'][0]['name']
    plays = top_artists_json['topartists']['artist'][0]['playcount']

    tweet = tweeter.format_top_artist_tweet(artist, plays)
    status = tweeter.send(tweet)

    return status


def main():
    limit = sys.argv[1]
    username = "user-name"
    api_key = "api-key"

    if limit == "tweet":
        link = "http://ws.audioscrobbler.com/2.0/?method=user.getTopArtists&user=" + username + "&limit=" + str(1) + "&api_key=" + api_key + "&format=json"
        result = tweet_top_artist(limit, link)
    elif limit.isalpha():
        sys.exit("No Limit Passed, Try Again")
    else:
        link = "http://ws.audioscrobbler.com/2.0/?method=user.getTopArtists&user=" + username + "&limit=" + str(limit)+ "&api_key=" + api_key + "&format=json"
        result = show_top_artists(limit, link)

    print(result)

if __name__ == '__main__':
    main()
