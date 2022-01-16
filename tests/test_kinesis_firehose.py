# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.kinesis_firehose import KinesisFirehoseEvent


class TestKinesisFirehoseEvent:
    data = {
        "invocationId": "invocationIdExample",
        "deliveryStreamArn": "arn:aws:kinesis:EXAMPLE",
        "region": "us-east-1",
        "records": [
            {
                "recordId": "49546986683135544286507457936321625675700192471156785154",
                "approximateArrivalTimestamp": 1495072949453,
                "data": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0IDEyMy4="
            }
        ]
    }

    def test(self):
        event = KinesisFirehoseEvent(self.data)
        record = event.records[0]
        _ = record.binary_data
        _ = record.approximate_arrival_datetime


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
