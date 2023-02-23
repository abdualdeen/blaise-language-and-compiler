#!/usr/bin/env sh

if [ -z "$2" ]; then
	MAIN=project2
else
	MAIN=$1
	shift
fi

ARG=$1
shift

./run.sh "$MAIN" "$ARG" "$@" -P debug=True