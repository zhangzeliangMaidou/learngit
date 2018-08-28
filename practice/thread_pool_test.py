#!/usr/bin/env python
# -*- coding:utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import requests
import time

urls = [
"http://www.baidu.com",
    "http://www.qq.com",
    "http://www.360.com",
    "http://www.baidu.com",
    "http://www.qq.com",
    "http://www.360.com",
    "http://www.baidu.com",
    "http://www.qq.com",
    "http://www.360.com"
]
logging.basicConfig(
    level=logging.DEBUG,
    format="%(threadName)-10s: %(message)s"
)

def download(url):
    r = requests.get(url)
    return url, r

def main():
    with ThreadPoolExecutor(5, thread_name_prefix="zeliang") as executor:
        start_time = time.time()
        # method 1
        futures = [executor.submit(download, url) for url in urls]
        for future in as_completed(futures):
            as_completed(futures)
            try:
                logging.debug(future.result())
            except Exception as e:
                logging.debug(e)

        # method 2
        # futures_result = executor.map(download, urls, timeout=30)
        # for future in futures_result:
        #     try:
        #         logging.debug(future)
        #     except Exception as e:
        #         logging.debug(e)

        logging.debug(time.time()-start_time)




main()