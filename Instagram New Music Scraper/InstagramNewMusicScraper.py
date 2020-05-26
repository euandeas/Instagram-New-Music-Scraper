from InstagramScraper import InstagramScraper

scraper = InstagramScraper()
data = scraper.scrapedata(20)
del scraper

print(data)