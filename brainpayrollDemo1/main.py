from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Initialize the WebDriver
driver = webdriver.Chrome()

target_urls = [
    "https://www.brainpayroll.co.uk/",
    "https://www.brainpayroll.co.uk/partner",
    "https://www.brainpayroll.co.uk/successstories",
    "https://www.brainpayroll.co.uk/testimonials",
    "https://www.brainpayroll.co.uk/blog/",
    "https://www.brainpayroll.co.uk/faq",
    "https://www.brainpayroll.co.uk/bureau-feature",
    "https://www.brainpayroll.co.uk/support"
]

text = ""
for url in target_urls:
    driver.get(url)

    # Wait for the page to load (adjust the timeout as needed)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Expand all FAQ questions if present
    if 'faq' in url or 'support' in url:
        faq_buttons = driver.find_elements(By.CSS_SELECTOR, 'a.faq-btn')
        for button in faq_buttons:
            try:
                driver.execute_script("arguments[0].click();", button)
                # Wait for the answer to be visible
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.collapse.show')))
            except Exception as e:
                print(f"Could not click button: {e}")

    # Get the page source after expanding the FAQs
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for header in soup.find_all(['h1', 'h2', 'h3']):
        text += header.get_text() + "\n"
    for paragraph in soup.find_all('p'):
        text += paragraph.get_text() + "\n"
    for div in soup.find_all('div', class_='card card-body'):
        text += div.get_text() + "\n"

with open('website_text.txt', 'w') as text_file:
    text_file.write(text)

print("Text extracted successfully")

driver.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# # Configure Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Ensure GUI is off
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# # Set up the WebDriver (no need to specify the path)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# target_urls = [
#     "https://www.brainpayroll.co.uk/",
#     "https://www.brainpayroll.co.uk/partner",
#     "https://www.brainpayroll.co.uk/successstories",
#     "https://www.brainpayroll.co.uk/testimonials",
#     "https://www.brainpayroll.co.uk/blog/",
#     "https://www.brainpayroll.co.uk/faq",
#     "https://www.brainpayroll.co.uk/bureau-feature",
#     "https://www.brainpayroll.co.uk/support"
# ]

# text = ""
# for url in target_urls:
#     driver.get(url)

#     # Wait for the page to load (adjust the timeout as needed)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

#     # Expand all FAQ questions if present
#     if 'faq' in url:
#         faq_items = driver.find_elements(By.CSS_SELECTOR, '.faq-btn')
#         for item in faq_items:
#             try:
#                 item.click()
#                 WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.faq-answer')))
#             except Exception as e:
#                 print(f"Could not click item: {e}")

#     # Get the page source after expanding the FAQs
#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     for paragraph in soup.find_all('h1'):
#         text += paragraph.get_text() + "\n"
#     for paragraph in soup.find_all('h2'):
#         text += paragraph.get_text() + "\n"
#     for paragraph in soup.find_all('p'):
#         text += paragraph.get_text() + "\n"

# with open('website_text.txt', 'w') as text_file:
#     text_file.write(text)

# print("Text extracted successfully")

# driver.quit()







# import requests
# from bs4 import BeautifulSoup

# target_url=[
#     "https://www.brainpayroll.co.uk/",
#     "https://www.brainpayroll.co.uk/partner",
#     "https://www.brainpayroll.co.uk/successstories",
#     "https://www.brainpayroll.co.uk/testimonials",
#     "https://www.brainpayroll.co.uk/blog/",
#     'https://www.brainpayroll.co.uk/faq',
#     "https://www.brainpayroll.co.uk/bureau-feature",
#     "https://www.brainpayroll.co.uk/support"]

# text=""
# for url in target_url:
#     response=requests.get(url)

#     if response.status_code==200:
#         soup=BeautifulSoup(response.content,'html.parser')
#         #text=""
#         for paragraph in soup.find_all('h1'):
#             text+=paragraph.get_text()
#         for paragraph in soup.find_all('h2'):
#             text+=paragraph.get_text()
#         for paragraph in soup.find_all('p'):
#             text+=paragraph.get_text()

#         with open('website_text.txt','w') as text_file:
#             text_file.write(text)

#         print("Text extracted successfully")

#     else:
#         print(f"Error:Failed to retrive website content.status code.{response.status_code}")










# import requests
# from bs4 import BeautifulSoup

# target_url="https://www.brainpayroll.co.uk/"

# response=requests.get(target_url)

# if response.status_code==200:
#     soup=BeautifulSoup(response.content,'html.parser')
#     text=""
#     for paragraph in soup.find_all('p'):
#         text+=paragraph.get_text()

#     with open('website_text.txt','w') as text_file:
#         text_file.write(text)

#     print("Text extracted duccessfully")

# else:
#     print(f"Error:Failed to retrive website content.status code.{response.status_code}")


# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import time

# visited_urls = set()
# base_url = "https://www.brainpayroll.co.uk/"

# def extract_text_from_tags(soup, tags):
#     text = ""
#     for tag in tags:
#         for element in soup.find_all(tag):
#             text += element.get_text() + "\n"
#     return text

# def crawl_and_extract(url, tags):
#     global visited_urls
#     if url in visited_urls or not url.startswith(base_url):
#         return ""
#     visited_urls.add(url)
#     time.sleep(1)  # To prevent overloading the server
    
#     response = requests.get(url)
#     if response.status_code != 200:
#         print(f"Error: Failed to retrieve content from {url}. Status code: {response.status_code}")
#         return ""
    
#     soup = BeautifulSoup(response.content, 'html.parser')
#     text = extract_text_from_tags(soup, tags)
    
#     for link in soup.find_all('a', href=True):
#         full_url = urljoin(base_url, link['href'])
#         text += crawl_and_extract(full_url, tags)
    
#     return text

# tags_to_extract = ['p', 'h1', 'h2', 'h3', 'a', 'li']
# all_text = crawl_and_extract(base_url, tags_to_extract)

# with open('website_text.txt', 'w') as text_file:
#     text_file.write(all_text)

# print("Text extracted successfully")
