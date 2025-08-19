import requests 
from bs4 import BeautifulSoup 
from urllib.parse import quote
prices= []

def min_max(link,title,tozih):
    max_price= max(prices)
    min_price= min(prices)
    namber_max = prices.index(max_price)
    namber_min = prices.index(min_price)
    print("\n")
    print("="*50)
    print("The most expensive")
    print("="*50)
    print ("link : divar.ir"+link[namber_max]['href'])
    print("title : "+title[namber_max].text)
    print("description : "+tozih[namber_max*2].text)
    print("price : "+tozih[namber_max*2+1].text)
    print("="*50)
    print("Cheapest")
    print("="*50)
    print ("link : divar.ir"+link[namber_min]['href'])
    print("title : "+title[namber_min].text)
    print("description : "+tozih[namber_min*2].text)
    print("price : "+tozih[namber_min*2+1].text)
def fa_en(text):
    fatoen={'۰': '0','۱': '1','۲': '2','۳': '3','۴': '4','۵': '5','۶': '6','۷': '7','۸': '8','۹': '9'}
    return ''.join(fatoen.get(char,"") for char in text )
def searcher():
    chek=input('If you want to go out. enter "exit" \nDo you want to enter a URL ? [y/n]')
    if chek == "exit": return False
    elif chek in "yY" :
        url = input(" for example \"https://divar.ir/???????\"\n url :")
    elif chek in "nN":
        city=input("enter your city:")
        serch=input("search:")
        encode= quote(serch)
        url=f"https://divar.ir/s/{city}?q={encode}&tab=default"
    site= requests.get(url)
    if site.status_code == 200 :
        soup=BeautifulSoup(site.text,'html.parser')
        link=soup.find_all("a" , {"class": "kt-post-card__action"})
        if link :
            title=soup.find_all("h2",{"class" : "kt-post-card__title"} )
            tozih=soup.find_all('div',{"class":"kt-post-card__description"})
            for i in range(len(link)):
                print ("_"*50)
                print(f"[{i+1}]")
                print ("link : divar.ir"+link[i]['href'])
                print("title : "+title[i].text)
                print("description : "+tozih[i*2].text)
                print("price : "+tozih[i*2+1].text)
                prices.append(int(fa_en(tozih[i*2+1].text)))
            if input("\n Do you want to see the cheapest and most expensive  [y/n] :") in "yY" :
                min_max(link,title,tozih)
        else:
            print ("oh! nothing found.")
            
    elif site.status_code == 404 :
        print ("Page not found")
        
    else :
        print(f"status code {site.status_code}")
        
while True :
    if  searcher() == False : break
