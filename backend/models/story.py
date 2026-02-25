from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, JSON, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    session_id = Column(String, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    nodes = relationship("StoryNode", back_populates="story", cascade="all, delete-orphan")

class StoryNode(Base):
    __tablename__ = "story_nodes"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(String, ForeignKey("stories.id"))
    content = Column(String, nullable=False)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_winning = Column(Boolean, default=False)
    options = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    story = relationship("Story", back_populates="nodes")
