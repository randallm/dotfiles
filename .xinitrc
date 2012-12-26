#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

# colors
xrdb ~/.Xresources &
redshiftgui &

# tray icon for volume
volumeicon &

# downloads
sabnzbd &
transmission-qt -m &

pidgin &
guake &
adeskbar &

exec fusion-icon
