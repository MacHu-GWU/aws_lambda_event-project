# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.events.cloudwatch_scheduled_event import CloudWatchScheduledEvent


class TestCloudWatchScheduledEvent:
    def test(self):
        event = CloudWatchScheduledEvent.fake()
        event_data = event.to_dict()
        assert event.to_dict() == event_data


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
