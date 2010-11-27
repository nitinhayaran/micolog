This is weblog based on Micolog, which is origianlly developed by Xuming (https://github.com/xuming/micolog).
The version of mine contains some improvements, those are in line with the architecture of Wordpress. 

List of Improvements:
------------------------------------------------------------------------------
# Default Category
  ----------------
  Every Post must belong to an category. If category is not specified for any entry, it will belong to a "default category". 
  By default "Uncategorized" category is created on system initiation, and it is the default category.
  
# Permalink contains Category
  ---------------------------
  As there is a category associated with every post, the permalink structure can now contain category in URL structure. 
  
# Make automatic slug
  -------------------
  Slug is automatically created for posts, it's not specified.
  
# Make Tag slug
  -------------
  Tags also have a slug, and themes should take this into consideration. 
  One can get tag slug with the help of a filter "slugify". So the URL for any tag should be:
  <a href="/tag/{{tag|slugify|urlencode}}">{{tag}}</a>
  
# Strip Tags
  ----------
  On creation, tags are now stripped for any extra space character. 
  
# Support for short codes Elink, youtube tags
  -------------------------------------------
  Support for [elink] and [youtube] shortcodes. With these shortcodes one can easily put youtube video and an external link in any blog post.
  following are some example:
  [elink]http://www.google.com[/elink]            
  -------->  <a href="http://www.google.com" class="external">http://www.google.com</a>
  [elink caption="Google Search"]http://www.google.com[/elink] 
  -------->  <a href="http://www.google.com" class="external">Google Search</a>
  [youtube]http://www.youtube.com/watch?v=LXUSaVw3Mvk[/youtube]
  -------->  It will be replaced with its equivalent embed code.
  
  More shortcodes can be created on similar line of shortcodes in ./short_code_parsers/*.py
  
  
# Ping Comment Feed to Google Search Engine
  -----------------------------------------
  If there is any new comment in last one hour it will ping comment feed to google search engine. This can be removed from cron.yaml

# Meta Description
  ----------------
  We can now have meta description for any entry. 
  {{entry.meta_description}}
  This is nothing but 120 characters of stripped text for entry content.
  
# To have hidden pages
  --------------------
  Want to hide some pages link in top navigation, Just set menu order to -1 and save the page.
  
# Update Links for more than 1000 URLs
  ------------------------------------
  Due to limitation in google app engine, update link action wasn't working for more than 1000 URLs. Now it can work for all the URLs, even for more than 1000.
  Configuration > Tools > Rebuild URL (in admin panel)

  

##############################################################################
                                How to Start                             
##############################################################################
1.Change "app.yaml.sample" to "app.yaml"
2.Replace "Application: mlog " as "Application: <your Google App ID>"
3.Upload micolog use "Google App Engine Launcher"

