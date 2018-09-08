# Import statements
 
    from BaseHTTPServer import HTTPServer
    from BaseHTTPServer import BaseHTTPRequestHandler
    from socket import gethostname, gethostbyname
    import re
    import os
    import csv
    import time
 
    # Config values
 
    HTMLFILE1 = 'error.html'
    RESULTS_REPLACESTR = 'Results Here' # String to replace to show results
 
    # LISTEN PORT
 
    LISTENPORT=8800
 
    class GetHandler(BaseHTTPRequestHandler):
 
    menuhtml = ''
 
    # Let's add some color
    def color(self, t, c):
    return chr(0x1b)+"["+str(c)+"m"+t+chr(0x1b)+"[0m"
    def bold(self, t):
    return self.color(t,1)
    def green(self, t):
    return self.color(t, 32)
    def red(self, t):
    return self.color(t, 31)
 
    def display(self, find_code):
 
    ifile = open('complete_error_codes.csv', "rb")
    reader = csv.reader(ifile)
 
    rownum = 0
    results = ''
    for row in reader:
    if 'Class' in row:
    list1 = row
    elif find_code in row:
    list2 = row
    break
    # if rownum == 0:
    # header = row
    # else:
    # column = 0
    # if row[1] == str(code):
    # results = dict(zip(header, row))
    # print results
    # rownum += 1
    for key, value in zip(list1, list2):
    print '%s: %s' % ((self.red(key)), value)
    ifile.close()
    return results
 
 
    def getMenu(self):
 
    fin = open(HTMLFILE1, 'r')
    menuhtml = fin.read()
    fin.close()
 
    return menuhtml
 
    def do_GET(self):
 
    print 'Processing request: %s' % self.path
    page = self.getMenu()
    A = re.sub("", "", self.path)
    print ("%s" % A)
    A = A.strip("/?")
    nv = A.split("&")
    print nv
    code = nv[0]
    code = code.strip("code=")
    results = self.display(code)
    results = str(results)
    results = results.strip("{")
    results = results.strip("}")
    results = re.sub(",","\n", results)
    page = page.replace(RESULTS_REPLACESTR, '%s' % results)
    #return results
    self.send_response(200)
    self.end_headers()
    self.wfile.write(page)
 
 
    if __name__ == '__main__':
 
    # Lets do it
 
    # Set up a Zulu time zone
    os.environ['TZ'] = 'UTC+00UTC+00'
    time.tzset()
 
    myip = gethostbyname(gethostname())
 
    print 'Starting server on '+str(myip)+':'+str(LISTENPORT)+', use <Ctrl-C> o stop'
    server = HTTPServer(('0.0.0.0', LISTENPORT), GetHandler)
    server.serve_forever()
