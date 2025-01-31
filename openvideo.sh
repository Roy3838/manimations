#!/bin/bash

nohup vlc --no-osd --no-video-title-show --no-video-deco --loop --qt-minimal-view --qt-start-minimized --no-embedded-video --qt-notification=0 --qt-system-tray $1 &
