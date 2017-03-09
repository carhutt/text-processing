#!/bin/bash
for f in *.txt; do
  python HTMLtable.py "$f" > "$f.html"
done