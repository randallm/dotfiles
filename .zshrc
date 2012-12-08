# history settings
HISTFILE=~/.histfile
HISTSIZE=100000
SAVEHIST=100000

## not really sure what this does
bindkey -e
zstyle :compinstall filename '/home/randall/.zshrc'
autoload -Uz compinit
compinit

# auto completion settings
zstyle ':completion:*' matcher-list 'm:{a-zA-Z}={A-Za-z}' \
        'r:|[._-]=* r:|=*' 'l:|=* r:|=*'

# default apps
export BROWSER="chromium"
export EDITOR="vim"

# PS1
export PS1="[%n@%m %~]$ "

# uniform look between QT and GTK
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"

# android dev
export PATH=$PATH:/opt/android-sdk/platform-tools:/opt/android-sdk/platform-tools

# steam beta workaround
alias steam='xdg-open steam://open/games'

# binds
alias ls='ls --color=auto'  # colored ls output
alias v="amixer sset \"Master\" 15%"
alias git="hub"
alias calc='python2 -ic "from __future__ import division; from math import *; from random import *"'

# insert sudo at beginning of line
insert_sudo () { zle beginning-of-line; zle -U "sudo " }
zle -N insert-sudo insert_sudo
bindkey "^[s" insert-sudo

# make delete key work
bindkey "^[[3~" delete-char
bindkey "^[3;5~" delete-char
