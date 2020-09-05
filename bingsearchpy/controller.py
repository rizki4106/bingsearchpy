import requests, json, random
from bs4 import BeautifulSoup
from bingsearchpy.useragent import useragent
from time import sleep


class Controller:

    def __init__(self):
        self.data = []
        self.page = 0
        self.user_agent = random.randint(0,len(useragent) - 1)

    def get_total_page(self, url):

        req = requests.get(url, headers={"User-Agent": useragent[self.user_agent]}).content
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

    
    # search image
    def get_image(self, query):
        """
        searching for images
        """
        # get image in 20 pages
        for i in range(1,20):
            url = 'https://www.bing.com/images/search?q={}&first={}&scenario=ImageBasicHover'.format(query, str(i))
            req = requests.get(url, headers={'User-Agent': useragent[self.user_agent]})
            soup = BeautifulSoup(req.content, 'html.parser')
            for data in soup.find_all('div', class_ = 'imgpt'):
                res = {}
                main_component = data.find('a').attrs['m']
                res['link'] = main_component.split('murl')[1].split('"')[2]
                res['title'] = main_component.split('desc')[1].split('"')[2]
                yield res
                
    
    # search video

    def get_video(self, query):
        """
        searching for video
        """
        # get video in 20 pages
        for i in range(1,20):
            url = 'https://www.bing.com/videos/search?q={}&first={}'.format(query, str(i))
            req = requests.get(url, headers={'User-Agent': useragent[self.user_agent]})
            soup = BeautifulSoup(req.content, 'html.parser')
            for data in soup.find_all('div', class_ = 'mc_vtvc_con_rc'):
                try:
                    res = {}
                    main_component = data.find('div', class_ = 'vrhdata').attrs['vrhm']
                    res['title'] = main_component.split("vt")[1].split('"')[2]
                    res['snippet_video'] = main_component.split("smturl")[1].split('"')[2]
                    res['detail_video'] = main_component.split('pgurl')[1].split('"')[2]
                    yield res
                except:
                    pass
                    