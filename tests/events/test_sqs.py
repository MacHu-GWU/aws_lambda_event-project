# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event.events.sqs import SQSEvent


class TestSQSEvent:
    def test(self):
        event = SQSEvent.fake()
        event_data = event.to_dict()
        assert event.to_dict() == event_data

        _ = event.Records[0]


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
