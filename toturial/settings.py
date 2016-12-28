# -*- coding: utf-8 -*-

# Scrapy settings for toturial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'toturial'

SPIDER_MODULES = ['toturial.spiders']
NEWSPIDER_MODULE = 'toturial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'toturial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
 #  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
   #'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    #'Avail-Dictionary':'XprLfaXG',
   #'Cookie':'__Q_w_s_hat_seed=1; __Q_w_s__appDataSeed=1; tvfe_boss_uuid=054d9ca20d1740fc; __Q_w_s__QZN_TodoMsgCnt=1; pac_uid=1_496280405; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=8; RK=uMGrwsRTTS; luin=o0496280405; lskey=00010000c69025c3ad86030501aaf46a61d01f44963b762d83d98280ece1c5f0b703f6d62e3fbd27902695a4; o_cookie=496280405; pgv_info=ssid=s8727785542; pgv_pvid=107937668; ptisp=ctc; ptcz=f06a74fc35f365f4c3531d334d160d09c5f409d053786dc13e9f29047b9e95c2; pt2gguin=o0496280405; uin=o0496280405; skey=@eKqhjqC8C; p_uin=o0496280405; p_skey=DshvyGz3DGtsnv*PaYHX9muBPduGoBNWRIXXbYzQQGY_; pt4_token=P9gfQzDXpFnQ0AJwnicE4nLlwyEj99b64ltnqmWe0CU_; qzone_check=496280405_1472308185; qzspeedup=sdch; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; g_ut=2; qzmusicplayer=qzone_player_1502680353_1472308191098',
#}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'toturial.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'toturial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'toturial.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
