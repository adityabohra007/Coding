'''
Definition of BaseGFSClient
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
'''


class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        self.baseGFSClient = BaseGFSClient()
        self.chunkSize = chunkSize
        self.chunk = {}

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        if filename not in self.chunk:
            return
        content = ""
        chunkNum = self.chunk[filename]
        for i in xrange(chunkNum):
            subContent = self.baseGFSClient.readChunk(filename, i)
            if subContent:
                content += subContent
        return content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        length = len(content)
        chunkNum = length / self.chunkSize + 1
        self.chunk[filename] = chunkNum
        for i in xrange(chunkNum):
            subContent = content[i*self.chunkSize: (i+1)*self.chunkSize]
            self.baseGFSClient.writeChunk(filename, i, subContent)
            
