# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.kinesis_stream import KinesisStreamEvent


class TestKinesisFirehoseEvent:
    data = {
        "Records": [
            {
                "kinesis": {
                    "partitionKey": "partitionKey-03",
                    "kinesisSchemaVersion": "1.0",
                    "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0IDEyMy4=",
                    "sequenceNumber": "49545115243490985018280067714973144582180062593244200961",
                    "approximateArrivalTimestamp": 1428537600
                },
                "eventSource": "aws:kinesis",
                "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",
                "invokeIdentityArn": "arn:aws:iam::EXAMPLE",
                "eventVersion": "1.0",
                "eventName": "aws:kinesis:record",
                "eventSourceARN": "arn:aws:kinesis:EXAMPLE",
                "awsRegion": "us-east-1"
            }
        ]
    }

    def test(self):
        event = KinesisStreamEvent(self.data)
        record = event.records[0]
        _ = record.kinesis_partition_key
        _ = record.kinesis_binary_data
        _ = record.kinesis_approximate_arrival_datetime
        _ = record.kinesis_sequence_number


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
