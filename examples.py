
#%%
from client import NeroBotClient

## Initialize the client
api_key = 'INSERT KEY'
client = NeroBotClient(api_key)

#%%
##Extract data from a single url
data = {
    "url": "https://www.fema.gov/appeal/result-declared-incident-59",
}
extract_response = client.extract_data(data)

print(extract_response)

#%%
## Create a bulk job
bulk_data = {
    "job_name":"Eval",
    "urls": [
        "https://edition.cnn.com/2023/09/21/politics/house-government-shutdown-negotiations-latest/index.html",
        "https://support.apple.com/guide/iphone/setup-basics-iph9374b7411/17.0/ios/17.0",
        "https://www.fema.gov/appeal/result-declared-incident-59"
    ],
    "notify": {
        "email": "kagen@nero.ai",  # Optional: Replace with your email if you want email notifications
    }
}

## Create the bulk job
bulk_create_response = client.create_bulk_job(bulk_data)
print(bulk_create_response)

#%%
## Get bulk job status
bulk_status_response = client.get_job_detail(bulk_create_response['job_id'])
print(bulk_status_response)

#%%
## Retrieve bulkresults
# Offset up and down are optional parameters to specify the range of results to return.

params = {
  "format_params": {
    "format": "json",
    "return_cleaned_html": True,
    "return_markdown_html": False,
    "return_text": False
  },
    "json_params": {
    "offset_down": 0,
    "offset_up": 10000
  }
}

# bulk_result_response = client.get_bulk_results(bulk_create_response['job_id'],params)
bulk_result_response = client.get_bulk_results('779',params)
print(bulk_result_response['results']['data'])




#%% 
"""
Previewing the agent will not crawl the website, but will show you the AI Crawl Assistant's plan for links to crawl.

If Skip Assistant is set to true it will defualt to the our frontend crawler and do basic pattern matching based on the seed urls

"""

#Create a crawl job with assistant
crawl_data = {
  "assistant_prompt":"crawl learn.getodin.ai, in english",
  "preview_agent": False,
  "skip_assistant": False,
  "job_name":"Eval test"
}
crawl_create_response = client.create_crawl_job(crawl_data)
print(crawl_create_response)
#%%
## Get crawl job status
crawl_status_response = client.get_job_detail(crawl_create_response['job_id'])
print(crawl_create_response)

#%%
## Retrieve crawl results
params = {
  "format_params": {
    "format": "json",
    "return_cleaned_html": True,
    "return_markdown_html": False,
    "return_text": False
  },
    "json_params": {
    "offset_down": 0,
    "offset_up": 10000
  }
}

bulk_result_response = client.get_crawl_results(crawl_create_response['job_id'],params)
# bulk_crawl_response = client.get_crawl_results('871',params)
print(bulk_crawl_response['results']['data'])

