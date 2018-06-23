class HtmlParser:
    """
    @param: content: content source code
    @return: a list of links
    """
    def parseUrls(self, content):
        # write your code here
        import re
        links = re.findall(r'\s*(?i)href\s*=\s*("|\')+([^"\'>\s]*)', content, re.I)
        links = [link[1] for link in links if len(link[1]) and not link[1].startswith('#')]
        return list(links)
