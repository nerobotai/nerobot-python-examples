import requests

class NeroBotClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.nero.ai/v1"
        
    def _send_request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.request(method, url, headers=headers, json=data)
        return response.json()

    def extract_data(self, data):
        return self._send_request('POST', '/extract/data', data)

    def create_bulk_job(self, data):
        return self._send_request('POST', '/bulk/create', data)

    def get_bulk_results(self, job_id, data):
        return self._send_request('POST', f'/bulk/retrieve/{job_id}', data)

    def get_job_detail(self, job_id):
        return self._send_request('GET', f'/job_detail/{job_id}')

    def update_bulk_job(self, job_id, data):
        return self._send_request('PUT', f'/bulk/{job_id}', data)

    def delete_bulk_job(self, job_id):
        return self._send_request('DELETE', f'/bulk/{job_id}')
    
    def create_crawl_job(self, data):
        return self._send_request('POST', '/crawl/create', data)

    def get_crawl_job_status(self, job_id):
        return self._send_request('GET', f'/crawl/{job_id}')

    def update_crawl_job(self, job_id, data):
        return self._send_request('PUT', f'/crawl/{job_id}', data)

    def delete_crawl_job(self, job_id):
        return self._send_request('DELETE', f'/crawl/{job_id}')

    def get_crawl_results(self, job_id, data):
        return self._send_request('POST', f'/crawl/retrieve/{job_id}', data)