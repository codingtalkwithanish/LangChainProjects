import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrap_linkedin_profile(linkedin_profile_url:str,mock:bool=False):
    """scrape information from the linkedin profiles,
    Manually scrape the information from the linkedin profile"""

    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/codingtalkwithanish/03c4efe297448b9f87c86c31de1879ea/raw/600fe99def27dee654d1e100242dbf66745d34f0/anish-singh.json"
        response=requests.get(linkedin_profile_url,timeout=10)

    else:
        api_key = os.environ.get("api_key")
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
        #'linkedin_profile_url': 'https://www.linkedin.com/in/anish-singh-32586540/',
        'url':linkedin_profile_url,
        'github_profile_id': 'include',
        'personal_email': 'include',
        'inferred_salary': 'include',
        'skills': 'include',
        'use_cache': 'if-present',
        'fallback_to_cache': 'on-error',
        }
        response = requests.get(api_endpoint,
        params=params,
        headers=headers,timeout=10)
    
    data=response.json()
    
    
    data={k:v for k,v in data.items() if v not in ([],"",None) and k not in ["people_also_viewed"] }

    if data.get("groups"):      
         for group_dict in data.get("groups"):
              group_dict.pop("profile_pic_url")
    return data

if __name__=="__main__":
    print(
        scrap_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/anish-singh-32586540/",mock=True)
          )