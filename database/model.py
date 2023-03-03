from dataclasses import dataclass
from typing import Optional


@dataclass
class SiteInformation:
    username: str
    website: str
    password: str
    description: Optional[str]
    active: bool = True


