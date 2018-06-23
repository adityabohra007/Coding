'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        result = {}
        for doc in docs:
            for content in doc.content.split():
                if content in result:
                    if result[content][-1] != doc.id:
                        result[content].append(doc.id)
                else:
                    result[content] = [doc.id]
        return result
