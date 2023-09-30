import feedparser

def read_rss_feed(rss_url):
    try:
        feed = feedparser.parse(rss_url)
        if feed.entries:
            print("Latest News Headlines:")
            for entry in feed.entries:
                print(f"- {entry.title}")
                print(f"  Link: {entry.link}")
                print()
        else:
            print("No news entries found in the RSS feed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Input the RSS feed URL
rss_url = input("Enter the URL of the RSS feed: ")

# Read and display the latest news
read_rss_feed(rss_url)
