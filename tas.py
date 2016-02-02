#!/usr/bin/env python3
import requests
from itertools import chain
from lxml.html import fromstring, HtmlElement
from lxml.cssselect import CSSSelector


def get_schedule_table():
    URL = 'http://horriblesubs.info/'
    response = requests.get(URL)
    document = create_html_document_from(response)
    table = search_for_nodes_by_css(document, '.schedule-table')
    return table[0]


def get_schedule_shows(table):
    shows = search_for_nodes_by_css(table, '.schedule-widget-show > a')
    return shows


def get_schedule_times(table):
    times = search_for_nodes_by_css(table, '.schedule-time')
    return times

 
def create_html_document_from(response):
    document = fromstring(response.text)
    return document


def search_for_nodes_by_css(document, selector):
    sel = CSSSelector(selector)
    return sel(document)


def make_schedule():
    table = get_schedule_table()
    shows = get_schedule_shows(table)
    times = get_schedule_times(table)
    return list(zip([show.text for show in shows],
                    [time.text for time in times]))
