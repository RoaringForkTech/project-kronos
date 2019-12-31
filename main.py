#!/usr/bin/env python3
"""
I am the main entry point to this program
"""
from typing import Dict, Any

from requests import Response
from dotenv import load_dotenv

from src.calendar_provider import CalendarProvider
from src.event_enricher import EventEnricher
from src.event_parser import EventParser
from src.event_pusher import EventPusher
from src.event_url_provider import EventUrlProvider
from src.providers import EventbriteEventProvider, GoogleProvider

# Pull in environment variables from dotenv file
load_dotenv()


def main() -> None:
    """
    I am an orchestrator for all other functionality
    """

    # 1. Gather known event urls
    url_provider = EventUrlProvider()
    raw_events: Dict[str, Any] = {}
    cal_fetcher: CalendarProvider = CalendarProvider()
    for name, url in url_provider.get_urls().items():
        raw_events[name] = cal_fetcher.find_events(name, url)

    # Just to see what's happening
    print("All events --> ", raw_events)


if __name__ == "__main__":
    # These lines execute only when this file is called from the command line
    main()
