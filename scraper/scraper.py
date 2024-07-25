# scraper/scraper.py
import requests
from bs4 import BeautifulSoup
from models.models import Case, session

url = 'https://example-legal-website.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for case in soup.find_all('div', class_='case'):
    case_name = case.find('h2').text
    court = case.find('span', class_='court').text
    decision_date = case.find('span', class_='date').text
    summary = case.find('p', class_='summary').text
    
    new_case = Case(case_name=case_name, court=court, decision_date=decision_date, summary=summary)
    session.add(new_case)

session.commit()
