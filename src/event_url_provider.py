from typing import List, Dict


class EventUrlProvider:
    """
    I am the source of known event calendar urls
    """
    
    def get_urls(self) -> Dict[str, str]:
        """
        Return a map of evant name -> url
        """
        return {}
