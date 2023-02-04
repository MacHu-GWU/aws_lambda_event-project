# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.events.s3_put import S3PutEvent


class TestS3PutEvent:
    def test(self):
        event = S3PutEvent.fake()
        event_data = event.to_dict()
        assert event.to_dict() == event_data

        record = event.Records[0]

        _ = record.event_datetime
        _ = record.bucket
        _ = record.key
        _ = record.etag
        _ = record.size


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
