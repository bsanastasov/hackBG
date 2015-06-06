import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, url):
        self.url = url
        self.internal_link = set()
        self.external_link = set()
        self.visited = set()

    def start(self):
        links = self.get_links_from_url(self.url)
        self.classify(links)
        self.visited.add(self.url)

        for link in self.internal_links:
            print link
            if link not in self.visited:
                self.visited.add(link)
                sub_pages = self.get_links_from_url(link)
                self.classify(sub_pages)



    def get_links_from_url(self, url):
        try:
            r = requests.get(url)
            r.text

            soup = BeautifulSoup(r.text)

            links = set()

            for link in soup.find_all('a'):
                links.add(link.get('href'))

        except:
            print "Greshka!"

        return links

    def classify(self, links):
        for link in links:
            if link is None:
                continue

            if "start.bg" in link:
                internal.add(link)
            elif "link.pho?" in link:
                external.add(link)

        return internal





def main():
    crawler = Crawler("http://www.start.bg/")
    crawler.start()

if __name__ == '__main__':
    main()



