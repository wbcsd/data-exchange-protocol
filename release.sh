#!/bin/sh

# This creates a new "release" of the tech specs.
# It requires 1 argument which is the status of this new release, which should be either
# - Consultation Draft
# - Release             [exact name to be checked]
#
# The script does the following
#
# 1. It first computes the release date in the format YYYYMMDD
# 2. it creates a new computed-metadata.include file
# 3. derives the HTML file locally as usual
# 4. clones the TR repository and pushes a release there

TR_REPO_URL="git@github.com:sine-fdn/tr"


if [ -z "$1" ]; then
    echo "Usage: $0 <Consultation Draft|Release>"
    exit 1
fi

set -euo pipefail

pushd spec/v2

STATUS="$1"
RELEASE_DATE=$(date +%Y%m%d)
PREV_VERSION=$(jq .TR < computed-metadata.include)
YEAR=$(date +%Y)


## create a new computed-metadata.include file
cat <<EOF > computed-metadata.include
{
  "Previous Version": ${PREV_VERSION},
  "TR": "https://wbcsd.github.io/tr/${YEAR}/data-exchange-protocol-${RELEASE_DATE}/",
  "Text Macro": "STATUS ${STATUS}"
}
EOF

echo "computed-metadata.include file successfully updated"

## create the release
make publish clean

popd

## check out the TR repository if it does not exist, yet
test -d ../tr || git clone ${TR_REPO_URL} ../tr

## add the newly created release to the TR repository
rm -rf ../tr/data-exchange-protocol
cp -r upload/v2/ ../tr/data-exchange-protocol
cp -r upload/v2/ ../tr/${YEAR}/data-exchange-protocol-${RELEASE_DATE}

## commit the release and push it back to GH
cd ../tr
git fetch origin main
git remote prune origin
git checkout -b release-${RELEASE_DATE} origin/main
git add .
git commit -m "Release data-exchange-protocol ${RELEASE_DATE}"
git push origin release-${RELEASE_DATE}
git checkout origin/main
