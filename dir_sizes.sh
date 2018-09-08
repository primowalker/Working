#!/bin/bash

du -sk * | awk '{size = $1/1024/1024 ; print size" GB" "\t" $2}' | sort -n
