import time
import requests

def time_measure(func):
    def wrapper():
        startTime = time.time()
        res = func()
        print("The function was performed for:", time.time() - startTime, "sec")
        return res
    return wrapper


@time_measure
def checkGitHub():
    response = requests.get('https://api.github.com')
    print("GitHub status code is:", response.status_code)


checkGitHub()


