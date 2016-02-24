#!/bin/sh

test -n "$HOSTED_ZONE_ID" || {
    echo "Error: missing required environment variable HOSTED_ZONE_ID" >&2
    exit 2
}
test -n "$NAME" || {
    echo "Error: missing required environment variable NAME" >&2
    exit 2
}

aws route53 change-resource-record-sets --cli-input-json "$(
    ./route53tool.py upsert --hosted-zone-id $HOSTED_ZONE_ID --name $NAME --value $(
        curl -sS http://169.254.169.254/latest/meta-data/public-ipv4
    )
)"

# vim: set expandtab shiftwidth=4:
