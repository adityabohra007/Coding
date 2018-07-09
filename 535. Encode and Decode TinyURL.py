class Codec:
    def __init__(self):
        self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.long = {}
        self.short = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long:
            return self.long[longUrl]
        shortUrl = self.getShortUrl()
        while shortUrl in self.short:
            shortUrl = self.getShortUrl()
        self.long[longUrl] = shortUrl
        self.short[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.short:
            return self.short[shortUrl]
        return None

    def getShortUrl(self):
        import random
        url = ''
        for i in xrange(6):
            url += random.choice(self.chars)
        return 'http://tinyurl.com/' + url


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
