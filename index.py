from selenium import webdriver
import bs4,re,string
browser=webdriver.Firefox()
url="https://codeforces.com/ratings"
browser.get(url)
html=browser.page_source
soup=bs4.BeautifulSoup(html,"html.parser")
ratings=soup.select(".ratingsDatatable .rated-user")
file1=open("top200names.txt",'w')
for name in ratings:
	file1.write(name.get_text()+'\n')
file1.close()
file2=open('top200names.txt','r')
lines=file2.readlines()
file2.close()
file3=open("average.txt",'w')
count=0
totalsum=0
for i in range(200):
	url="https://codeforces.com/profile/"+lines[i]
	browser.get(url)
	html=browser.page_source
	soup=bs4.BeautifulSoup(html,"html.parser")
	names=soup.find_all('div',class_='tickLabel',style=re.compile('left:'))
	try:
		str1=names[-1].get_text()
		str2=names[0].get_text()
		num1=re.search('[0-9]+',str1)
		num2=re.search('[0-9]+',str2)
		if(num1 is not None and num2 is not None):
			num1=int(num1.group(0))
			num2=int(num2.group(0))
			file3.write(lines[i].rstrip('\n')+":"+str(num1-num2+1)+'\n')
			if(num1-num2>=0):
				totalsum+=num1-num2+1
				count+=1	
	except:
		pass
file3.write('AVERAGE: '+str(totalsum/count))
file3.close()