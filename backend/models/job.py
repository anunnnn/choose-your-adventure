from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, nullable=False, unique=True, index=True)
    session_id = Column(String, nullable=False, index=True)
    theme = Column(String, nullable=False)
    status = Column(String, nullable=False, default="pending")
    story_id = Column(Integer, ForeignKey("stories.id"), nullable=False)
    error = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

