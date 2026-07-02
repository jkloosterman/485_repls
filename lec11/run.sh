#!/bin/bash -xe
echo "Map:"
python3 map.py < data/input.txt | tee output/after_map.txt
echo ""
echo "Group:"
sort output/after_map.txt | tee output/after_group.txt
echo ""
echo "Reduce:"
python3 reduce.py < output/after_group.txt | tee output/after_reduce.txt
