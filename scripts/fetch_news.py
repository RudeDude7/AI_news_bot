import urllib.request
import xml.etree.ElementTree as ET
import ssl
import json
import os

def fetch_ai_news():
    # 1. Define the Google News RSS URL
    rss_url = "https://news.google.com/rss/search?q=artificial+intelligence&hl=en-US&gl=US&ceid=US:en"
    
    try:
        # 2. Fetch the RSS feed using urllib
        # Use a User-Agent header to avoid being blocked
        context = ssl._create_unverified_context()
        req = urllib.request.Request(rss_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=context) as response:
            xml_data = response.read()
            
        # 3. Parse the XML response
        root = ET.fromstring(xml_data)
        
        # 4. Extract titles and links
        # Find all 'item' elements in the RSS feed
        items = root.findall('.//item')
        
        # 5. Format the top 5 news items as a list of dictionaries
        news_data = []
        for item in items[:5]:
            title = item.find('title').text
            link = item.find('link').text
            news_data.append({"title": title, "link": link})
            
        # 6. Ensure 'data' directory exists and save to JSON
        os.makedirs("data", exist_ok=True)
        with open("data/news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, indent=4)
            
        print("Successfully saved top 5 AI news to data/news.json")
            
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    fetch_ai_news()

if __name__ == "__main__":
    main()
