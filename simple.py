import vlc

def main():
    player = vlc.MediaPlayer("/home/hamza/Videos/test.webm")
    player.play()
    input("Press Enter to quit...")

if __name__ == "__main__":
    main()
