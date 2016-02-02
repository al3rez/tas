from lxml.html import HtmlElement
from assertpy import assert_that
from tas import (make_schedule,
		 get_schedule_table,
		 get_schedule_shows,
		 get_schedule_times,
		 search_for_nodes_by_css)


table = get_schedule_table()


def test_that_table_is_an_html_element():
    assert_that(table).is_type_of(HtmlElement)


def test_that_shows_is_not_empty():
    shows = get_schedule_shows(table)
    assert_that(shows).is_not_empty()
    

def test_that_times_is_not_empty():
    times = get_schedule_times(table)
    assert_that(times).is_not_empty()


def test_that_css_match_is_not_empty():
    match = search_for_nodes_by_css(table, 'tr')
    assert_that(match).is_not_empty()


def test_that_schedule_is_not_empty():
    schedule = make_schedule()
    assert_that(schedule).is_not_empty()
