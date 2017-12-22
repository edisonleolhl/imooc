import urllib.request
import os

urls = []

path = 'textbook/math_required5/'
if not os.path.exists (path):
    os.makedirs (path)

for i in range(102,105):
    url = 'http://res.ajiao.com/uploadfiles/Book/270/' + str(i+1) + '_838x979.jpg'

    with open (path + str(i+1) + '.jpg', 'wb+') as f_img:
        f_img.write (urllib.request.urlopen (url).read ())
        print ("DOWALOADING url:" + url)