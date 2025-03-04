import json

def max_revenue(movies):
    max_revenue = 0
    max_name = ''
    for movie in movies:
        movie_json = open(f'data/movies/{movie["id"]}.json', encoding = 'utf-8')
        movie_info = json.load(movie_json)
        if movie_info['revenue'] > max_revenue:
            max_revenue = movie_info['revenue']
            max_name = movie_info['title']
    return max_name
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
