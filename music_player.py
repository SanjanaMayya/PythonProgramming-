import os
import time
import threading
import pygame

pygame.mixer.init()

playlist = [
    r"D:\T SANJANA-PYTHON\playlist\song1.mp3",
    r"D:\T SANJANA-PYTHON\playlist\song2.mp3",
    r"D:\T SANJANA-PYTHON\playlist\song3.mp3"
]

stop_event = threading.Event()
player_thread = None


def show_menu():
    print("\nMusic Player Menu")
    print("1. Play first song only")
    print("2. Play all songs once")
    print("3. Play all songs in a loop")
    print("4. Stop current playback")
    print("5. Exit")


def get_valid_songs(song_list):
    valid_songs = []

    for song in song_list:
        if os.path.isfile(song):
            valid_songs.append(song)
        else:
            print(f"File Not Found: {song}. Skipping...")

    return valid_songs


def play_song(song):
    try:
        print(f"Now playing: {song}")
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            if stop_event.is_set():
                pygame.mixer.music.stop()
                return
            time.sleep(0.1)

    except Exception as e:
        if not stop_event.is_set():
            print(f"Error playing {song}: {e}")


def play_playlist_thread(valid_songs, loop=False):
    global player_thread

    try:
        while True:
            for song in valid_songs:
                if stop_event.is_set():
                    print("Playback stopped.")
                    return

                play_song(song)

                if stop_event.is_set():
                    print("Playback stopped.")
                    return

            if not loop:
                print("Playlist finished")
                return

            print("Playlist loop restarted")

            if stop_event.is_set():
                print("Playback stopped.")
                return

    finally:
        player_thread = None


def start_playlist(song_list, loop=False):
    global player_thread

    if player_thread is not None and player_thread.is_alive():
        stop_event.set()
        player_thread.join(timeout=0.5)

    stop_event.clear()
    valid_songs = get_valid_songs(song_list)

    if not valid_songs:
        print("Your playlist is empty or all files are missing.")
        return

    player_thread = threading.Thread(
        target=play_playlist_thread,
        args=(valid_songs, loop),
        daemon=True
    )
    player_thread.start()


while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        start_playlist(playlist[:1], loop=False)

    elif choice == "2":
        start_playlist(playlist, loop=False)

    elif choice == "3":
        start_playlist(playlist, loop=True)

    elif choice == "4":
        if player_thread is not None and player_thread.is_alive():
            stop_event.set()
            print("Playback stopped.")
        else:
            print("No song is currently playing.")

    elif choice == "5":
        if player_thread is not None and player_thread.is_alive():
            stop_event.set()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose again.")
