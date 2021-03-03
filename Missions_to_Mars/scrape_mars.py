from splinter import Browser 
from bs4 import BeautifulSoup as bs
import pandas as pd 
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}    
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_p = news(broswer)
    mars_data_info = {
        'news_title': news_title,
        'news_paragraph': news_p,
        'featured_image': featured_image(browser),
        'facts': facts(),
        'hemispheres': img_urls(browser)
    }
    browser.quit()
    return mars_data_info


def news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    # Retrieve all elements that contain latestr news titles 
    news_title = soup.find_all('div', class_='content_title')[1].text  
    news_p = soup.find_all('div', class_='rollover_description_inner')[1].text 
    return news_title, news_p

