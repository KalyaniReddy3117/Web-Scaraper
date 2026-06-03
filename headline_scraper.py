import requests
from bs4 import BeautifulSoup

response=requests.get("https://www.thehindu.com?utm_source=chatgpt.com")
soup=BeautifulSoup(response.text,"html.parser")
headlines=soup.find_all("h2",{"class":"title"})
if response.status_code==200:
    with open("headlines.txt","w") as file:
        for i,headline in enumerate(headlines,start=1):
            file.write(f"{i}.{headline.text.strip()}\n")
    print("Headlines have been saved to headlines.txt")
else:    
    print("Failed to retrieve the webpage. Status code:", response.status_code)