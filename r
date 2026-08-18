#xvfb-run manimgl ind.py -w -r 1080x1920 --fps 30
# ffmpeg -i my.mov -c copy -movflags +faststart -bsf:a aac_adtstoasc patched_video.mp4
ffmpeg -i my.mov \
  -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
  -g 120 -movflags +faststart \
  -c:a aac -b:a 192k -af loudnorm=I=-14:LRA=11:TP=-1 \
  -bsf:a aac_adtstoasc \
  output_power_patch.mov