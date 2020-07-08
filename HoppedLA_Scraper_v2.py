from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

neighborhoods = [
    "central-la",
    "downtown-la",
    "eastside",
    "long-beach",
    "north-la",
    "pasadena",
    "san-fernando-valley",
    "san-gabriel-valley",
    "south-bay",
    "south-la",
    "westside",
]

with open("HoppedLA_Scraper.csv", "w", newline="") as csvFile:
    csv_writer = csv.writer(csvFile)

    for neighborhood in neighborhoods:
        site = "https://hoppedla.com/beer-finder?fwp_neighborhood={}".format(
            neighborhood
        )
        header = {"User-Agent": "Mozilla/5.0"}
        req = Request(site, headers=header)
        page = urlopen(req)
        soup = BeautifulSoup(page, "lxml")

        neighboroodName = neighborhood.upper()
        csv_writer.writerow([neighboroodName])
        csv_writer.writerow(["Venue", "Address"])

        for venue in soup.find_all("div", class_="nh-venue-description"):
            venueName = venue.h3.a.text.strip()
            venueAddress = venue.p.text.strip()
            csv_writer.writerow([venueName, venueAddress])
#        print(venueName)
#        print(venueAddress)

