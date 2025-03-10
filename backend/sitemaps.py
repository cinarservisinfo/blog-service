from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.sitemaps import Sitemap  # new

class HomeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return ['index']  # Anasayfa sayfasının adı

    def location(self, item):
        return ''  # Anasayfa sayfasının URL'si


class AboutSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['hakkimizda']  

    def location(self, item):
        return '/hakkimizda.html/'  

class ContactSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['iletisim']  

    def location(self, item):
        return '/iletisim.html/'  

#akhisar bölgesi kombi servisi için

class AkhisarAirfelCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/airfel.html/'  
    
class AkhisarAlarkCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/alarko.html/'  

class AkhisarBaymakCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/baymak.html/'  
    
class AkhisarBoschCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/bosch.html/'  
    
class AkhisarBuderusCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['buderus']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/buderus.html/'  
    
class AkhisarDaikinCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/daikin.html/'  

class AkhisarDemirDokumCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/demirdokum.html/'  

class AkhisarEcaCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/eca.html/' 
     
class AkhisarFerroliCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ferroli']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/ferroli.html/'  
    
    
class AkhisarImmergasCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['immergas']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/immergas.html/'  
    
class AkhisarProthermCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['protherm']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/protherm.html/'  
    
    
class AkhisarVaillantCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/vaillant.html/'  
    
class AkhisarViessmannCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/viessmann.html/'  
    
class AkhisarWharmhouseCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['wharmhouse']  

    def location(self, item):
        return '/servisler/kombi-servisi/akhisar/wharmhouse.html/'  
    
# saruhanlı bölgesi kombi servisi

class SaruhanliAirfelCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/airfel.html/'  
    
class SaruhanliAlarkCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/alarko.html/'  

class SaruhanliBaymakCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/baymak.html/'  
    
class SaruhanliBoschCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/bosch.html/'  
    
class SaruhanliBuderusCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['buderus']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/buderus.html/'  
    
class SaruhanliDaikinCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/daikin.html/'  

class SaruhanliDemirDokumCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/demirdokum.html/'  

class SaruhanliEcaCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/eca.html/' 
     
class SaruhanliFerroliCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ferroli']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/ferroli.html/'  
    
    
class SaruhanliImmergasCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['immergas']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/immergas.html/'  
    
class SaruhanliProthermCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['protherm']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/protherm.html/'  
    
    
class SaruhanliVaillantCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/vaillant.html/'  
    
class SaruhanliViessmannCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/viessmann.html/'  
    
class SaruhanliWharmhouseCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['wharmhouse']  

    def location(self, item):
        return '/servisler/kombi-servisi/saruhanli/wharmhouse.html/'  


#Şehzadeler bölgesi kombi servisi için

class SehzadelerAirfelCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/airfel.html/'  
    
class SehzadelerAlarkCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/alarko.html/'  

class SehzadelerBaymakCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/baymak.html/'  
    
class SehzadelerBoschCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/bosch.html/'  
    
class SehzadelerBuderusCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['buderus']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/buderus.html/'  
    
class SehzadelerDaikinCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/daikin.html/'  

class SehzadelerDemirDokumCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/demirdokum.html/'  

class SehzadelerEcaCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/eca.html/' 
     
class SehzadelerFerroliCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ferroli']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/ferroli.html/'  
    
    
class SehzadelerImmergasCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['immergas']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/immergas.html/'  
    
class SehzadelerProthermCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['protherm']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/protherm.html/'  
    
    
class SehzadelerVaillantCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/vaillant.html/'  
    
class SehzadelerViessmannCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/viessmann.html/'  
    
class SehzadelerWharmhouseCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['wharmhouse']  

    def location(self, item):
        return '/servisler/kombi-servisi/sehzadeler/wharmhouse.html/'  

#turgutlu bölgesi kombi servisi için

class TurgutluAirfelCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/airfel.html/'  
    
class TurgutluAlarkCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/alarko.html/'  

class TurgutluBaymakCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/baymak.html/'  
    
class TurgutluBoschCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/bosch.html/'  
    
class TurgutluBuderusCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['buderus']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/buderus.html/'  
    
class TurgutluDaikinCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/daikin.html/'  

class TurgutluDemirDokumCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/demirdokum.html/'  

class TurgutluEcaCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/eca.html/' 
     
class TurgutluFerroliCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ferroli']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/ferroli.html/'  
    
    
class TurgutluImmergasCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['immergas']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/immergas.html/'  
    
class TurgutluProthermCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['protherm']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/protherm.html/'  
    
    
class TurgutluVaillantCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/vaillant.html/'  
    
class TurgutluViessmannCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/viessmann.html/'  
    
class TurgutluWharmhouseCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['wharmhouse']  

    def location(self, item):
        return '/servisler/kombi-servisi/turgutlu/wharmhouse.html/'  


#yunusemre bölgesi kombi servisi için

class YunusemreAirfelCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/airfel.html/'  
    
class YunusemreAlarkCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/alarko.html/'  

class YunusemreBaymakCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/baymak.html/'  
    
class YunusemreBoschCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/bosch.html/'  
    
class YunusemreBuderusCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['buderus']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/buderus.html/'  
    
class YunusemreDaikinCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/daikin.html/'  

class YunusemreDemirDokumCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/demirdokum.html/'  

class YunusemreEcaCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/eca.html/' 
     
class YunusemreFerroliCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ferroli']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/ferroli.html/'  
    
    
class YunusemreImmergasCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['immergas']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/immergas.html/'  
    
class YunusemreProthermCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['protherm']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/protherm.html/'  
    
    
class YunusemreVaillantCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/vaillant.html/'  
    
class YunusemreViessmannCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  
#
    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/viessmann.html/'  
    
class YunusemreWharmhouseCombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['wharmhouse']  

    def location(self, item):
        return '/servisler/kombi-servisi/yunusemre/wharmhouse.html/'  



######## klima servisi ################

#akhisar bölgesi klima servisi

class AkhisarAirfelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/airfel.html/'  

class AkhisarAlarkoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/alarko.html/'  

class AkhisarArcelikClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/arcelik.html/'  

class AkhisarBaymakClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/baymak.html/'  

class AkhisarBekoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/beko.html/'  
    
class AkhisarBoschClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/bosch.html/'  
    

class AkhisarDaikinClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/daikin.html/'  

class AkhisarDemirDokumClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/demirdokum.html/'  

class AkhisarDijitsuClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['dijitsu']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/dijitsu.html/'  
    
class AkhisarEcaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/eca.html/' 
     
class AkhisarLgClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/lg.html/'  

class AkhisarMitsubishiClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['mitsubishi']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/mitsubishi.html/'  
    
class AkhisarRegalClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/regal.html/'  
    
    
class AkhisarSamsungClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/samsung.html/'  
    
class AkhisarSegClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/seg.html/'  
    
    
class AkhisarSiemensClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/siemens.html/'  
    
class AkhisarSigmaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['sigma']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/sigma.html/'  

class AkhisarToshibaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['toshiba']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/toshiba.html/'  

class AkhisarVaillantClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/vaillant.html/'  
    
class AkhisarVestelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/klima-servisi/akhisar/vestel.html/'  
    

#Saruhanlı bölgesi klima servisi

class SaruhanliAirfelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/airfel.html/'  

class SaruhanliAlarkoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/alarko.html/'  

class SaruhanliArcelikClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/arcelik.html/'  

class SaruhanliBaymakClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/baymak.html/'  

class SaruhanliBekoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/beko.html/'  
    
class SaruhanliBoschClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/bosch.html/'  
    

class SaruhanliDaikinClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/daikin.html/'  

class SaruhanliDemirDokumClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/demirdokum.html/'  

class SaruhanliDijitsuClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['dijitsu']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/dijitsu.html/'  
    
class SaruhanliEcaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/eca.html/' 
     
class SaruhanliLgClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/lg.html/'  

class SaruhanliMitsubishiClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['mitsubishi']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/mitsubishi.html/'  
    
class SaruhanliRegalClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/regal.html/'  
    
    
class SaruhanliSamsungClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/samsung.html/'  
    
class SaruhanliSegClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/seg.html/'  
    
    
class SaruhanliSiemensClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/siemens.html/'  
    
class SaruhanliSigmaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['sigma']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/sigma.html/'  

class SaruhanliToshibaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['toshiba']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/toshiba.html/'  

class SaruhanliVaillantClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/vaillant.html/'  
    
class SaruhanliVestelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/klima-servisi/saruhanli/vestel.html/'  
    

#şehzadeler bölgesi klima servisi için


class SehzadelerAirfelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/airfel.html/'  

class SehzadelerAlarkoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/alarko.html/'  

class SehzadelerArcelikClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/arcelik.html/'  

class SehzadelerBaymakClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/baymak.html/'  

class SehzadelerBekoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/beko.html/'  
    
class SehzadelerBoschClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/bosch.html/'  
    

class SehzadelerDaikinClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/daikin.html/'  

class SehzadelerDemirDokumClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/demirdokum.html/'  

class SehzadelerDijitsuClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['dijitsu']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/dijitsu.html/'  
    
class SehzadelerEcaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/eca.html/' 
     
class SehzadelerLgClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/lg.html/'  

class SehzadelerMitsubishiClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['mitsubishi']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/mitsubishi.html/'  
    
class SehzadelerRegalClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/regal.html/'  
    
    
class SehzadelerSamsungClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/samsung.html/'  
    
class SehzadelerSegClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/seg.html/'  
    
    
class SehzadelerSiemensClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/siemens.html/'  
    
class SehzadelerSigmaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['sigma']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/sigma.html/'  

class SehzadelerToshibaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['toshiba']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/toshiba.html/'  

class SehzadelerVaillantClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/vaillant.html/'  
    
class SehzadelerVestelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/klima-servisi/sehzadeler/vestel.html/'  


#turgutlu bölgesi klima servisi için


class TurgutluAirfelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/airfel.html/'  

class TurgutluAlarkoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/alarko.html/'  

class TurgutluArcelikClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/arcelik.html/'  

class TurgutluBaymakClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/baymak.html/'  

class TurgutluBekoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/beko.html/'  
    
class TurgutluBoschClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/bosch.html/'  
    

class TurgutluDaikinClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/daikin.html/'  

class TurgutluDemirDokumClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/demirdokum.html/'  

class TurgutluDijitsuClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['dijitsu']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/dijitsu.html/'  
    
class TurgutluEcaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/eca.html/' 
     
class TurgutluLgClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/lg.html/'  

class TurgutluMitsubishiClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['mitsubishi']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/mitsubishi.html/'  
    
class TurgutluRegalClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/regal.html/'  
    
    
class TurgutluSamsungClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/samsung.html/'  
    
class TurgutluSegClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/seg.html/'  
    
    
class TurgutluSiemensClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/siemens.html/'  
    
class TurgutluSigmaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['sigma']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/sigma.html/'  

class TurgutluToshibaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['toshiba']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/toshiba.html/'  

class TurgutluVaillantClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/vaillant.html/'  
    
class TurgutluVestelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/klima-servisi/turgutlu/vestel.html/'  


#yunusemre bölgesi klima servisi için

class YunusemreAirfelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['airfel']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/airfel.html/'  

class YunusemreAlarkoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['alarko']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/alarko.html/'  

class YunusemreArcelikClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/arcelik.html/'  

class YunusemreBaymakClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['baymak']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/baymak.html/'  

class YunusemreBekoClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/beko.html/'  
    
class YunusemreBoschClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/bosch.html/'  
    

class YunusemreDaikinClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['daikin']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/daikin.html/'  

class YunusemreDemirDokumClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['demirdokum']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/demirdokum.html/'  

class YunusemreDijitsuClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['dijitsu']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/dijitsu.html/'  
    
class YunusemreEcaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['eca']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/eca.html/' 
     
class YunusemreLgClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/lg.html/'  

class YunusemreMitsubishiClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['mitsubishi']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/mitsubishi.html/'  
    
class YunusemreRegalClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/regal.html/'  
    
    
class YunusemreSamsungClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/samsung.html/'  
    
class YunusemreSegClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/seg.html/'  
    
    
class YunusemreSiemensClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/siemens.html/'  
    
class YunusemreSigmaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['sigma']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/sigma.html/'  

class YunusemreToshibaClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['toshiba']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/toshiba.html/'  

class YunusemreVaillantClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vaillant']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/vaillant.html/'  
    
class YunusemreVestelClimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/klima-servisi/yunusemre/vestel.html/'  


######## beyaz eşya servisi ################

#akhisar bölgesi beyaz eşya servisi

class AkhisarArcelikHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/arcelik.html/'  

class AkhisarAristonHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ariston']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/ariston.html/'  

class AkhisarBekoHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/beko.html/'  

class AkhisarBoschHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/bosch.html/'  

class AkhisarLgHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/lg.html/'  

class AkhisarProfiloHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['profilo']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/profilo.html/'  
    
class AkhisarRegalHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/regal.html/'  

class AkhisarSamsungHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/samsung.html/'  
    
class AkhisarSegHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/seg.html/'  

class AkhisarSiemensHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/siemens.html/'  
    
class AkhisarVestelHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/akhisar/vestel.html/'  
    

#saruhanlı bölgesi beyaz eşya servisi

class SaruhanliArcelikHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/arcelik.html/'  

class SaruhanliAristonHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ariston']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/ariston.html/'  

class SaruhanliBekoHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/beko.html/'  

class SaruhanliBoschHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/bosch.html/'  

class SaruhanliLgHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/lg.html/'  

class SaruhanliProfiloHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['profilo']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/profilo.html/'  
    
class SaruhanliRegalHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/regal.html/'  

class SaruhanliSamsungHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/samsung.html/'  
    
class SaruhanliSegHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/seg.html/'  

class SaruhanliSiemensHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/siemens.html/'  
    
class SaruhanliVestelHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/saruhanli/vestel.html/'  
    


#şehzadeler bölgesi beyaz eşya servisi

class SehzadelerArcelikHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/arcelik.html/'  

class SehzadelerAristonHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ariston']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/ariston.html/'  

class SehzadelerBekoHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/beko.html/'  

class SehzadelerBoschHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/bosch.html/'  

class SehzadelerLgHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/lg.html/'  

class SehzadelerProfiloHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['profilo']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/profilo.html/'  
    
class SehzadelerRegalHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/regal.html/'  

class SehzadelerSamsungHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/samsung.html/'  
    
class SehzadelerSegHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/seg.html/'  

class SehzadelerSiemensHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/siemens.html/'  
    
class SehzadelerVestelHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/sehzadeler/vestel.html/'  

#turgutlu bölgesi beyaz eşya servisi

class TurgutluArcelikHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/arcelik.html/'  

class TurgutluAristonHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ariston']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/ariston.html/'  

class TurgutluBekoHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/beko.html/'  

class TurgutluBoschHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/bosch.html/'  

class TurgutluLgHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/lg.html/'  

class TurgutluProfiloHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['profilo']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/profilo.html/'  
    
class TurgutluRegalHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/regal.html/'  

class TurgutluSamsungHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/samsung.html/'  
    
class TurgutluSegHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/seg.html/'  

class TurgutluSiemensHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/siemens.html/'  
    
class TurgutluVestelHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/turgutlu/vestel.html/'  


#yunusemre bölgesi beyaz eşya servisi

class YunusemreArcelikHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/arcelik.html/'  

class YunusemreAristonHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ariston']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/ariston.html/'  

class YunusemreBekoHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/beko.html/'  

class YunusemreBoschHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/bosch.html/'  

class YunusemreLgHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/lg.html/'  

class YunusemreProfiloHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['profilo']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/profilo.html/'  
    
class YunusemreRegalHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/regal.html/'  

class YunusemreSamsungHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/samsung.html/'  
    
class YunusemreSegHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/seg.html/'  

class YunusemreSiemensHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/siemens.html/'  
    
class YunusemreVestelHomeAppService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/servisler/beyaz-esya-servisi/yunusemre/vestel.html/'  


#markalar

class ArcelikService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['arcelik']  

    def location(self, item):
        return '/markalar/arcelik.html/'  

class AristonService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['ariston']  

    def location(self, item):
        return '/markalar/ariston.html/'  

class BekoService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beko']  

    def location(self, item):
        return '/markalar/beko.html/'  

class BoschService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bosch']  

    def location(self, item):
        return '/markalar/bosch.html/'  

class LgService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['lg']  

    def location(self, item):
        return '/markalar/lg.html/'  

class ProfiloService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['profilo']  

    def location(self, item):
        return '/markalar/profilo.html/'  

class RegalService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['regal']  

    def location(self, item):
        return '/markalar/regal.html/'  

class SamsungService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['samsung']  

    def location(self, item):
        return '/markalar/samsung.html/'  

class SegService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['seg']  

    def location(self, item):
        return '/markalar/seg.html/'  

class SiemensService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['siemens']  

    def location(self, item):
        return '/markalar/siemens.html/'  

class VestelService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['vestel']  

    def location(self, item):
        return '/markalar/vestel.html/'  
    


#bölgeler

class AkhisarService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['akhisar']  

    def location(self, item):
        return '/bolgeler/akhisar.html/'  

class SaruhanliService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['saruhanli']  

    def location(self, item):
        return '/bolgeler/saruhanli.html/'  

class SehzadelerService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['sehzadeler']  

    def location(self, item):
        return '/bolgeler/sehzadeler.html/'  

class TurgutluService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['turgutlu']  

    def location(self, item):
        return '/bolgeler/turgutlu.html/'  

class YunusemreService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['yunusemre']  

    def location(self, item):
        return '/bolgeler/yunusemre.html/'  


#servisler

class BeyazEsyaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['beyazesya']  

    def location(self, item):
        return '/servisler/beyaz-esya.html/'  
    
class BulasikMakinesiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['bulasik-makinesi']  

    def location(self, item):
        return '/servisler/bulasik-makinesi-servisi.html/'  

class BuzdolabiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['buzdolabi']  

    def location(self, item):
        return '/servisler/buzdolabi-servisi.html/'  

class CamasirMakinesiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['camasir-makinesi']  

    def location(self, item):
        return '/servisler/camasir-makinesi-servisi.html/'  

class KlimaService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['klima-servisi']  

    def location(self, item):
        return '/servisler/klima-servisi.html/'  

class KombiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['kombi-servisi']  

    def location(self, item):
        return '/servisler/kombi-servisi.html/'  

class KurutmaMakinesiService(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return ['kurutma-makinesi-servisi']  

    def location(self, item):
        return '/servisler/kurutma-makinesi-servisi.html/'  
