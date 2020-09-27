import urllib.request, urllib.parse, urllib.error

url = input('Enter url\n')
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())
