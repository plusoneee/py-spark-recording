

from icrawler.builtin import GoogleImageCrawler
import sys


search_content = str(sys.argv[1])
out_put_dir = str(sys.argv[2])
print(out_put_dir)
google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=1,
    downloader_threads=100,
    storage={'root_dir': './'+ out_put_dir})
google_crawler.crawl(keyword=search_content,max_num=1000, file_idx_offset=0, min_size=None)
