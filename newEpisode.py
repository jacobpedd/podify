import feedparser


# date:   2019-01-18
# categories: podcast
# permalink: https: // atp.fm/episodes/361
# podcast_link: http: // traffic.libsyn.com/atpfm/atp361.mp3
# podcast_duration: "02:12:27"
# podcast_length: 13654375

def main():
    d = feedparser.parse('https://anchor.fm/s/68c27b4/podcast/rss')
    e = d.entries[0]
    print(e.title)
    print("\n")  # 2 newlines


if __name__ == "__main__":
  main()
