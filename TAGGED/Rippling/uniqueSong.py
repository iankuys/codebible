"""
Problem: Music Analytics System

Most Played Songs by Unique Users
add_song(songId)
play_song(userId, songId)
print_analytics()

Recently Played Unique Songs
print_recently_played(userId)
print_recently_played(userId, k)
"""

from collections import defaultdict
import heapq
class MusicAnalytics:

    def __init__(self):
        self.songs = set()
        self.users = defaultdict(list)
        self.song_users = defaultdict(set)

    def add_song(self, songId):
        self.songs.add(songId)

    def play_song(self, userId, songId):
        if songId not in self.songs:
            print(f"Song {songId} does not exist.")
            return
        self.users[userId].insert(0, songId)
        self.song_users[songId].add(userId)

    def print_recently_played(self, userId, k=1):
        history = self.users.get(userId, [])
        for song in history[:k]:
            print(song)

    def print_analytics(self):
        for key, value in self.song_users.items():
            print(f"Song {key}: {len(value)} of unique users")
            
    def print_top_k_most_played_songs(self, k):
        heap = [(len(value), key) for key, value in self.song_users.items()]
        res = heapq.nlargest(k, heap)
        print("The most played songs by unique users are:")
        for count, song in res:
            print(f"Song {song} with {count} unique users")
        
