#!/usr/bin/env python
#-*- coding: utf-8 -*-
import argparse
import json
from mutagen.easyid3 import EasyID3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='*')
    parser.add_argument('--poster', help = 'Imagen a mostrar en el playlist')
    parser.add_argument('-p', '--prefix', default = '/shared/', help = 'Prefijo a usar (puede ser el directorio remoto en URL)')
    parser.add_argument('-a', '--artist', help = 'Nombre del artista para todas las canciones')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()

    playlist = list()
    for f in args.files:
        #Cargo los metadatos
        cancion = dict()
        try:
            audio = EasyID3(f)
        except:
            # El fichero no tiene metadatos
            cancion['title'] = raw_input('Título para %s: ' % f).decode('utf8')
            cancion['artist'] = args.artist or raw_input('Artista de %s: ', f).decode('utf8')
        else:
            cancion['title'] = audio['title'][0]
            cancion['artist'] = args.artist or audio['artist'][0]
            cancion['free'] = True # Con link a la descarga
        if args.poster:
            cancion['poster'] = args.prefix + args.poster
        cancion['mp3'] = args.prefix + f
        playlist.append(cancion)

    j = dict(playlist = playlist)
    if args.output:
        json.dump(j, open(args.output, 'w'))
    else:
        print json.dumps(j)

if __name__ == '__main__':
    main()

