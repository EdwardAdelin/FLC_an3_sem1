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
     # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the text within the <a> tag that links to "index.html"
    link_text = soup.find('a', href="index.html").get_text(strip=True)
    print("Link text:", link_text)
    
    # Extract the text within the <small> tag
    small_text = soup.find('small').get_text(strip=True)
    print("Small text:", small_text)

#exercitiul 2
    print("--------exercise2--------")
    page_info = soup.find('li', class_='current')
    
    # Extract the text from the <li> tag, stripping extra whitespace
    page_text = page_info.get_text(strip=True) if page_info else "No page info found"
    print("Page info:", page_text)

#exercitiul 3
    print("--------exercise3--------")
    button = soup.find('button') 
    # Extract the text from the <button> tag, stripping extra whitespace
    button_text = button.get_text(strip=True) if button else "No button found"
    print("Button text:", button_text)

#exercitiul 4
    print("--------exercise4--------")
    products = soup.find_all('article', class_='product_pod')
    
    # tipare de folosire regex 
    title_regex = re.compile(r'title="(.+?)"')   # Matches the title within the `title` attribute
    price_regex = re.compile(r'£(\d+\.\d{2})')   # Matches prices formatted as £XX.XX

    for product in products:
        # titlu
        title_tag = product.find('h3').a  # Assuming the title is within <a> in <h3>
        title_match = title_regex.search(str(title_tag))
        title = title_match.group(1) if title_match else "No title found"
        
        # pret
        price_tag = product.find('p', class_='price_color')  # Assuming price is in <p class="price_color">
        price_match = price_regex.search(str(price_tag))
        price = price_match.group(1) if price_match else "No price found"
        
        print("Title:", title)
        print("Price:", f"£{price}")
        print("-" * 20)

#exercitiul 5
    print("--------exercise5--------")
    # Locate the category section, typically in a list with class "nav-list"
    category_section = soup.find('ul', class_='nav-list')
    
    # Find all <li> tags within the category section
    categories = category_section.find_all('li') if category_section else []
    
    # Iterate through each <li> and extract the category name
    for category in categories:
        # Get the text from each <a> tag inside <li> (which should be the category name)
        category_name = category.get_text(strip=True)
        print("Category:", category_name)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

#exercitiul 6
print("--------exercise6--------")
images = soup.find_all('img')

# Regular expression to capture the content of the alt attribute
alt_regex = re.compile(r'alt="(.*?)"')

# Iterate over each image and extract the alt content
for img in images:
    # Convert the <img> tag to a string to use regex
    img_str = str(img)
    alt_match = alt_regex.search(img_str)
    
    # Get the alt text if it exists
    alt_text = alt_match.group(1) if alt_match else "No alt text"
    print("Image alt text:", alt_text)
