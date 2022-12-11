 #!/bin/bash

# Set the folder containing the MP4 files
folder="/home/jay/manimations/rendered/"

# Loop over all the MP4 files in the folder
for file in "$folder"/*.mp4
do
  # Use ffmpeg to convert the MP4 file to a GIF
  # skip if file already exists
  if [ -f "${file%.mp4}.gif" ]; then
    echo "skipping $file"
    continue
  fi
    ffmpeg -i "$file" "${file%.mp4}.gif"
done

