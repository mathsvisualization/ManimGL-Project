xvfb-run manimgl ind.py -w -r 1080x1920 --fps 30
# ffmpeg -i my.mov -c copy -movflags +faststart -bsf:a aac_adtstoasc patched_video.mov
./g