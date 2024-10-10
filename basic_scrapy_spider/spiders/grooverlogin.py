import scrapy
import json
from scrapy.http import FormRequest
from scrapy.http import HtmlResponse

class LoginSpider(scrapy.Spider):
    name = 'login_spider'
    
    # Website login URL
    #start_urls = ['https://auth.groover.co/api/login/']

    def start_requests(self):
        # Extract the necessary login credentials here
        login_data = {
            'email': 'aspenjadeartist@gmail.com',
            'password': 'password'
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
            yield response.follow('https://groover.co/en/band/dashboard/', callback=self.parse)

            
    def parse(self, response):
        if 'band/dashboard' in response.url:
            print('Successfully navigated to the dashboard page.')
            if self.wait_for_page_load(response):
            # Process the loaded page data
                self.logger.info("Page has finished loading: {}".format(response.url))
            # Call your parse_dashboard method here
            yield self.parse_dashboard(response)
        else:
            print('Navigation to the dashboard page failed. Current URL: %s', response.url)

    def wait_for_page_load(self, response):
        """
        Waits for the page to load completely
        """
        if isinstance(response, HtmlResponse) and response.body:
            print('page loaded')
            html_file = open('random.html', 'w')
            html_file.write(response.body.decode("utf-8"))
            # Additional check can be added based on your requirement (e.g. certain element to be present)
            return True
        return False


    def parse_dashboard(self, response):
        if response.url == 'https://groover.co/en/band/dashboard/':
            print('Successfully navigated to the dashboard page.')
        print('campaigned_songs')
        campaigned_songs = response.xpath('//div[@id="ignoreFontUpscale"]/div/fieldset[1]//label/span/text()').extract()
        print('OKAY')
        field_set_items = response.css('fieldset')
        print(field_set_items)


        print(campaigned_songs)
        # Parse and extract data from the authenticated dashboard page
        # Example: Extracting information from the dashboard page
        pass


















