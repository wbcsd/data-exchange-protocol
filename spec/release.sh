#!/bin/sh

pip3 install bikeshed && bikeshed update
sed -i '' 's@wbcsd.github.io/data-exchange-protocol/v2@wbcsd.github.io/tr/data-exchange-protocol@g' v2/header.include
make
mkdir -p ../release/diagrams

for i in v2/diagrams/*.svg; do
    cp $i ../release/diagrams/
done

cp v2/index.html ../release/
