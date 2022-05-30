


import requests
from bs4 import BeautifulSoup

def extract_inform_wework(name='python'):
    job_list = list()
    URL_WEWORK = f"https://weworkremotely.com/remote-jobs/search?utf8=✓&term={name}"
    page_result = requests.get(URL_WEWORK)
    soup = BeautifulSoup(page_result.text, 'html.parser')
    results = soup.find_all("section", class_="jobs")
    for result in results:
        jobs = result.find_all("li", class_="feature")
        for job in jobs:
            job = extract_job(job)
            job_list.append(job)
    return job_list

def extract_job(job):
    URL = "https://weworkremotely.com"
    NEXT_URL = URL+job.find_all("a")[1]['href']
    company_name = job.find("span",class_="company").get_text()
    job_name = job.find("span", class_="title").get_text()
    return {'title': job_name,
            'company': company_name,
            'link': NEXT_URL}