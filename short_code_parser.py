import re
import short_code_parsers


def import_parser(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

def parse(value):
 # The regular expresion contains 6 different sub matches to help with parsing.
 #
 # 1/6 - An extra [ or ] to allow for escaping shortcodes with double [[]]
 # 2 - The shortcode name
 # 3 - The shortcode argument list
 # 4 - The self closing /
 # 5 - The content of a shortcode when it wraps some content.
 #
 # Idea taken from wordpress
 #
            
    regex = r'(.?)\[(youtube|elink)\b(.*?)(?:(\/))?\](?:(.+?)\[\/\2\])?(.?)'
    #regex = r'(\[)(youtube|elink)\b(.*?)(?:(\/))?\](?:(.+?)\[\/\2\])?'
    ex = re.compile(regex)
    groups = ex.findall(value)
    parsed = value
    index = 0
    for item in groups:
        name = item[1]
        args = parse_args(item[2])
        content = item[4]
        
        try:
            module = import_parser('short_code_parsers.' + name)
            function = getattr(module, 'parse')
            result = function(args, content)
            parsed = re.sub(regex, item[0] + result + item[5], parsed, 1)
        except ImportError:
            pass
        
    return parsed

def parse_args(value):
    ex = re.compile(r'[ ]*(\w+)=([^" ]+|"[^"]*")[ ]*(?: |$)')
    groups = ex.findall(value)
    kwargs = {}
    
    for group in groups:
        if group.__len__() == 2:
            item_key = group[0]
            item_value = group[1]
            
            if item_value.startswith('"'):
                if item_value.endswith('"'):
                    item_value = item_value[1:]
                    item_value = item_value[:item_value.__len__() - 1]
            
            kwargs[item_key] = item_value
            
    return kwargs