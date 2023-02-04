# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.events.sns import SNSTopicNotificationEvent


class TestSNSTopicNotificationEvent:
    def test(self):
        event = SNSTopicNotificationEvent.fake()
        event_data = event.to_dict()
        assert event.to_dict() == event_data

        record = event.Records[0]

        _ = record.message
        _ = record.subject
        _ = record.notification_time


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
