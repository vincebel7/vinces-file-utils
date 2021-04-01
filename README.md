# vinces-file-utils
Re-implementations of various Linux file utilities, and a few utilities of my own

Usage:

	python3 vfu.py <cmd>


### diff

Compare two files or directories (directories only for now)

Directory comparison is recursive.

Example:

	python3 vfu.py diff difftest/testdir1 difftest/testdir2

Note: Runtime is O(m*n) for the time being... I believe by hashing I can rewrite this in O(m+n) when i have time

### rename

Rename files in bulk, using a pattern

Examples:

	python3 vfu.py rename myfile.py F@.backup

Becomes: myfile.py.backup
	
	python3 vfu.py rename * X@-revisedE@

Becomes: myfile-revised.py, myfile-revised.sh

Syntax:

F@ - filename, including extension

X@ - filename, excluding extension

E@ - file extension

Note: * is not supported yet, single files only for now
