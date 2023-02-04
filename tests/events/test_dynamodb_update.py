# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.events.dynamodb_update import DynamodbUpdateEvent


class TestDynamodbUpdateEvent:
    def test(self):
        event1 = DynamodbUpdateEvent.fake(is_insert=True)
        event2 = DynamodbUpdateEvent.fake(is_update=True)
        event3 = DynamodbUpdateEvent.fake(is_delete=True)
        event1.Records.extend(event2.Records)
        event1.Records.extend(event3.Records)

        event = event1
        event_data = event.to_dict()
        assert event.to_dict() == event_data

        record = event.Records[1]

        _ = record.keys
        _ = record.old_image
        _ = record.new_image
        _ = record.approximate_creation_timestamp
        _ = record.approximate_creation_datetime

        assert event.Records[0].old_image == dict()
        assert event.Records[2].new_image == dict()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
