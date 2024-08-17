import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set your OpenAI API key

# Function to scrape product prices from a website
def scrape_prices(url, product_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_elements = soup.find_all('div', class_='product')  # Example class name
    
    product_data = []

    for product in product_elements:
        name = product.find('h2', class_='product-name').text.strip()  # Example tag and class
        price = product.find('span', class_='product-price').text.strip()  # Example tag and class
        
        if product_name.lower() in name.lower():
            product_data.append({
                'name': name,
                'price': float(price.replace('$', '')),
                'url': url
            })
    
    return product_data
# Function to find the best prices within a budget
def find_best_prices(product_name, budget, retailer_urls):
    all_products = []
    
    for url in retailer_urls:
        products = scrape_prices(url, product_name)
        all_products.extend(products)
    # Filter products within the budget
    affordable_products = [p for p in all_products if p['price'] <= budget]
    
    # Sort by price
    affordable_products = sorted(affordable_products, key=lambda x: x['price'])
    
    # Convert to DataFrame for better display
    df = pd.DataFrame(affordable_products)
    return df

# Function to summarize and provide recommendations using OpenAI API
def summarize_and_recommend(products_df, budget):
    # Prepare the input text for the OpenAI API
    product_summary = products_df.to_string(index=False)
    prompt = f"""You are an AI assistant. Given the following product prices and a budget of ${budget}, summarize the best options and offer personalized recommendations:
    Products:
{product_summary}
"""
    
   
    
   
# Example usage
retailer_urls = [
    'https://naivas.online/',
    'https://www.carrefour.ke/mafken/en/',
    'https://quickmart.co.ke/'
]

product_name = 'apple'
budget = 5.00  # Example budget in dollars

best_prices = find_best_prices(product_name, budget, retailer_urls)
summary = summarize_and_recommend(best_prices, budget)
print("Best Prices:")
print(best_prices)
print("\nSummary and Recommendations:")
print(summary)