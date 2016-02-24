#!/usr/bin/env python
# vim: set expandtab shiftwidth=4 fileencoding=UTF-8:

"""Creates JSON for input to aws route53 change-resource-record-sets."""

import argparse
import json

def _syntax():
    parser = argparse.ArgumentParser(description=\
        'Creates an AWS Route53 record modification request body.'
    )
    parser.add_argument('verb', choices=['create', 'delete', 'upsert'])
    parser.add_argument(
        '--hosted-zone-id', required=True, help='AWS hosted zone ID'
    )
    parser.add_argument(
        '--name', required=True, help='DNS name, e.g., test.example.com.'
    )
    parser.add_argument(
        '--ttl', type=int, default=300, help='DNS record TTL (seconds)'
    )
    parser.add_argument(
        '--type', choices=['A'], default='A', help='DNS record type'
    )
    parser.add_argument(
        '--value', required=True, help='DNS record value, e.g., 192.0.2.1'
    )
    return parser

def main(verb, hosted_zone_id, name, ttl, type, value):
    print json.dumps({
        'HostedZoneId': hosted_zone_id,
        'ChangeBatch': {
            'Changes': [
                {
                    'Action': verb.upper(),
                    'ResourceRecordSet': {
                        'Name': name,
                        'Type': type,
                        'TTL': ttl,
                        'ResourceRecords': [
                            {
                                'Value': value,
                            }
                        ],
                    },
                },
            ],
        },
    })

if __name__ == "__main__":
    main(**vars(_syntax().parse_args()))
