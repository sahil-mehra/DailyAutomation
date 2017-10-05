import urllib.request
import json
import sys
import tweeter


def show_top_tracks(limit,link):
    display = "Top " + str(limit) + " Most Listened To Tracks:"

    i = 0
    while i < int(limit):
        top_tracks = urllib.request.urlopen(link).read()
        top_tracks_json = json.loads(top_tracks.decode())

        track = top_tracks_json['toptracks']['track'][i]['name']
        artist = top_tracks_json['toptracks']['track'][i]['artist']['name']
        plays = top_tracks_json['toptracks']['track'][i]['playcount']
        display += ('\n' + str(i+1) + ". " + track + " by " + artist + " (" + plays + " plays)")
        i = i + 1

    return display


def tweet_top_track(limit,link):

    top_tracks = urllib.request.urlopen(link).read()
    top_tracks_json = json.loads(top_tracks.decode())

    track = top_tracks_json['toptracks']['track'][0]['name']
    artist = top_tracks_json['toptracks']['track'][0]['artist']['name']
    plays = top_tracks_json['toptracks']['track'][0]['playcount']

    tweet = tweeter.format_top_tracks_tweet(track, artist, plays)
    status = tweeter.send(tweet)

    return status


def main():
    limit = sys.argv[1]
    username = "user-name"
    api_key = "api-key"

    if limit == "tweet":
        link = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=" + username + "&limit=" + str(1) + "&api_key=" + api_key + "&format=json"
        result = tweet_top_track(limit, link)
    elif limit.isalpha():
        sys.exit("No Limit Passed, Try Again")
    else:
        link = "http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=" + username + "&limit=" + str(limit) + "&api_key=" + api_key + "&format=json"
        result = show_top_tracks(limit, link)

    print(result)

if __name__ == '__main__':
    main()
