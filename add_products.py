import urllib
import yaml
from urllib2 import urlopen, URLError, HTTPError
import os
file_name = "products/database.yaml"
pic_url = "https://m.pricez.co.il/ProductPictures/200x/%s.jpg"


def dlfile(url,output_file):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(output_file, "wb") as local_file:
            local_file.write(f.read())

    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
        raise e
    except URLError, e:
        print "URL Error:", e.reason, url
        raise e



# load YAML
stream = open(file_name, 'r')
data = yaml.load(stream)



while (True):
    code = raw_input("Scan BarCode:")
    if (code == ""): break
    prod_name = raw_input("Enter Name:")
    prod_price = raw_input("Enter Price:")

    data[code] = {
        "name" : str(prod_name),
        "price" : int(prod_price)
    }

    # try to get a pictures
    try:
        dlfile(pic_url%code,"./products/%s.jpg"%code)
        data[code]["picture"] = code + ".jpg"
    except:
        print("Cant find a picture...")
        pass




with open(file_name, 'w') as yaml_file:
    yaml_file.write( yaml.safe_dump(data, default_flow_style=False,encoding=None))

