import feedparser

def main():
    d = feedparser.parse('https://anchor.fm/s/68c27b4/podcast/rss')
    e = d.entries[0]
    print(e)
    print(e.title)
    print(e.published)
    print(e.link)
    print(e.links[0])
    print(e.description)
    print("\n")  # 2 newlines


if __name__ == "__main__":
  main()
