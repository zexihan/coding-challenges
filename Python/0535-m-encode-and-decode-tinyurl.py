# Using Simple Counter
class Codec_1:

    def __init__(self):
        self.i = 0
        self.map = {}
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.map[self.i] = longUrl
        shortUrl = "http://tinyurl.com/" + str(self.i)
        self.i += 1
        return shortUrl 
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.map.get(int(shortUrl.replace("http://tinyurl.com/","")))

# Variable-length Encoding        
class Codec_2:

    def __init__(self):
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.count = 1
        self.map = {}

    def getString(self):
        c = self.count
        sb = ""
        while c > 0:
            c -= 1
            sb += self.chars[c % 62]
            c //= 62   
        return sb 

    def encode(self, longUrl):
        key = self.getString()
        self.map[key] = longUrl
        self.count += 1
        return "http://tinyurl.com/" + key


    def decode(self, shortUrl):
        return self.map.get(shortUrl.replace("http://tinyurl.com/",""))
        
# Using hashcode
# import hashlib
class Codec_3:

    def __init__(self):
        self.map = {}

    def encode(self, longUrl):
        # hash = hashlib.md5(bytes(longUrl,encoding='utf-8')).hexdigest()
        hashcode = abs(hash(longUrl))
        self.map[hashcode] = longUrl
        return "http://tinyurl.com/" + str(hashcode)

    def decode(self, shortUrl):
        return self.map.get(int(shortUrl.replace("http://tinyurl.com/","")))

# Random fixed-length encoding
import random
class Codec_4:

    def __init__(self):
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.map = {}
        self.key = self.getRand()

    def getRand(self):
        sb = ""
        for i in range(6):
            sb += self.alphabet[random.randint(0,61)]
        return sb

    def encode(self, longUrl):
        while self.key in self.map:
            self.key = self.getRand()
        self.map[self.key] = longUrl
        return "http://tinyurl.com/" + self.key


    def decode(self, shortUrl):
        return self.map.get(shortUrl.replace("http://tinyurl.com/", ""))


# Your Codec object will be instantiated and called as such:
codec = Codec_4()

print(codec.encode("https://leetcode.com/problems/design-tinyurl"))
print(codec.encode("https://leetcode.com/problems/design-tinyurlsdv"))
print(codec.encode("https://leetcode.com/problems/design-tinyurlswa"))