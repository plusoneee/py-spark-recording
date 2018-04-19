

from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(
    feeder_threads=15,
    parser_threads=15,
    downloader_threads=15,
    storage={'root_dir': './output'})
google_crawler.crawl(keyword='cat',max_num=1000, file_idx_offset=0)
