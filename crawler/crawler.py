from models import services

from helper import get_bs_object, call_request

def services2jobs(service):
    bs = get_bs_object(service.jobs_url)
    if bs:
        jobs = bs.select('div[id="jobs"]')
        jobs = jobs[0].select('div[class="job"]')
    return jobs

def start_crawler(web_name, tags=None, company=None):
    jobs=[]
    web_url = ''
    for service in services:
        try:
            if(service.name == web_name):
                service_jobs = services2jobs(service)
                web_url = service.jobs_url
                jobs.extend(service_jobs)
        except Exception:
            print('err: ', Exception)

    return jobs, web_url

# 3 method beautiful soup hay sử dụng
# .select(selector)  select('h3[class='abc']')
#.get_text()
#  attrs

# Lấy ra thông tin obj 
# Mỗi job có 1 thuộc tính service
# Làm thêm về vietnamwork
# tổ chức lại code

