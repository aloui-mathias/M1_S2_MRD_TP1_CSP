#!/bin/bash

for n in 20 23 24 43 60 100
do
    python main.py -data=[3,$n]
done

for n in 60 66 67 100
do
    python main.py -data=[4,$n]
done

for n in 140 150 160 170 171
do
    python main.py -data=[5,$n]
done
