# Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the 
# user has listened to as values.
# Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs 
# within that genre as values. The song can only belong to only one genre.
# The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list 
# of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one 
# favorite genre if he/she has listened to the same number of songs per each of the genres.

#import collections
def favGenres(userSongs, songGenres):
    output={}
    for user in userSongs:
        user_song_list = userSongs[user]
        #genre_count = collections.defaultdict(int)
        genre_count = {}
        for user_song in user_song_list:
            for genre, genre_song in songGenres.items():
                if user_song in genre_song:
                    #genre_count[genre] += 1
                    genre_count[genre] = genre_count.get(genre, 0) + 1
        #output[user]=[genre for genre, genre_song in genre_count.items() \
        #              if genre_song == max(genre_count.values())]
        for genre, genre_song in genre_count.items():
            if genre_song == max(genre_count.values()):
                output[user] = genre
        
    return output
# Test
userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}
favGenres(userSongs, songGenres)
# Time: O(U*S*G), space: O(U*G)
