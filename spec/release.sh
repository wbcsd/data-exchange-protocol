#!/bin/sh

cd spec/v2
pip3 install bikeshed && bikeshed update
make
mkdir -p ../release/diagrams

for i in diagrams/*.svg; do
    cp $i ../release/diagrams/
done

cp index.html ../release/
