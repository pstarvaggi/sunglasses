# Sunglasses Hut Web Scraping for Product Details and Brand Comparisons

This project has a few components.

1) sunglass_hut/sunglass_hut folder is a Scrapy Spider that scrapes the Sunglass Hut for product details on all of their sunglasses. First, sunglass_hut.py, which is in the outer sunglass_hut folder, must run to scrape the urls into url.csv using Selenium. This is then passed to the spider folder. It is currently urls_copy.csv

2) Woot! is also scraped for it's sunglasses and details. That spider is contained in the sunglasses folder.

3) The jupyter notebook sunglass_hut_woot_eda.ipynb explores the data and matches sunglasses on woot! with possible matches on sunglass hut.

4) There is a keynote presentation for further explanation, sunglass_hut_woot.
