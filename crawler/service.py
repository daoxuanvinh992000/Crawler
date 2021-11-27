from urllib.parse import urljoin
def job_to_object(jobs, url):
    job_convert = []
    for job in jobs:
        job_obj = {}
        # job_obj['image_src'] = job.select('div[class="logo"]')
        images = job.find('img')
        job_obj['image_src'] = images['data-src']
        job_link = job.select('h3[class="title"]')[0].find('a')
        job_obj['title'] = job_link.get_text()
        job_obj['link'] = urljoin(url, job_link['href'])
        job_obj['address'] = job.select('div[class="address"] span')[0].get_text()
        job_obj['distance-time'] = job.select('div[class="distance-time-job-posted"] span')[0].get_text().replace('\n', '')
        tag = []
        tag_lists = job.select('div[class="tag-list"] a')
        for tag_list in tag_lists:
            tag.append(tag_list.select('span')[0].get_text().replace('\n', ''))

        job_obj['tag'] = tag
        job_convert.append(job_obj)
    
    print(job_convert)
    return job_convert