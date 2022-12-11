 #!/bin/bash

# Set the folder containing the MP4 files
folder="/home/jay/manimations/rendered/"

# Loop over all the MP4 files in the folder
for file in "$folder"/*.mp4
do

    # calculate width and height for scale 1/4
    w=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=s=x:p=0 "$file")
    h=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=s=x:p=0 "$file")
    w=$(echo "scale=0; $w / 4" | bc)
    h=$(echo "scale=0; $h / 4" | bc)

  # Use ffmpeg to convert the MP4 file to new size
  # ffmpeg -i input.mp4 -vf scale=$w:$h <encoding-parameters> output.mp4
    ffmpeg -i "$file" -vf scale="$w:$h" "${file%.mp4}-resized.mp4"
done

