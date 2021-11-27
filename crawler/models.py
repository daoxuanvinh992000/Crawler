class Service:

    def __init__(self, name, job_url, root_url=None) -> None:
        self.name = name
        self.jobs_url = job_url
        self.root_url = get_root_url(job_url)

def get_root_url(job_url):
    return job_url

services = [
    Service('Itviec', 'https://itviec.com/it-jobs'),
    Service('vietnamworks', ' https://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam')
]


class Job:

    def __init__(self) -> None:
        pass