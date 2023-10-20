import requests
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzRjMzE3NWJjMGExNzNiMDkwZjkyZTljMjQ3NzRmNyIsInN1YiI6IjY0NzBlM2NmNzcwNzAwMDBkZjE0MDFjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Y3zfcONHo2VXJV_CQbXmR56Kw0YqR296Bvqz_HbcbGU"
}

def get_upcoming(page=3):
    global headers
    url = f"https://api.themoviedb.org/3/movie/upcoming?language=en-US&page={page}"
    response = requests.get(url, headers=headers)

    if response.status_code==200:
        data=response.json()
        return data.get('results')
    return[]

# def get_images_base_path():
#     global headers
#     url = "https://api.themoviedb.org/3/configuration"
#     response = requests.get(url, headers=headers)

#     if response.status_code==200:
#         data=response.json()
#         return data.get('images').get('base_url')
#     return('')

def get_popular(page=1):
    global headers
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json()
        return data.get('results')
    return []


# d=get_upcoming()
# b=get_images_base_path()