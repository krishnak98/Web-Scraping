import requests , bs4 , webbrowser, sys 

print('What do u want to search') 
search_query = input() 


print('Googling....') 

#Downloading google web page
res = requests.get('http://google.com/search?q='+' '.join(search_query)) 
res.raise_for_status() 

#Retrieve top search results
soup = 	bs4.BeautifulSoup(res.text) 

links = soup.select('.r a') 

#Opening a Browser for each tab 
numTabs = min ( 5 , len(links)) 
for i in range (numTabs) : 
	webbrowser.open('http://google.com'+(links[i].get('href')))

