from HTMLParser import HTMLParser
import urllib2

class MyFancyHTMLParser(HTMLParser):
  def fetch_url(self, url) :
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    link = response.geturl()
    html = response.read()
    response.close()
    self.feed(html)   # feed() starts the HTMLParser parsing

  def handle_starttag(self, tag, attrs):
    if tag == 'img' :
      # attrs is a list of tuples, (attribute, value)
      srcindex = self.has_attr('src', attrs)
      if srcindex < 0 :
        return   # img with no src tag? skip it
      src = attrs[srcindex][1]
      # Make relative URLs absolute
      src = self.make_absolute(src)
      attrs[srcindex] = (attrs[srcindex][0], src)

    print '<' + tag
    for attr in attrs :
      print ' ' + attr[0]
      if len(attr) > 1 and type(attr[1]) == 'str' :
        # make sure attr[1] doesn't have any embedded double-quotes
        val = attr[1].replace('"', '\"')
        print '="' + val + '"'
    print '>'

  def handle_endtag(self, tag):
    self.outfile.write('</' + tag.encode(self.encoding) + '>\n')


c=MyFancyHTMLParser()
c.fetch_url('http://www.theguardian.com/world/2014/may/19/narendra-modi-india-election-victory-america-china-pakistan-world')


