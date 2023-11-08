import requests
def get(url):
  return requests.get(url).status_code
