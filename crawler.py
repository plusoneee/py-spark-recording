

from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=15,
    parser_threads=15,
    downloader_threads=100,
    storage={'root_dir': './1410332003'})
google_crawler.crawl(keyword='doona bea',max_num=1000, file_idx_offset=0, min_size=None)
