# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.events.kinesis_firehose import KinesisFirehoseEvent


class TestKinesisFirehoseEvent:
    def test(self):
        event = KinesisFirehoseEvent.fake()
        event_data = event.to_dict()
        assert event.to_dict() == event_data

        record = event.records[0]

        _ = record.binary_data
        _ = record.approximate_arrival_datetime


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
