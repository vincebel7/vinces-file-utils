# vinces-file-utils
Re-implementations of various Linux file utilities

Usage:
python3 vfu.py <cmd>


### diff
Example:
python3 vfu.py diff difftest/testdir1 difftest/testdir2

Note: Runtime is O(m*n) for the time being... I believe by hashing I can rewrite this in O(m+n) when i have time
