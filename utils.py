import re
def slugify(inStr):
    inStr = inStr.replace('-','')
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for","from","is", "in", "into", "like", "of", "off", "on", "onto","per","since", "than", "the", "this", "that", "to", "up", "via","with"];
    for a in removelist:
        aslug = re.sub(r'\b'+a+r'\b','',inStr)
    aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
    aslug = re.sub('\s+', '-', aslug)
    return aslug
    
def strip_tags(text, valid_tags={}):
    from BeautifulSoup import BeautifulSoup, Comment
    
    soup = BeautifulSoup(text)
    for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
        comment.extract()
    for tag in soup.findAll(True):
        if tag.name in valid_tags:
            valid_attrs = valid_tags[tag.name]
            tag.attrs = [(attr, val.replace('javascript:', '')) 
                for attr, val in tag.attrs if attr in valid_attrs]
        else:
            tag.hidden = True
    return soup.renderContents().decode('utf8')

def trim_excerpt_without_filters(text):
    MAXIMUM_DESCRIPTION_LENGTH = 120
    text = text.replace(']]>', ']]&gt;')
    text = re.sub( '|\[(.+?)\](.+?\[/\\1\])?|s', '', text )
    text = strip_tags(text)
    max = MAXIMUM_DESCRIPTION_LENGTH
    
    if (max < len(text)):
        while( text[max] != ' ' and max > MAXIMUM_DESCRIPTION_LENGTH ):
            max -= 1
    text = text[:max]
    return text.strip()