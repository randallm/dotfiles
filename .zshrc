HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
zstyle :compinstall filename '/home/randall/.zshrc'

autoload -Uz compinit
compinit
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' \
        'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

export BROWSER="chromium"
export EDITOR="vim"
export G_FILENAME_ENCODING=utf-8
export LC_ALL="en_US.UTF-8"
export PATH=$PATH:/opt/android-sdk/platform-tools:/opt/android-sdk/platform-tools
export PS1="[%n@%m]$ "

alias taskmgr="ps at"
alias getprocess="ps -ef | grep"
alias v="amixer sset \"Master\" 15%"
alias git="hub"
alias ls='ls --color=auto'
alias calc='ipython -ic "from __future__ import division; from math import *; from random import *"'
