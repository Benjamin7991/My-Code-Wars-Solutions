def domain_name(url):
    url = url.split('http://')
    url = ''.join(url)
    url = url.split('https://')
    url = ''.join(url)
    url = url.split('www.')
    url = ''.join(url)
    url = url.split('.')
    return url[0]
