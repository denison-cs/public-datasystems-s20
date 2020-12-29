from lxml import etree

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
