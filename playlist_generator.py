#!-*- coding: utf-8 -*-
import argparse
import json
from mutagen.easyid3 import EasyID3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='*')
    parser.add_argument('--poster', help = 'Imagen a mostrar en el playlist')
    parser.add_argument('-p', '--prefix', default = '', help = 'Prefijo a usar (puede ser el directorio remoto en URL)')
    args = parser.parse_args()

    playlist = list()
    for f in args.files:
        #Cargo los metadatos
        cancion = dict()
        audio = EasyID3(f)
        cancion['title'] = audio['title'][0]
        cancion['artist'] = audio['artist'][0]
        cancion['free'] = True # Con link a la descarga
        if args.poster:
            cancion['poster'] = args.prefix + args.poster
        cancion['mp3'] = args.prefix + f
        playlist.append(cancion)
    print json.dumps(dict(playlist = playlist))

if __name__ == '__main__':
    main()

