import urllib.request, urllib.parse, urllib.error

url = "https://anastl.github.io/web4kids/index.html"
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())