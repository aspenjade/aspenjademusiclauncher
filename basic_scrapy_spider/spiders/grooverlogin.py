import scrapy
import json
from scrapy.http import FormRequest

class LoginSpider(scrapy.Spider):
    name = 'login_spider'
    
    # Website login URL
    #start_urls = ['https://auth.groover.co/api/login/']

    def start_requests(self):
        # Extract the necessary login credentials here
        login_data = {
            'email': 'aspenjadeartist@gmail.com',
            'password': 'Rachel*22'
        }
        
        url = 'https://auth.groover.co/api/login/'
        
        # Submit the form data

        yield FormRequest(url,
                            formdata={'email': 'aspenjadeartist@gmail.com', 'password': 'Rachel*22'},
                            callback=self.after_login)

       

    def after_login(self, response):
        print(response.text)
        # Check login success by inspecting the redirected page
        if "access" in response.text:
            self.logger.info("Logged in successfully!")
            # Now you can continue scraping as an authenticated user
            # For example, scraping content from the authenticated pages
            pass
            #yield response.follow('https://groover.co/en/band/dashboard/', callback=self.parse_dashboard)

            

    def parse_dashboard(self, response):
        campaigned_songs = response.xpath('/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div/fieldset[1]')
        print(campaigned_songs)
        # Parse and extract data from the authenticated dashboard page
        # Example: Extracting information from the dashboard page
        pass