import urllib.request
def get_price():
    page = urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    price = float(text[start_of_price:end_of_price])
    return(price)

price = 0.0
while price < 6.0:
    price = get_price()
    print (price)
print ("Price for regular member : ",price)
