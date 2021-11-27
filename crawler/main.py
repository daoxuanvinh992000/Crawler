import sys
from crawler import start_crawler
from service import job_to_object

def search_jobs(args):
    print(args)
    web_name = ''
    if len(args) >=2:
        web_name = args[1]
        
    jobs, url = start_crawler(web_name)
    if not len(jobs): 
        print("not found")
    else:
       job_to_object(jobs, url)

if __name__ == '__main__':
    search_jobs(sys.argv)