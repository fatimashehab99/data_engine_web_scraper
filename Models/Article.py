from dataclasses import field, dataclass
from typing import List, Optional

@dataclass
class Article:
    url: str
    postId: Optional[str] = None
    type: Optional[str] = None
    title: Optional[str] = None
    thumbnail: Optional[str] = None
    video_duration: Optional[int] = None
    word_count: Optional[int] = None
    published_date: Optional[str] = None
    updated_date: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    category: Optional[str] = None
    country: Optional[str] = None
    post_type: Optional[str] = None
    classes: List[dict] = field(default_factory=list)
    keywords: List[str] = field(default_factory=list)





