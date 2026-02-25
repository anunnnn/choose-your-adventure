import uuid
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.story import (
    CompleteStoryNodeResponse,
    CreateStoryRequest
)
from schemas.job import StoryJobResponse

router = APIRouter(
    prefix="/story",
    tags=["story"]
)

def get_session_id(session_id: Optional[str] = Cookie(None)):
    if session_id is None:
        session_id = str(uuid.uuid4())
    return session_id



@router.post("create", response_model=StoryJobResponse)
def create_story(
    request: CreateStoryRequest,
    background_tasks: BackgroundTasks,
    response: Response,
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db)
):
    response.set_cookie(keys="session_id", value=session_id, httponly=True, secure=True)

    # Create a new story job
    job_id = str(uuid.uuid4())
    job = StoryJob(
        job_id=job_id,
        session_id=session_id,
        status="pending",
        theme=request.theme,
        created_at=datetime.now()
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    # todo: Add background task to generate the story
    background_tasks.add_task(
        generate_story_task,
        job_id=job_id,
        theme=request.theme,
        session_id=session_id
    )

    return job


def generate_story_task(job_id: str, theme: str, session_id: str):

    db = SessionLocal()

    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()

        if not job:
            return
        
        try:
            job.status = "in_progress"
            db.commit()

            story = {} # todo: Generate the story based on the theme
            job.story_id = 1 # todo: update story id
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()

        except Exception as e:
            job.status = "failed"
            job.completed_at = datetime.now()
            job.error = str(e)
            db.commit()

    finally:
        db.close()