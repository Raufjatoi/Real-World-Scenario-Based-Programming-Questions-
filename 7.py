# 7. Basic Music Player: Develop a program to act as a simple music player. It should allow users to
# browse and select music files from their device. The program should play the selected music file,
# pause or stop playback, and adjust the volume.

songs = [
    {'name': 'Breezeblocks', 'artist': 'Alt-J', 'album': 'An Awesome Wave', 'year': '2012'},
    {'name': 'Ho Hey', 'artist': 'The Lumineers', 'album': 'The Lumineers', 'year': '2012'},
    {'name': 'Riptide', 'artist': 'Vance Joy', 'album': 'Dream Your Life Away', 'year': '2013'},
    {'name': 'Skinny Love', 'artist': 'Bon Iver', 'album': 'For Emma, Forever Ago', 'year': '2007'},
    {'name': 'Say Something', 'artist': 'A Great Big World ft. Christina Aguilera', 'album': 'Is There Anybody Out There?', 'year': '2013'},
    {'name': 'All I Want', 'artist': 'Kodaline', 'album': 'In a Perfect World', 'year': '2013'},
    {'name': 'Lost Cause', 'artist': 'Billie Eilish', 'album': 'Don\'t Smile at Me', 'year': '2017'},
    {'name': 'Cherry Wine', 'artist': 'Hozier', 'album': 'Hozier', 'year': '2014'},
    {'name': 'Fix You', 'artist': 'Coldplay', 'album': 'X&Y', 'year': '2005'},
    {'name': 'Hollow', 'artist': 'Tori Kelly', 'album': 'Unbreakable Smile', 'year': '2015'},
    {'name': 'Wicked Game', 'artist': 'James Vincent McMorrow', 'album': 'Early in the Morning', 'year': '2010'},
    {'name': 'Slow Dancing in a Burning Room', 'artist': 'John Mayer', 'album': 'Continuum', 'year': '2006'},
    {'name': 'Breathe Me', 'artist': 'Sia', 'album': 'Colour the Small One', 'year': '2004'},
    {'name': 'Landslide', 'artist': 'Fleetwood Mac', 'album': 'Fleetwood Mac', 'year': '1975'},
    {'name': 'Someone You Loved', 'artist': 'Lewis Capaldi', 'album': 'Divinely Uninspired to a Hellish Extent', 'year': '2019'},
    {'name': 'Make It Rain', 'artist': 'Ed Sheeran', 'album': 'x', 'year': '2014'},
    {'name': 'Another Love', 'artist': 'Tom Odell', 'album': 'Long Way Down', 'year': '2012'},
    {'name': 'Liability', 'artist': 'Lorde', 'album': 'Melodrama', 'year': '2017'},
    {'name': 'Stay', 'artist': 'Rihanna ft. Mikky Ekko', 'album': 'Unapologetic', 'year': '2012'},
    {'name': 'Happier', 'artist': 'Ed Sheeran', 'album': '÷', 'year': '2017'}
]

def play():
    c = input('Enter the song name to play : ').capitalize()
    found = False
    for s in songs:
        if s['name'] == c:
            found = True
            print(f'Playing {s["name"]} song by {s["artist"]}')
            volume = 7
            duration = '3.00 min'
            print(f'Volume is {volume} and duration is {duration}')
            print('You can type "p" to pause ⏸, "+" to volume up 🔊, "-" to volume down 🔈, or any other key to quit')
            while True:
                choice = input('Enter choice: ')
                if choice == 'p':
                    print('Music is paused')
                elif choice == '+':
                    volume += 1
                    print(f'Volume is 1 point up. New volume is {volume}')
                elif choice == '-':
                    volume -= 1
                    print(f'Volume is one point down. New volume is {volume}')
                else:
                    break
    if not found:
        print('Song not found in your playlist')

def view():
    print('Songs 🎶 ')
    for s in songs:
        print(f"Song: {s['name']}, by {s['artist']}, album: {s['album']}, year: {s['year']}")

def main():
    while True:
        print('\t\t\t 🎵 SIMPLE MUSIC PLAYER 🎼')
        view()
        s = input('Enter "p" to play something or anything else to quit: ')
        if s == 'p':
            play()
        else:
            print('BYE Bye 🙋‍♂️')
            break

if __name__ == '__main__':
    main()