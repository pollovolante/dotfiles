#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

colorscript random
alias config='/usr/bin/git --git-dir=/home/edoardo/.dotfiles/ --work-tree=/home/edoardo'
