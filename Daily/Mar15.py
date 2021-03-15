'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''

from random import choice

class Codec:
    
    def __init__(self):
        self.ltsmap = {}
        self.stlmap = {}
        self.base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        if longUrl in self.ltsmap:
            return self.ltsmap[longUrl]
        
        while True:
            key = 'http://tinyurl.com/' + ''.join(choice(self.base) for i in range(6))
            if key not in self.stlmap:
                self.ltsmap[longUrl] = key
                self.stlmap[key] = longUrl
                break;
                
        return key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.stlmap:
            return self.stlmap[shortUrl]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))