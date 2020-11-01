from django.shortcuts import render
from django.http import  HttpResponse
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import pymongo

def index(request):
    return render(request, 'scrapper/index.html', {})


# def scrap(request):
    
#     if request.method == 'POST':
#         searchString = request.POST.get('content').replace(" ", "")
#         try:
#             dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
#             db = dbConn['crawlerDB']
#             reviews = db[searchString].find({})
#             if reviews.count()>0:
#                 return render(request, 'scrapper/result.html', {'reviews':reviews})
#             else:
#                 flipkart_url = "https://www.flipkart.com/search?q=" + searchString
#                 uClinet = urlopen(flipkart_url)
#                 flipkart_page = uClinet.read()
#                 uClinet.close()
#                 page_beautify = BeautifulSoup(flipkart_page, "html.parser")
#                 bigboxes = page_beautify.find_all("div", {"class":"bhgxx2 col-12-12"})
#                 del bigboxes[0:3]
#                 box = bigboxes[0]   
#                 product_link = "https://www.flipkart.com" + box.div.div.div.a["href"]
                
#                 product = requests.get(product_link)
#                 product_html = BeautifulSoup(product.text, "html.parser")

#                 all_cmt_section = product_html.find_all("div", {"class":"_39LH-M"})
#                 for box in all_cmt_section:
#                     comments_link = "https://www.flipkart.com" + box.a['href']

#                 paginate_review = requests.get(comments_link)
#                 reviews_page = BeautifulSoup(paginate_review.text, "html.parser")

#                 comment_boxes = reviews_page.find_all("div", {"class":"_3gijNv col-12-12"})
#                 last = comment_boxes[-1]
#                 no_pages = last.div.div.span.text.split()[-1]
                
#                 next_page_link = [a['href'] for a in reviews_page.find_all("a", {"class":"_2Xp0TH fyt9Eu"}, href=True)]

#                 next_sub_link = next_page_link[0][:-1]
#                 all_reviews = []
#                 table = db[searchString]

#                 for i in range(1, int(no_pages)+1):
#                     next = "https://www.flipkart.com" + next_sub_link + str(i)
#                     # print(next)
#                     reviews = requests.get(next)
#                     reviews_page = BeautifulSoup(reviews.text, "html.parser")

#                     comment_boxes = reviews_page.find_all("div", {"class":"_3gijNv col-12-12"})
#                     del comment_boxes[0:3]

#                     for comment_box in comment_boxes:
#                         try:
#                             name = comment_box.div.div.find_all('p', {"class":"_3LYOAd _3sxSiS"})[0].text
#                         except :
#                             name = 'Name'

#                         try:
#                             rating = comment_box.div.div.div.div.text
#                         except :
#                             rating = "No Rating"
                        
#                         try:
#                             commentHead = comment_box.div.div.div.p.text
#                         except :
#                             commentHead = 'No Comment Heading'
                        
#                         try:
#                             comtag = comment_box.div.div.find_all('div', {'class': ''})
#                             custComment = comtag[0].div.text
#                         except:
#                             custComment = 'No Customer Comment'

#                         myDict = {
#                             'Product':searchString,
#                             'Name':name, 
#                             'Rating': rating,
#                             'CommentHead':commentHead,
#                             'Comment':custComment,
#                         }

#                         # some changes : make a list -> append dictonary containing one page review 
#                         x = table.insert_one(myDict)
#                         all_reviews.append(myDict)

#                 context = {
#                     'reviews':all_reviews,
#                     'product':searchString,
#                     'pages':no_pages,
#                     }
#                 return render(request, 'scrapper/result.html', context)

#         except Exception as e:
#             print(e)
#             return HttpResponse('Something went wrong! or list index out of range')
#     else:
#         return render(request, 'scrapper/index.html', {})
        
#     return render(request, 'scrapper/result.html', {})




def scrap(request):
    try:
        if request.method == 'POST':
            searchString = request.POST.get('content').replace(" ", "")
            # try:
            #     dbConn = pymongo.MongoClient("mongodb://localhost:27017/")
            #     db = dbConn['crawlerDB']
            #     reviews = db[searchString].find({})
            #     if reviews.count()>0:
            #         return render(request, 'scrapper/result.html', {'reviews':reviews})
            #     else:
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClinet = urlopen(flipkart_url)
            flipkart_page = uClinet.read()
            uClinet.close()
            page_beautify = BeautifulSoup(flipkart_page, "html.parser")
            bigboxes = page_beautify.find_all("div", {"class":"bhgxx2 col-12-12"})
            del bigboxes[0:3]
            box = bigboxes[0]   
            product_link = "https://www.flipkart.com" + box.div.div.div.a["href"]
            
            product = requests.get(product_link)
            product_html = BeautifulSoup(product.text, "html.parser")

            all_cmt_section = product_html.find_all("div", {"class":"_39LH-M"})
            for box in all_cmt_section:
                comments_link = "https://www.flipkart.com" + box.a['href']

            paginate_review = requests.get(comments_link)
            reviews_page = BeautifulSoup(paginate_review.text, "html.parser")

            comment_boxes = reviews_page.find_all("div", {"class":"_3gijNv col-12-12"})
            last = comment_boxes[-1]
            no_pages = last.div.div.span.text.split()[-1]
            
            next_page_link = [a['href'] for a in reviews_page.find_all("a", {"class":"_2Xp0TH fyt9Eu"}, href=True)]

            next_sub_link = next_page_link[0][:-1]
            all_reviews = []
            # table = db[searchString]

            for i in range(1, int(no_pages)+1):
                next = "https://www.flipkart.com" + next_sub_link + str(i)
                # print(next)
                reviews = requests.get(next)
                reviews_page = BeautifulSoup(reviews.text, "html.parser")

                comment_boxes = reviews_page.find_all("div", {"class":"_3gijNv col-12-12"})
                del comment_boxes[0:3]

                for comment_box in comment_boxes:
                    try:
                        name = comment_box.div.div.find_all('p', {"class":"_3LYOAd _3sxSiS"})[0].text
                    except :
                        name = 'Name'

                    try:
                        rating = comment_box.div.div.div.div.text
                    except :
                        rating = "No Rating"
                    
                    try:
                        commentHead = comment_box.div.div.div.p.text
                    except :
                        commentHead = 'No Comment Heading'
                    
                    try:
                        comtag = comment_box.div.div.find_all('div', {'class': ''})
                        custComment = comtag[0].div.text
                    except:
                        custComment = 'No Customer Comment'

                    myDict = {
                        'Product':searchString,
                        'Name':name, 
                        'Rating': rating,
                        'CommentHead':commentHead,
                        'Comment':custComment,
                    }

                    # some changes : make a list -> append dictonary containing one page review 
                    # x = table.insert_one(myDict)
                    all_reviews.append(myDict)

            context = {
                'reviews':all_reviews,
                'product':searchString,
                'pages':no_pages,
                }
            return render(request, 'scrapper/result.html', context)

        else:
            return render(request, 'scrapper/index.html', {})
            
        # return render(request, 'scrapper/result.html', {})
    except :
        return HttpResponse("List out of index")