import datetime
import urllib.request
'''
Command line program that repeatedly accepts accepts URL as input, and prints out the HTML data as output
Todo: add caching
'''
class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()


cache = {} #key is the URL, the value is the data from that URL
TIMEOUT_SECONDS = 10

while True:
    url = input("Enter a URL: ")
    if url == 'exit':
        break
    needs_refresh = False
    if url not in cache:
        needs_refresh = True
    else:
        #did it timeout?
        cur_time = datetime.datetime.now().timestamp()
        diff_time = cur_time - cache[url].timestamp
        '''
        if diff_time > TIMEOUT_SECONDS:
            needs_refresh = True
        '''
        needs_refresh = diff_time > TIMEOUT_SECONDS

    if needs_refresh:
        print("GETTING FROM SERVER")
        resp = urllib.request.urlopen(url)
        data = resp.read()
        cache[url] = CacheEntry(url, data)

        # print('CACHE MISS')
        # resp = urllib.request.urlopen(url)
        # data = resp.read()
        # cache[url] = data
    print(cache[url].data[:60]) # it prints only the first 60 bytes
    # else:
    #     print('CACHE HIT')
    print(data.decode()) #it formats it 
   