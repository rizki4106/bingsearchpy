import requests, json, random
from bs4 import BeautifulSoup
from bingsearchpy.useragent import useragent

class BingSearch:

    def __init__(self):
        self.data = []
        self.page = 0

    def get_total_page(self, url):

        no = random.randint(0,len(useragent) - 1)
        req = requests.get(url, headers={"User-Agent": useragent[no]}).content
        soup = BeautifulSoup(req, 'html.parser')
        result_count = soup.find('span', class_ = 'sb_count').get_text().split(' ')[0].split(',')
        pages_count = ''
        for page in result_count:
            pages_count += str(page)
        self.page = int(pages_count)

    
    def request_data(self, url):
        """
        used for request data and DO NOT USE this method directly from your code
        """
        no = random.randint(0,len(useragent) - 1)
        user_agent = useragent[no]
        try:
            # get total search result
            self.get_total_page(url)

            # handling large data
            repeat = 0
            if self.page >= 20:
                repeat = 20
            else:
                repeat = self.page

            # generating search result
            for i in range(1,repeat):
                # request data
                
                req = requests.get(url + "&first=" + str(i), headers={"User-Agent": user_agent}).content

                # start scraping data
                soup = BeautifulSoup(req, 'html.parser')
                result_count = soup.find('span', class_ = 'sb_count').get_text().split(' ')[0].split(',')

                # parsing data ( title, link, description )

                for data in soup.find_all(class_ = 'b_algo'):
                    main = data.find('h2').find('a')
                    list_data = {}
                    list_data['no'] = i
                    list_data['title']  = main.get_text()
                    list_data['link']   = main.attrs['href']
                    yield list_data

        except:
            pass

    def search(self, query):
        """
        search data with random user agent.
        query : what kind topic that you want to find
        """
        url = "https://www.bing.com/search?q=" + query
        return self.request_data(url)

if __name__ != "__main__":
    engine = BingSearch()
else:
    pass