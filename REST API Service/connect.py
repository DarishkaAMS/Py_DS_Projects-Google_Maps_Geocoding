import requests
import pprint
api_key = "9db581b66af3875cd0f60398f7e45671"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ZGI1ODFiNjZhZjM4NzVjZDBmNjAzOThmN2U0NTY3MSIsInN1YiI6IjVmOTc5ZDMyZDJmNWI1MDAzYTdlYjE2MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.H1mCVcN4474KHzCW6nLmGB9gNz073JdXw4T8pwuo9xk"

# HTTP Requests
# What's our endpoint // a url?
# What HTTP method will we need?

'''
Endpoint 
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=9db581b66af3875cd0f60398f7e45671
'''

# Using v3
movie_id = 500
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}'
# print(endpoint)
# r = requests.get(endpoint) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)

# Using v4
movie_id = 501
api_version = 4
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{api_base_url}{endpoint_path}' # ?api_key={api_key}'
# print(endpoint)
# headers = {
#     'Authorization': f'Bearer {api_key_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }
# r = requests.get(endpoint, headers=headers) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)

api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie'
search_query = 'The Matrix'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&' \
           f'query={search_query}'
pprint.pprint(endpoint)
r = requests.get(endpoint)
pprint.pprint(r.json())