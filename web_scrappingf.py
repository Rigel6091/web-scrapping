#we are going to extract reviews of a product from flipkart
#First choose  the product and click on all reviews. 
#Click on page 2 then copy url
url="https://www.flipkart.com/redmi-8-sapphire-blue-64-gb/product-reviews/itme9614ba9b9bda?pid=MOBFKPYDENDXZZ7U&lid=LSTMOBFKPYDENDXZZ7U5KFCKA&marketplace=FLIPKART&page="
#remove page number in the url
import requests#getting access to a site
from bs4 import BeautifulSoup as bs#Extracting reviews
reviews=[]#For storing final reviews
for i in range(1,11):#extracting reviews from first 10 pages
    page=[]#store reviews in a single page
    response=requests.get(url+str(i))
    soup=bs(response.content,'html.parser')# creating soup object to iterate over the extracted content 
    rev=soup.findAll('div',attrs={'class',''})# Extracting the content under specific tags 
    #tag is 'div' and class is ''(NULL)
    #to know the tag, click on the review-->right click-->select inspect
    for i in range(len(rev)):
        page.append(rev[i].text)
    reviews=reviews+page
#Save the reviews as text file
# writng reviews in a text file 
with open("D:/reviews.txt","w",encoding='utf8') as output:#w- wrie r-read
    for i in reviews:
        output.write(i+"\n\n")
    
#Removing unwanted characters from reviews using re function
import re
reviews=" ".join(reviews)#converting list into a single string because re only work in string
reviews=re.sub('[^A-Za-z' ']+',' ',reviews).lower()
#converting the string to list to remove unwanted words
review_words=reviews.split()
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
sw=stopwords.words('english')
#removing the words in stop words
review_words=[i for i in review_words if i not in sw]
#we can plot wordcloud for better understanding
#wordcloud only accept string values so again convert list to str
reviews=" ".join(review_words)
from wordcloud import WordCloud
plot=WordCloud().generate(reviews)
import matplotlib.pyplot as plt
plt.imshow(plot)
