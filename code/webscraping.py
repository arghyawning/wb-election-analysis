import scrapy
import unidecode
import csv


class WbSpider(scrapy.Spider):
    name = 'wb'
    allowed_domains = ['https://myneta.info/']
    start_urls = ['https://myneta.info/wb2006/index.php?action=show_winners&sort=default']

    def parse(self, response):
        DELIM = ","

        def clean_row(row):
            return [item.strip().replace(DELIM, "") if item else "" for item in row]

        rows = response.css("tr")
        with open(f"data_table.csv", "w", newline="") as f:
            writer = csv.writer(f, delimiter=DELIM)
            for row in rows:
                data = [
                    unidecode.unidecode(word) for word in row.css("td *::text").getall()
                    #word for word in row.css("td *::text").getall()
                ]
                if len(data) == 11:
                    writer.writerow(clean_row(data[:-1]))


    #def parse(self, response):
        #get = []
     #   for row in response.css("tr"):
      #      print(row.css("td *::text").getall())
       #     print("\n")
            
        #print(get)
        #print("\n\nHERE^^\n\n")
