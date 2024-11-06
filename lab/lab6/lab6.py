#importam nebuniile
import requests
from bs4 import BeautifulSoup
import re

#site-ul cu pricina pentru scraping
req = requests.get('https://books.toscrape.com')

#verificam daca merge conexiunea
response = req
if response.status_code == 200:
    print("Webpage retrieved successfully.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

#exercitiul 1
print("--------exercise1--------")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    link_text = soup.find('a', href="index.html").get_text(strip=True)
    print("Link text:", link_text)
    
    small_text = soup.find('small').get_text(strip=True)
    print("Small text:", small_text)

#exercitiul 2
    print("--------exercise2--------")
    page_info = soup.find('li', class_='current')
    
    page_text = page_info.get_text(strip=True) if page_info else "No page info found"
    print("Page info:", page_text)

#exercitiul 3
    print("--------exercise3--------")
    button = soup.find('button') 
   
    button_text = button.get_text(strip=True) if button else "No button found"
    print("Button text:", button_text)

#exercitiul 4
    print("--------exercise4--------")
    products = soup.find_all('article', class_='product_pod')
    
    # teroare :)))
    title_regex = re.compile(r'title="(.+?)"')   
    price_regex = re.compile(r'£(\d+\.\d{2})')   

    for product in products:
        # titlu
        title_tag = product.find('h3').a  
        title_match = title_regex.search(str(title_tag))
        title = title_match.group(1) if title_match else "No title found"
        
        # pret
        price_tag = product.find('p', class_='price_color')  
        price_match = price_regex.search(str(price_tag))
        price = price_match.group(1) if price_match else "No price found"
        
        print("Title:", title)
        print("Price:", f"£{price}")
        print("-" * 20)

#exercitiul 5
    print("--------exercise5--------")
    # Locate the category section, typically in a list with class "nav-list"
    category_section = soup.find('ul', class_='nav-list')
    
    categories = category_section.find_all('li') if category_section else []
    
    for category in categories:
        category_name = category.get_text(strip=True)
        print("Category:", category_name)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

#exercitiul 6
print("--------exercise6--------")
images = soup.find_all('img')
# teroare din nou
alt_regex = re.compile(r'alt="(.*?)"')

for img in images:
    # conversie string reg
    img_str = str(img)
    alt_match = alt_regex.search(img_str)
    alt_text = alt_match.group(1) if alt_match else "No alt text"
    print("Image alt text:", alt_text)
