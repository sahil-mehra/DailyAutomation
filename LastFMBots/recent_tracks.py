import urllib.request
import json
import sys
import tweeter


def show_recent_tracks(limit,link):
    i = 0
    limit = int(sys.argv[1])
    display = "My " + str(limit) + " Most Recently Played Tracks:"
    while i < limit:
        recent_track = urllib.request.urlopen(link).read()
        recent_track_json = json.loads(recent_track.decode())

        track = recent_track_json['recenttracks']['track'][i]['name']
        artist = recent_track_json['recenttracks']['track'][i]['artist']['#text']

        if limit == 1:
            display = ""
            display = "The most recent track I played was " + track + " by " + artist
            break
        display += '\n' + str(i + 1) + ". " + track + " by " + artist
        i = i + 1
    return display

def tweet_recent_track(limit,link):
    recent_track = urllib.request.urlopen(link).read()
    recent_track_json = json.loads(recent_track.decode())

    track = recent_track_json['recenttracks']['track'][0]['name']
    artist = recent_track_json['recenttracks']['track'][0]['artist']['#text']

    tweet = tweeter.format_recent_track_tweet(track, artist)
    status = tweeter.send(tweet)

    return status

def main():
    limit = sys.argv[1]
    username = "user-name"
    api_key = "api-key"

    if limit == "tweet":
        link = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + username + "&limit="+ str(1) + "&api_key=" + api_key + "&format=json"
        result = tweet_recent_track(limit,link)
    elif limit.isalpha():
        sys.exit("No Limit Passed, Try Again")
    else:
        link = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=" + username + "&limit="+ str(limit) + "&api_key=" + api_key + "&format=json"
        result = show_recent_tracks(limit,link)

    print(result)

if __name__ == '__main__':
    main()
