import urllib2
import webbrowser
import simplejson as json
 
class randomWikiArticle():
    curidList = []
 
    def wikiAPI(self):
        random = urllib2.urlopen("http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json").read()
        print "Select the Topic:\n"
        return random
 
    def parseValue(self, parseData):
        global curidList
        curidList = []
        parsedData = json.loads(parseData)
        for key,value in parsedData['query'].iteritems():
            for i in range(0, 10):
                for k,v in value[i].iteritems():
                    if (k == 'id'):
                        curidList.append(v) 
                    if (k == 'title'):
                        print i+1, v.encode('utf-8')
 
    def openURL(self):
        var = input('\n')
        webbrowser.open_new("http://en.wikipedia.org/wiki?curid="+str(curidList[var]))
 
    def init(self):
        random = randomWikiArticle().wikiAPI()
        randomWikiArticle().parseValue(random)
        randomWikiArticle().openURL()
 
if __name__ == '__main__':
    randomWikiArticle().init()
