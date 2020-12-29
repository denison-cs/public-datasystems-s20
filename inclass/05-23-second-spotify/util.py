import json
import os.path
import random
import string
from lxml import etree

def buildURL(resource_path, host="http.bin", protocol="https", 
             extension=None, port=None):
    if resource_path[0] != '/':
        resource_path = '/' + resource_path
    
    if extension != None:
        resource_path += "." + extension
        
    if port != None:
        host = host + ":{}".format(port)
    
    url_template = "{}://{}{}"
    url = url_template.format(protocol, host, resource_path)
    return url

def read_creds(key, folder=".", file="creds.json"):
    path = os.path.join(folder, file)
    assert os.path.isfile(path)
    with open(path, "rt") as f:
        creds = json.load(f)
    assert key in creds
    return creds[key]

def update_creds(key, keycreds, folder=".", file="creds.json"):
    path = os.path.join(folder, file)
    assert os.path.isfile(path)
    with open(path, "rt") as f:
        creds = json.load(f)
    assert key in creds
    creds[key] = keycreds
    creds_string = json.dumps(creds, indent=2)
    with open(path, "wt") as f:
        f.write(creds_string)
        f.flush()

def json_head(json_ds, numlines=5):
    json_string = json.dumps(json_ds, indent=2)
    i = 0
    linecount = 0
    while i < len(json_string) and linecount < numlines:
        try:
            i = json_string.index('\n', i+1)
        except:
            i = len(json_string)
        linecount += 1
    #print(i, len(json_string))
    print(json_string[:i])
    
def random_string(length=8):
    # using random.choices() 
    # generating random strings  
    res = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k = length))
    return res

def attr_string(node):
    s = ''
    for k, v in node.attrib.items():
        nextval = " {}='{}'".format(k, v)
        s += nextval
    return s

def print_leaf_node(node, level):
    indent = level*'  '
    tag_string = "<{}{}>".format(node.tag, attr_string(node))
    nodetext = str(node.text).strip()
    if node.text != None and nodetext != '':
        tag_string += nodetext + ''
    end_tag = "</{}>".format(node.tag)
    print(indent, tag_string, end_tag, sep='')
    
def print_start_tag(node, level):
    indent = level*'  '
    tag_string = "<{}{}>".format(node.tag, attr_string(node))
    nodetext = str(node.text).strip()
    if node.text != None and nodetext != '':
        tag_string += nodetext + ''
    print(indent, tag_string, sep='')

def print_end_tag(node, level):
    indent = level*'  '
    tag_string = "</{}>".format(node.tag)
    print(indent, tag_string, sep='')


def print_levels(node, level, maxlevel, maxchildren=30):
    if len(node) == 0:
        print_leaf_node(node, level)
    else:
        print_start_tag(node, level)
        if len(node) > 0 and level < maxlevel:
            for i, child in enumerate(node):
                if i < maxchildren:
                    print_levels(child, level+1, maxlevel, maxchildren)
                else:
                    print((level+1)*'  ', '...')
                    break
        print_end_tag(node, level)
        
def print_tree(node, pretty_print=True, encoding='utf-8', limit=0):
    result = etree.tostring(node, pretty_print=pretty_print)
    if isinstance(result, bytes):
        result = result.decode(encoding)
    if limit > 0:
        print(result[:limit])
    else:
        print(result)
        
def print_results(nodeset, maxlevel=2, maxchildren=5):
    """
    This function iterates over all Elements in a given list
    of Elements, printing the tag, text, and attributes of each.
    
    Parameters:
    nodeset - a list of Elements
    """
    print("Length of nodeset result:", len(nodeset))
    for element in nodeset:
        print("Type:", type(element))
        if type(element) == etree._Element:
            print_levels(element, 0, maxlevel, maxchildren)
        else:
            print(element)
        print()

haschildren = lambda node: isinstance(node, list) or isinstance(node, dict)

def print_scalar(v):
    if isinstance(v, str):
        print('"' + v + '"', sep='',end="")
        return
    if isinstance(v, int) or isinstance(v, float):
        print(v, sep='',end="")
        return
    
def print_json(node, level, maxlevel=5, maxchildren=5):
    if isinstance(node, str):
        print(level*'  ','"' + node + '"', sep='')
        return
    if isinstance(node, int) or isinstance(node, float):
        print(level*'  ',node, sep='')
        return
    
    assert isinstance(node, list) or isinstance(node, dict)
    
    if isinstance(node, list):
        print(level*'  ', '[')
        if level < maxlevel:
            for i, item in enumerate(node):
                if i < maxchildren:
                    print_json(item, level+1, maxlevel, maxchildren)
                else:
                    print((level+1)*'  ', '...')
                    break
        print(level*'  ', ']')
        return
    if isinstance(node, dict):
        print(level*'  ', '{')
        if level <= maxlevel:
            i = 0
            for k,v in node.items():
                if i < maxchildren:
                    print((level+1)*'  ','"',k,'": ',sep="",end="")
                    if haschildren(v):
                        print()
                        print_json(v, level+1, maxlevel, maxchildren)
                    else:
                        print_scalar(v)
                        print()
                    i += 1
                else:
                    print((level+1)*'  ', '...')
                    break
        else:
            print((level+1)*'  ', '...')
        print(level*'  ', '}')
        return