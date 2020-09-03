import requests, json, random
from bs4 import BeautifulSoup
from bingsearchpy.useragent import useragent

class BingSearch:

    def __init__(self):
        self.data = []
        self.page = 0

    
    def request_data(self, url):

        try:
            # request data
            no = random.randint(0,len(useragent) - 1)
            page = 1
            req = requests.get(url, headers={"User-Agent": useragent[no]}).content

            # start scraping data
            soup = BeautifulSoup(req, 'html.parser')
            result_count = soup.find('span', class_ = 'sb_count').get_text().split(' ')[0].split(',')
            if len(result_count) > 0:
                container_count = ""
                for count in result_count:
                    container_count += str(count)
                # final_count = int(container_count)
                # self.page = final_count

            # parsing data ( title, link, description )
            final_data = []
            index = 0
            for data in soup.find_all(class_ = 'b_algo'):
                index += 1
                main = data.find('h2').find('a')
                list_data = {}
                list_data['no'] = index
                list_data['title']  = main.get_text()
                list_data['link']   = main.attrs['href']
                final_data.append(list_data)
            return final_data
        except:
            pass
        

    def search(self, query):
        """
        search data with random user agent
        """
        url = "https://www.bing.com/search?q=" + query + "&first="
        index = 1
        res = []
        for i in range(1,5):
            try:
                for data in self.request_data(url + str(i)):
                    res.append(data)
            except:
                pass
        return res

if __name__ != "__main__":
    engine = BingSearch()
else:
    pass