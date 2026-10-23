#!/usr/bin/env bash
# Monta los dos muestrarios a partir de los fotogramas de render_vrm.mjs.
# Uso: montar.sh <dir_trabajo> <carpeta_salida>   (dir_trabajo con f_retrato/ y f_puntual/)
set -euo pipefail
W=$1; O=$2; A="$(dirname "$0")/../../c36-2026-10-22/c36.mp3"; FUENTE=/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf
# 1 · Retrato: el avatar a pantalla completa, con la voz de MDS-045 (primeros 14 s)
ffmpeg -y -v error -framerate 25 -i "$W/f_retrato/f%04d.png" -t 14 -i "$A" \
  -c:v libx264 -pix_fmt yuv420p -crf 20 -c:a aac -b:a 128k -shortest "$O/retrato_1080x1920.mp4"
# 2 · Momento puntual: tarjeta de marca con el titular arriba y el avatar en la mitad de abajo (franja algo más clara detrás: la camiseta es del azul del fondo)
ffmpeg -y -v error -f lavfi -i "color=c=0x16213A:s=1080x1920:r=25:d=14" \
  -framerate 25 -i "$W/f_puntual/f%04d.png" -t 14 -i "$A" -filter_complex \
  "[0:v]drawbox=x=0:y=760:w=1080:h=1160:color=0x26385F@1:t=fill,drawtext=fontfile=$FUENTE:text='Cena de empresa.':fontcolor=0xFFB020:fontsize=110:x=(w-text_w)/2:y=420,\
drawtext=fontfile=$FUENTE:text='¿De quién te ríes más?':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=580[f];\
[1:v]scale=810:1440[av];[f][av]overlay=x=135:y=820:shortest=1[v]" \
  -map "[v]" -map 2:a -c:v libx264 -pix_fmt yuv420p -crf 20 -c:a aac -b:a 128k -shortest "$O/puntual_1080x1920.mp4"
ffmpeg -y -v error -ss 3.2 -i "$O/retrato_1080x1920.mp4" -frames:v 1 "$O/retrato_fotograma.png"
ffmpeg -y -v error -ss 3.2 -i "$O/puntual_1080x1920.mp4" -frames:v 1 "$O/puntual_fotograma.png"
