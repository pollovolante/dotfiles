#!/bin/bash

killall conky
sleep 2s
		
conky -c $HOME/.config/conky/"Regulus Cinnamon"/Regulus.conf &> /dev/null &
