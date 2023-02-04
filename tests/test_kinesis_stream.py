# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.events.kinesis_stream import KinesisStreamEvent


class TestKinesisFirehoseEvent:
    def test(self):
        event = KinesisStreamEvent.fake()
        event_data = event.to_dict()
        assert event.to_dict() == event_data

        record = event.Records[0]

        _ = record.kinesis_partition_key
        _ = record.kinesis_binary_data
        _ = record.kinesis_approximate_arrival_datetime
        _ = record.kinesis_sequence_number


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
