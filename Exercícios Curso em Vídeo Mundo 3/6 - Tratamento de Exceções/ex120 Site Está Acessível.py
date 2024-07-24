import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except(urllib.error.URLError):
    print('O site Youtube.com não está acessível no momento.')
else:
    print('Consegui acessar o site Youtube.com com sucesso!')