import csv, sys

podcast_csv = open('podcastInfo.csv')
rss_file = open('rssFeed.txt', 'w')

podreader = csv.reader(podcast_csv, delimiter=',')

rss_links = [line[6] for line in podreader if len(line) >= 7]

for rss in rss_links:
	rss_file.write(f'{rss}\n')