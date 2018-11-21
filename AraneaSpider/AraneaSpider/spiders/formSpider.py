from scrapy.http import FormRequest
from scrapy.spiders import Spider

class FormSpider(Spider): 
    name = 'horseForm'

    start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

    def parse(self, response): 
    # define parse method

        formdata = {'firstname': 'Brittany', 
                    'lastname': 'Beckett-Harrison', 
                    'jobtitle': 'Junior Developer'}
        
        # pass data into form and utilize submit button to submit data"
        return FormRequest.from_response(response, formnumber=0,
                                        formdata=formdata,
                                        callback=self.after_post)
    def after_post(self, response): 
        print('\n\n********\nForm processed.\n')
        print(response)
        print('\n********\n')
                                        
        