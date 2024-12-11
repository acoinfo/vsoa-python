#!/usr/bin/env bash

VERSION=`sed -n 's/version = "\(.*\)"/\1/p' pyproject.toml`

FILES=(dist/vsoa-${VERSION}*)

function test () {
	echo Test version $VERSION
	echo To be done...
	echo
}

function build () {
	if [[ ${FILES} == "dist/vsoa-${VERSION}*" ]]; then
		echo Build version $VERSION
		python3 -m build
	else
		echo Build version $VERSION, skipped...
		ls -l ${FILES[@]} | awk '{print $9" "$5" "$6$7" "$8}' | column -t
	fi
	echo
}

function publish () {
	echo Publish version $VERSION
	python3 -m twine upload --skip-existing --config-file .pypirc ${FILES[@]}
}

test && build && publish