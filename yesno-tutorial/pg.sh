#!/usr/bash

a=1
b=2

for ((argpos=1; argpos<$#; argpos++)); do
  if [ "${!argpos}" == "--config" ]; then
    argpos_plus1=$((argpos+1))
    config=${!argpos_plus1}
    [ ! -r $config ] && echo "$0: missing config '$config'" && exit 1
    . $config  # source the config file.
  fi
done

