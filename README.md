# coc-crypto

A simple Clash of Clans proxy in Python.

Run with:

	python2.7 proxy.py

## Setup

### Modules

The following modules must be installed for proper use:

Install `pynacl` with:

	python2.7 pip install pynacl

Install `pyblake2` with:

	python2.7 pip install pyblake2

### Game patching

Moreover, it is necessary to modify the public key in the libg.so file.
The offsets of the keys for each game version can be found [here](https://github.com/clugh/coc-proxy/wiki/Key-Offsets).

### Routing packets

The packets must be routed through the proxy.