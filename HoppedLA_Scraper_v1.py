from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv


site = "https://hoppedla.com/beer-finder?fwp_neighborhood=pasadena"
header = {"User-Agent": "Mozilla/5.0"}
req = Request(site, headers=header)
page = urlopen(req)
soup = BeautifulSoup(page, "lxml")

csvFile = open("HoppedLA_Scraper_Pasadena.csv", "w", newline="")
csv_writer = csv.writer(csvFile)
csv_writer.writerow(["Venue", "Address"])


for venue in soup.find_all("div", class_="nh-venue-description"):
    venueName = venue.h3.a.text.strip()
    venueAddress = venue.p.text.strip()
    csv_writer.writerow([venueName, venueAddress])
    print(venueName)
    print(venueAddress)

csvFile.close()
