# web-scraping-challenge
This repository builds a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

The intial data scrape is performed using Jupyter Notebook, BeautifulSoup, Pandas, and Splinter inside a file called mission_to_mars.ipynb. It scrapes the Mars News Site and collects the latest News Title and Paragraph Text. Then it scrapes JPL Mars Space Images, using splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url. Next, it visits the Mars Facts webpage and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. before using Pandas to convert the data to a HTML table string.Finally, it visits the astrogeology site to obtain high resolution images for each of Mar's hemispheres.

Next, MongoDB with Flask templating is used to create a new HTML page that displays all of the information that was scraped from the URLs above.





