import scrapy
import unicodedata
from scrapy.http import Request

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'mirc'
    allowed_domains = ['mirc.sc.edu']
    start_urls = [ "http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%29/",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=1",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=2",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=3",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=4",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=5",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=6",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=7",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=8",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=9",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=10",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=11",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=12",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=13",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=14",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=15",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=16",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=17",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=18",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=19",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=20",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=21",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=22",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=23",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=24",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=25",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=26",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=27",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=28",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=29",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=30",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=31",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=32",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=33",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=34",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=35",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=36",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=37",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=38",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=39",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=40",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=41",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=42",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=43",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=44",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=45",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=46",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=47",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=48",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=49",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=50",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=51",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=52",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=53",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=54",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=55",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=56",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=57",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=58",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=59",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=60",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=61",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=62",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=63",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=64",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=65",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=66",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=67",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=68",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=69",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=70",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=71",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=72",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=73",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=74",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=75",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=76",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=77",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=78",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=79",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=80",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=81",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=82",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=83",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=84",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=85",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=86",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=87",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=88",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=89",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=90",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=91",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=92",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=93",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=94",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=95",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=96",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=97",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=98",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=99",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=100",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=101",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=102",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=103",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=104",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=105",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=106",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=107",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=108",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=109",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=110",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=111",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=112",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=113",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=114",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=115",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=116",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=117",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=118",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=119",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=120",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=121",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=122",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=123",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=124",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=125",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=126",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=127",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=128",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=129",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=130",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=131",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=132",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=133",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=134",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=135",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=136",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=137",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=138",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=139",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=140",
"http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=141" ,
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=142',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=143',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=144',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=145',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=146',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=147',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=148',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=149',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=150',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=151',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=152',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=153',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=154',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=155',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=156',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=157',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=158',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=159',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=160',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=161',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=162',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=163',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=164',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=165',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=166',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=167',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=168',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=169',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=170',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=171',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=172',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=173',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=174',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=175',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=176',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=177',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=178',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=179',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=180',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=181',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=182',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=183',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=184',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=185',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=186',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=187',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=188',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=189',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=190',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=191',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=192',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=193',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=194',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=195',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=196',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=197',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=198',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=199',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=200',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=201',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=202',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=203',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=204',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=205',
'http://mirc.sc.edu/islandora/search/catch_all_txt%3A%28*%3A*%29?page=206' ]

    def parse(self, response):
        BASE_URL = 'http://mirc.sc.edu'
        
        for sel in response.xpath('//div[@class="islandora-solr-search-result-inner"]'):
            item = DmozItem()
            item['image_urls'] = sel.xpath('dl/dt/a/img/@src').extract()
            identifier = sel.xpath('dl/dt/a/@href').extract()
            item['identifier'] = identifier
            item['title'] = sel.xpath('dl/dd[@class="solr-value pb-parent-title-main-ms"]/text()').extract()
            item['desc'] = sel.xpath('dl/dd[@class="solr-value pb-parent-description-summary-ms"]/text()').extract()
            absolute_url = BASE_URL + str(identifier[0])
            request = Request(absolute_url, callback=self.parse_vid)
            request.meta['item'] = item
            yield request


    def parse_vid(self, response):
        item = response.meta['item']
        item['vid_url'] = response.xpath('//a[@class="usc-flowplayer"]/@href').extract()
        return item
