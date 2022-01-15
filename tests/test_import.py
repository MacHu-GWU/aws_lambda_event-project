# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import aws_lambda_event

    _ = aws_lambda_event.S3PutEvent
    _ = aws_lambda_event.SNSTopicNotificationEvent
    _ = aws_lambda_event.SQSEvent
    _ = aws_lambda_event.DynamodbUpdateEvent
    _ = aws_lambda_event.KinesisFirehoseEvent


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
