from bs4 import BeautifulSoup
import requests

def find_fake_domains(search_query):
    url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all("a")
    suspicious_domains = []
    
    for link in links:
        href = link.get('href')
        if "url?q=" in href:
            domain = href.split("url?q=")[1].split("&")[0]
            # Replace 'yourdomain.com' with the legitimate domain you're checking against
            if "yourkeyword" in domain and "yourdomain.com" not in domain:
                suspicious_domains.append(domain)
                
    return suspicious_domains

# Example usage
search_query = "YourSearchQueryHere"
fake_domains = find_fake_domains(search_query)
print("Suspicious domains found:", fake_domains)
