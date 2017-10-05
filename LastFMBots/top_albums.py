import urllib.request
import json
import sys
import tweeter


def show_top_albums(limit,link):
    display = "My Top " + str(limit) + " My Most Listened To Albums:"

    i = 0
    while i < int(limit):
        top_albums = urllib.request.urlopen(link).read()
        top_albums_json = json.loads(top_albums.decode())

        artist = top_albums_json['topalbums']['album'][i]['artist']['name']
        album = top_albums_json['topalbums']['album'][i]['name']
        plays = top_albums_json['topalbums']['album'][i]['playcount']

        display += ('\n' + str(i+1)+ '. "' + album + '"' + ' by ' + artist + " (" + plays + " plays)")
        i = i + 1

    return display


def tweet_top_album(limit,link):
    tweet = "James' LastFM Bot: My Most Listened To Album is "

    top_albums = urllib.request.urlopen(link).read()
    top_albums_json = json.loads(top_albums.decode())

    artist = top_albums_json['topalbums']['album'][0]['artist']['name']
    album = top_albums_json['topalbums']['album'][0]['name']
    plays = top_albums_json['topalbums']['album'][0]['playcount']
    
    tweet = tweeter.format_top_album_tweet(artist, album, plays)
    status = tweeter.send(tweet)
    return status


def main():
    limit = sys.argv[1]
    username = "user-name"
    api_key = "api-key"
    
    if limit == "tweet":
        link = "http://ws.audioscrobbler.com/2.0/?method=user.getTopAlbums&user=" + username + "&limit=" + str(1) + "&api_key=" + api_key + "&format=json"
        result = tweet_top_album(limit, link)
    elif limit.isalpha():
        sys.exit("No Limit Passed, Try Again")
    else:
        link = "http://ws.audioscrobbler.com/2.0/?method=user.getTopAlbums&user=" + username + "&limit=" + str(limit) + "&api_key=" + api_key + "&format=json"
        result = show_top_albums(limit, link)

    print(result)

if __name__ == '__main__':
    main()
