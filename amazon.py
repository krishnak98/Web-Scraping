import requests , bs4 , webbrowser 

#Searching amazon for top 5 links and finding their price 
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

print ( 'Enter name of product:\n')
product = input() 

print('Finding prices on Amazon.....')

res = requests.get('https://www.amazon.in/s/field-keywords='+''.join(product) , headers = headers  ) 
res.raise_for_status() 

soup = bs4.BeautifulSoup(res.text,'lxml')

links = soup.select('a[class="a-link-normal a-text-normal"]') 

numOfTabs = min(5,len(links)) 

for i in range (numOfTabs): 
	webbrowser.open(links[i].get('href'))