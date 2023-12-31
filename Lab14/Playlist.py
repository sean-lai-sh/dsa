from ChainingHashTableMap import *
from DoublyLinkedList import *


class Playlist:
    def __init__(self):
        self.map = ChainingHashTableMap()
        self.playing_list = DoublyLinkedList()  # TODO Choose one if needed

    def add_song(self, song_name):
        node_val = self.playing_list.add_last(song_name)
        self.map[song_name] = node_val
        # We want to add the song to map and then to the extra Queue [Do Doubly Linked maybe?]
        # Perhaps store something to the map so that we cna have Theta(1) avg

    def add_song_after(self, song_before, song_name):
        if song_name not in self.map:
            raise KeyError("")
        # Use our map perhaps to get the node of where the Doubly Linked List Node is, then insert after
        node_before = self.map[song_before]
        new_song_node = self.playing_list.add_after(node_before, song_name)
        self.map[song_name] = new_song_node

    def play_song(self, song_name):
        if song_name not in self.map:
            raise KeyError("")
        # Does something with the ordering where we append to the front another instance of the
        print("Playing ", song_name)

    def play_list(self):
        for elem in self.playing_list:
            print("Playing ", elem)
