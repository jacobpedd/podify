import feedparser
from datetime import date as dt


# date:   2019-01-18
# categories: podcast
# permalink: https: // atp.fm/episodes/361
# podcast_link: http: // traffic.libsyn.com/atpfm/atp361.mp3
# podcast_duration: "02:12:27"
# podcast_length: 13654375

def main():
    d = feedparser.parse('http://sellingthecouch.libsyn.com/rss')
    e = d.entries[0]
    print(e.title)
    print("\n")  # 2 newlines


def addPost():
    title = "Perspectives: Human Trafficking"
    date = "Thu, 09 Jan 2020 05:00:00 +0000"
    link = "https://news.wfsu.org/post/perspectives-human-trafficking-2"
    file = "https://cpa.ds.npr.org/wfsu/audio/2020/01/ps200109_cleaned.mp3"
    length = "3019"
    duration = "3019"

    today = dt.today()
    d1 = today.strftime("%Y-%m-%d")
    f = open("_posts/{}-{}.md".format(d1, title), "w+")
    f.write("---\n")
    f.write("layout: null\n")
    f.write('title: "{}"\n'.format(title))
    f.write("date: {}\n".format(date))
    f.write("permalink: {}\n".format(link))
    f.write("podcast_link: {}\n".format(file))
    f.write("podcast_duration: {}\n".format(duration))
    f.write("podcast_length: {}\n".format(length))
    f.write("---")
    f.close()



if __name__ == "__main__":
  addPost()
