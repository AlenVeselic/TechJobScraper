import requests, bs4, json

urls = {
    "https://slo-tech.com/delo":[".forums tbody tr", ".name", ".company", ".last_msg"]
    "https://www.mojedelo.com/prosta-delovna-mesta/racunalnistvo-programiranje/vse-regije?p=1":".job-ad"
}

listing = {}

for url in urls.keys():
    listing[url] = {}
    response = requests.get(url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    
    jobs = soup.select(urls[url])
    jobNum = 0
    for job in jobs:
        
        listing[url]["job" + str(jobNum)]=[]
        listing[url]["job" + str(jobNum)].append(job.select_one(".name").text)
        listing[url]["job" + str(jobNum)].append(job.select_one(".company").text)
        listing[url]["job" + str(jobNum)].append(job.select_one(".last_msg").text)
        jobNum = jobNum + 1
    

    print(json.dumps(listing))

