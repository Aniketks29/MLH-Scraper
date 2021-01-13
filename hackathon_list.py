import os
import requests
import html5lib
import bs4
import csv

def scraper(result):
    event_list = []
    date_list = []
    soup = bs4.BeautifulSoup(result.text,'html5lib')
    events = soup.select('.event-name')
    dates = soup.select('.event-date')

    for event,date in zip(events,dates):
        event_list.append(event.getText())
        date_list.append(date.getText())
    coulmns = ['Event Name','Event Date']
    print("Making CSV file!!")
    with open('hackathon_list.csv','w',newline="") as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(coulmns)
        for event,date in zip(event_list,date_list):
            entry = [event,date]
            writer.writerow(entry)
    print("Completed!!")

if __name__ == "__main__":
    
    result  = requests.get("https://mlh.io/seasons/2021/events")
    scraper(result)
