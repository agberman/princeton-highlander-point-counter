Princeton Highlander Point Counter
=====
This script is for automatically counting points for the Princeton Highlander Magic: The Gathering format. Decklist files for input into the script should be created with one card name on each line of the text file. \*CMDR\* must follow all commander card names, and \*CMPN\* must follow all companion card names (see `tibalt_princeton_highlander.txt` for an example of a compliant text file).

Cloning this repository
---
```
git clone https://github.com/agberman/princeton-highlander-point-counter
```


Usage example
----
```
python princeton_highlander_point_counter.py --decklist tibalt_princeton_highlander.txt
```

Example output:
```
Chrome Mox - 1 pt.
Dockside Extortionist - 1 pt.
Imperial Seal - 1 pt.
Mana Vault - 1 pt.
Mox Diamond - 1 pt.
Mox Opal - 1 pt.
Sol Ring - 4 pt.

10 points total
```
