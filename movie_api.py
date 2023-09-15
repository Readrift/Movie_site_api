import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "Your Key"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResult(self, keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMovieDb()

while True:
    choose = input("-----------MENU------------\n1-Popular Movies\n2-Search\n3-Exit\nChoose: ")
    
    if choose =="3":
        break
    else:
        if choose =="1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        
        if choose =="2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResult(keyword)
            for movie in movies['results']:
                print(movie['name'])






































