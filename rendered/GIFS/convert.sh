 #!/bin/bash

# Set the folder containing the MP4 files
folder="/home/jay/manimations/renderffmpeg/rendered/"

# Loop over all the MP4 files in the folder
for file in "$folder"/*.mp4
do
  # Use ffmpeg to convert the MP4 file to a GIF
  ffmpeg -i "$file" "${file%.mp4}.gif"
done

