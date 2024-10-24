#!/bin/sh

cd spec/v2

mv header.include header.include_temp
mv header.include_release header.include
rm index.html

if [ "$DRAFT" = "true" ]; then
    RELEASE_STATUS="RELEASE Consultation Draft"
else
    RELEASE_STATUS="RELEASE Stable Release"
fi
make STATUS="$RELEASE_STATUS"

mkdir -p ../release/diagrams

for i in diagrams/*.svg; do
    cp $i ../release/diagrams/
done

cp index.html ../release/

mv header.include header.include_release
mv header.include_temp header.include
