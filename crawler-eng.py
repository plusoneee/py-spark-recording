
from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=200,
    storage={'root_dir': './1410332003'})
google_crawler.crawl(keyword='cat', offset=0, max_num=1000,
                     min_size=None, max_size=None, file_idx_offset=0)

bing_crawler = BingImageCrawler(downloader_threads=4,
                                storage={'root_dir': './1410332003'})
bing_crawler.crawl(keyword='cat', filters=None, offset=0, max_num=1000)

baidu_crawler = BaiduImageCrawler(storage={'root_dir': './1410332003'})
baidu_crawler.crawl(keyword='cat', offset=0, max_num=1000,
                    min_size=None, max_size=None)
