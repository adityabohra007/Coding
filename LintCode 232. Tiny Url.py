"""
通过随机生成的方式
"""
class TinyUrl:
    def __init__(self):
        self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.longUrl = {}
        self.shortUrl = {}
        
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        if url in self.longUrl:
            return self.longUrl[url]
        short = self.generateShortUrl()
        if short in self.shortUrl:
            short = self.generateShortUrl()
        self.longUrl[url] = short
        self.shortUrl[short] = url
        return short

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        if url in self.shortUrl:
            return self.shortUrl[url]
        return None
    
    def generateShortUrl(self):
        import random
        url = ''
        for _ in xrange(6):
            url += random.choice(self.chars)
        return 'http://tiny.url/' + url

"""
Solution 2: base62
"""
class TinyUrl2:
    def __init__(self):
        self.urlMap = {}
        
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        id = 0
        for c in url:
            id = (id * 256 + ord(c)) % 56800235584L
        
        while id in self.urlMap and self.urlMap[id] != url:
            id = (id + 1) % 56800235584L
        
        self.urlMap[id] = url
        return 'http://tiny.url/' + self.idToShortUrl(id)

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        shortUrl = url[-6:]
        return self.urlMap[self.shortUrltoId(shortUrl)]
    
    def idToShortUrl(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            s = ch[id % 62] + s
            id /= 62
        while len(s) < 6:
            s = 'a' + s
        
        return s
    
    def shortUrltoId(self, short_url):
        id = 0
        for c in short_url:
            if 'a' <= c and c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c and c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c and c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52
        return id
