from freezegun import freeze_time
from pendulum import datetime

from core import applicable_timezones

timezones_test_cases = [
    'America/New_York',
    'America/Toronto',
    'Asia/Colombo',
    'Australia/Darwin',
    'Australia/Lord_Howe',
    'Australia/Sydney',
    'Canada/Saskatchewan'
]


def utc_now_standard_mode_for(hour, minute=0):
    return datetime(2012, 1, 1, hour=hour, minute=minute)


def utc_now_day_light_mode_for(hour, minute=0):
    return datetime(2012, 9, 1, hour=hour, minute=minute)


def test_applicable_timezones():
    expected_timezones = {
        'America/New_York',
        'America/Toronto',
    }

    with freeze_time(utc_now_standard_mode_for(hour=8)):
        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)

    with freeze_time(utc_now_day_light_mode_for(hour=7)):
        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)


def test_applicable_timezones_with_dst():
    expected_timezones = {
        'Canada/Saskatchewan'
    }

    with freeze_time(utc_now_standard_mode_for(hour=9)):
        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)

    with freeze_time(utc_now_day_light_mode_for(hour=9)):
        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)


def test_applicable_timezones_30mins_offset():
    expected_timezones = {
        'Asia/Colombo',
    }

    with freeze_time(utc_now_standard_mode_for(hour=21, minute=30)):
        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)

    with freeze_time(utc_now_day_light_mode_for(hour=21, minute=30)):
        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)


def test_applicable_timezones_30mins_dst_offset():
    with freeze_time(utc_now_standard_mode_for(hour=16)):
        expected_timezones = {
            'Australia/Lord_Howe',
            'Australia/Sydney',
        }

        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)

    with freeze_time(utc_now_day_light_mode_for(hour=16, minute=30)):
        expected_timezones = {
            'Australia/Lord_Howe',
        }

        actual_timezones = applicable_timezones(timezones=timezones_test_cases)
        assert expected_timezones == set(actual_timezones)
