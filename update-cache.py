from django.core.management import setup_environ
import settings
setup_environ(settings)
from django.core.cache import cache
from alertme.stocks.models import Stock
import urllib2
from urllib import quote
import json
import pdb

stock_dict = {'506134':'Intellivate Cap', '500209':'Infosys', '532696':'Educomp Sol', '533398':'MUTHOOT FIN', '532299':'TV Eighteen',
    '533217':'Hindustan Media', '532706':'Inox Leisure', '532689':'PVR', '533155':'Jubilant Food', '532848':'Delta Corp', '523261':'Venkys'}
google_url = "http://finance.google.com/finance/info?client=ig&q="
def getStockHandle():
  #stocks = Stock.objects.all()
  #for i in stocks:
  #  id = i.id
  #  print id
  cache.set('foo','bar',900)
  for key in stock_dict:
    stock_url = google_url + quote(key)
    try:
      urlhandle = urllib2.urlopen(stock_url)
      data = urlhandle.read()
    except:
      continue
    if data:
      data = json.loads(data[3:])
      data[0]['name'] = stock_dict[key]
      data = json.dumps(data)
      cache.set(key, data, 900);

getStockHandle()


