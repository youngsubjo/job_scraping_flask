


import requests
from bs4 import BeautifulSoup


def extract_inform_remote(name='python'):
    URL = "https://remoteok.com"
    jobs = list()
    URL_REMOTE = f"https://remoteok.com/remote-{name}-jobs"
    #headers inform : http://www.useragentstring.com/ This is pervent from 503 error
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
    page_result = requests.get(URL_REMOTE, headers=headers)
    soup = BeautifulSoup(page_result.text, 'html.parser')
    result = soup.find("div",class_="page")
    results = result.find_all("tr", class_="job")
    for result in results:
        NEXT_URL = URL + result["data-url"]
        company_name = result.find("h3",itemprop="name").get_text()
        job_name = result.find("h2",itemprop="title").get_text()
        job = extract_job(result)
        jobs.append(job)
    return jobs

def extract_job(result):
    URL = "https://remoteok.com"
    NEXT_URL = URL + result["data-url"]
    company_name = result.find("h3",itemprop="name").get_text()
    job_name = result.find("h2",itemprop="title").get_text()
    return {'title': job_name,
            'company': company_name,
            'link': NEXT_URL}