#!/bin/sh

cd spec/v2
pip3 install bikeshed && bikeshed update
mv header.include_release header.include
rm index.html
make
mkdir -p ../release/diagrams

for i in diagrams/*.svg; do
    cp $i ../release/diagrams/
done

cp index.html ../release/