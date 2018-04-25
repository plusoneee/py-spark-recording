

from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
import sys
search_content = str(sys.argv[1])
out_put_dir = str(sys.argv[2])
print(out_put_dir)

bing_crawler = BingImageCrawler(downloader_threads=100,
                                storage={'root_dir':'./'+ out_put_dir})
bing_crawler.crawl(keyword=search_content, filters=None, offset=0, max_num=1000)

