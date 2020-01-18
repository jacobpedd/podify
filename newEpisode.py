import feedparser, csv, random


# date:   2019-01-18
# title:	Tim Roty Eats His Own Shit: Part II
# categories: podcast
# permalink: https: // atp.fm/episodes/361
# podcast_link: http: // traffic.libsyn.com/atpfm/atp361.mp3
# podcast_duration: "02:12:27"
# podcast_length: 13654375
# description: Time Roty shits into a cup and eats it!

def main():
    # get a random rss feed from the podcast info file
    lines = open('rssFeed.txt').read().splitlines()
    rss_link = random.choice(lines)

    d = feedparser.parse(f'{rss_link.strip()}')

    # latest episode
    e = d.entries[0]

    episode_data = {}
    episode_data['title'] = e.title
    episode_data['date'] = e.published
    episode_data['permalink'] = e.link
    episode_data['podcast_link'] = e.links[1]['href']
    episode_data['podcast_duration'] = e.itunes_duration
    episode_data['podcast_length'] = e.links[1]['length']
    episode_data['description'] = e.description
    
    print(episode_data)

if __name__ == "__main__":
  main()
