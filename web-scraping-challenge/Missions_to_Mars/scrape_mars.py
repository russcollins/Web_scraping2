# Declare Dependencies 
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # @NOTE: Path to my chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    # NASA MARS NEWS
    # Initialize browser 
    browser = init_browser()

    # Visit Nasa news url through splinter module
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # Retrieve the latest element that contains news title and news_paragraph
    result = soup.find('div', class_="list_text")
    news_title = result.text
    news_p = result.find('div',class_="article_teaser_body").text

    # FEATURED IMAGE
    # Visit Mars Space Images through splinter module
    img_url = 'https://spaceimages-mars.com/'
    browser.visit(img_url)

    # HTML Object 
    img_html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(img_html, 'html.parser')

    # Retrieve url
    img_result = soup.find('img', class_="headerimage fade-in")['src']
    img_url = img_result.replace("background-image: url('","").replace("');","")
    featured_image_url = f"https://spaceimages-mars.com/{img_url}"
      
    # MARS FACTS
    # Visit Mars facts url 
    facts_url = 'https://galaxyfacts-mars.com/'
    browser.visit(facts_url)

    # Use Pandas to "read_html" to parse the URL
    tables = pd.read_html(facts_url)

    #Find Mars Facts DataFrame in the lists of DataFrames
    df = tables[1]
    df.columns = ["Description","Value"]
    idx_df = df.set_index("Description")
    facts_html = idx_df.to_html()

    # MARS HEMISPHERE
    # Visit hemispheres website through splinter module 
    hemi_url = 'https://marshemispheres.com/'
    browser.visit(hemi_url)

    # HTML Object
    hemi_html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(hemi_html, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemi_img_urls = []

    # Store the main_ul 
    hemi_main_url = 'https://marshemispheres.com/'

    # Loop through the items previously stored
    for i in items: 
        # Store title
        title = i.find('h3').text
            
        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
        # Visit the link that contains the full image website 
        browser.visit(hemi_main_url + partial_img_url)
            
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
            
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = bs(partial_img_html, 'html.parser')
            
        # Retrieve full image source 
        img_url = hemi_main_url + soup.find('img', class_='wide-image')['src']
            
        # Append the retreived information into a list of dictionaries 
        hemi_img_urls.append({"title" : title, "img_url" : img_url})
        
    # Dictionary entry for Mars hemispheres
    mars_info = {"news_title":news_title,"news_text":news_p,"featured_image":featured_image_url,
    "facts_table":facts_html,"hemisphere_img":hemi_img_urls}
        
    
    browser.quit()

    # Return mars_data dictionary 
    return mars_info