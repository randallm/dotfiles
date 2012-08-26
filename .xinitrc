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

test `hostname` == 'skynet' && xfce4-power-manager && xbacklight -set 100
test `hostname` == 'manbearpig' && xset -b && conky -p 20 && volumeicon && deluged

xrdb ~/.Xresources &
redshiftgui &
conky -p 20 &
volumeicon &
dropboxd &

xsetroot -cursor_name left_ptr
bitlbee

test `hostname` == 'manbearpig' && exec ck-launch-session dbus-launch startxfce4
test `hostname` == 'skynet' && exec ck-launch-session dbus-launch qtile
