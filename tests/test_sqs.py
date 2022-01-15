# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.sqs import SQSEvent


class TestSQSEvent:
    data = {
        "Records": [
            {
                "messageId": "19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
                "receiptHandle": "MessageReceiptHandle",
                "body": "Hello from SQS!",
                "attributes": {
                    "ApproximateReceiveCount": "1",
                    "SentTimestamp": "1523232000000",
                    "SenderId": "123456789012",
                    "ApproximateFirstReceiveTimestamp": "1523232000001"
                },
                "messageAttributes": {},
                "md5OfBody": "{{{md5_of_body}}}",
                "eventSource": "aws:sqs",
                "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
                "awsRegion": "us-east-1"
            }
        ]
    }

    def test(self):
        event = SQSEvent(**self.data)
        _ = event.records[0]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
