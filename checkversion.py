import requests
import xmltodict
from xml.parsers.expat import ExpatError

path1 = "/language/en-GB/en-GB.xml"
path2 = "/administrator/manifests/files/joomla.xml"

def joomla():
    site = input("Enter site: ").lower()
    try:
        if "https" not in site or "http" not in site:
                r = requests.get("http://"+site+path1)
                r2 = requests.get("http://"+site+path2)
        else:
                r = requests.get(site+path1)
                r2 = requests.get(site+path2)
        if r.status_code != 200 and r2.status_code != 200:
            print(f"Failed, Status code: {r.status_code} and {r2.status_code}")
        else:
            doc = xmltodict.parse(r.text)
            doc2 = xmltodict.parse(r2.text)
            print("Joomla Posible Version: "+doc['metafile']['version'])
            print("Joomla Posible Version: "+doc2['extension']['version'])
    except requests.exceptions.InvalidURL:
        print("Invalid URL")
    except requests.exceptions.ConnectionError:
        print("Failed to establish")
    except xmltodict.expat.ExpatError:
        print("Failed parser")

joomla()
