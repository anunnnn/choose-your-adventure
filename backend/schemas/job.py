from typing import Optional
from datetime import datetime
from models.story import Story
from pydantic import BaseModel

class StoryJobBase(BaseModel):
    """Base schema for a story job."""
    theme: str

class StoryJobResponse(BaseModel):
    """Schema for a complete story job response."""
    job_id: str
    status: str
    created_at: datetime
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config:
        from_attributes = True

class StoryJobCreate(Story):
    pass
