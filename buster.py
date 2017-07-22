import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from pprint import pprint

def getBusData(url):
    XMLresult = requests.get(url)
    XMLresult.encoding = 'UTF-8'
    XML = XMLresult.text.encode('UTF-8')
    return XML



chchhospitalplatformtag ='2102'
#'http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPPlatform'
stopData = getBusData('http://rtt.metroinfo.org.nz/rtt/public/utility/file.aspx?ContentType=SQLXML&Name=JPRoutePositionET2&PlatformTag=2102')

#
soup = BeautifulSoup(stopData, 'xml')
output = soup.find(Name="Purple Line")
# print(output)
root = ET.fromstring(str(output))

for dest in root.iter('Destination'):
    destname = dest.attrib['Name']
    print(destname)
    xpath = ".//*[@Name='"+destname+"']/Trip"
    # print(xpath)
    for trip in root.findall(xpath):
        print(trip.attrib['ETA'])
