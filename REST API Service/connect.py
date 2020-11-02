import requests
api_key = "9db581b66af3875cd0f60398f7e45671"

# HTTP Requests
# What's our endpoint // a url?
# What HTTP method will we need?

'''
Endpoint 
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=9db581b66af3875cd0f60398f7e45671
'''

movie_id = 500
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/movie/{movie_id}'
endpoint = f'{api_base_url}{endpoint_path}'
r = requests.get(endpoint)
print(r.status_code)