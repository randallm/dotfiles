#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

alias calc='ipython2 -ic "from __future__ import division; from math import *; from random import *"'

export WINEDEBUG=-all
export EDITOR="vim"
export HISTSIZE=1000
export G_FILENAME_ENCODING=utf-8
export LC_ALL="en_US.UTF-8"

alias suspend='sudo clear && i3lock -c 000000 && sudo pm-suspend'
alias getprocess='ps -ef | grep'
