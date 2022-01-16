# -*- coding: utf-8 -*-

import pytest
from aws_lambda_event import helpers


def test_datetime_from_timestamp():
    dt = helpers.datetime_from_timestamp(1640995200)
    assert str(dt).startswith("2022-01-01 00:00:00")

    dt = helpers.datetime_from_timestamp(1640995200000)
    assert str(dt).startswith("2022-01-01 00:00:00")

    with pytest.raises(ValueError):
        helpers.datetime_from_timestamp(1000)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
