def remove_url_anchor(url):
    for i in range(len(url)):
        if url[i] == '#':
            return url[:i]
    return url
