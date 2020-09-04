from bingsearchpy.controller import Controller


class BingSearch(Controller):

    def search(self, query):
        """
        search data with random user agent.
        query : what kind topic that you want to find
        """

        url = "https://www.bing.com/search?q=" + query
        return self.request_data(url)
    def search_image(self, query):
        return self.get_image(query)


if __name__ != "__main__":
    engine = BingSearch()
else:
    pass