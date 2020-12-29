def buildURL(protocol, location, resource):
    """Construct a URL, given the protocol (with or without the trailing '://'), 
       a location, and a resource.
       Return: string version of the url
    """
    fmt1 = "{}{}{}"
    fmt2 = "{}://{}{}"
    if protocol[-3:] == "://":
        url = fmt1.format(protocol, location, resource)
    else:
        url = fmt2.format(protocol, location, resource)
    return url