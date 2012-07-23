#!/usr/bin/python

import urllib
param = urllib.urlencode({'ajax' : 'Product-SetData',
  'language' : 'en',
  'droit' : 'STAG',
  'profil' : 'INTERNE',
  's' : '21978',
  'w' : '46739OTfs!RiGhtOwtSrCing',
  'views' : 'UnitFloatingBar,UnitBackOfficeMenu,UnitInfoSocietySimple,UnitCompanyMiscellaneous,ListProductContainer,UnitProductContainer,UnitProduct,Default',
  'containerType' : 'Group',
  'field' : 'Specification',
  'level' : 'product',
  'item_id' : '316339',
  'value' : 'WAKEBOARDS > BOOTS > MEN'})

opener = urllib.urlopen("http://www.nauticexpo.com/restricted/BackOffice/ajax.php", param)
print opener.read()
