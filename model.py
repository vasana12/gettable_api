from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from enum import Enum
from typing import Literal, Optional, List, Union
from odmantic import AIOEngine, EmbeddedModel, Field, Model
import setting

client = AsyncIOMotorClient(setting.MONGODB_URL)
engine = AIOEngine(motor_client=client, database="gettable")

class ActorStatus(str, Enum):
    buildRequest = "buildRequest"
    buildRunning = "buildRunning"
    buildSucceeded = "buildSucceeded"
    buildFailed = "buildFailed"
    buildCancel = "buildCancel"
    runRequest = "executeRequest"
    runRunning = "executeRunning"
    runSucceeded = "runSucceeded"
    runFailed = "runFailed"
    runCancel = "runCancel"


class ActorRegisterPatchSchema(Model):
    client: Optional[str] = "admin"
    github_repository: str = Field(primary_field=False, regex="(?:https?://)?(?:www[.])?github[.]com/[\w-]+/?")

class Actor(Model):
    client: Optional[str] = "admin"
    github_repository: str = Field(primary_field=False, regex="(?:https?://)?(?:www[.])?github[.]com/[\w-]+/?")
    local_repository: Optional[str]
    created_at: Optional[datetime]
    status: Optional[ActorStatus]
    image_name: Optional[str]

class Task(Model):
    client: Optional[str] = "admin"
    input: Optional[List[dict]]
    image_name: Optional[str]
    cpu: Optional[int]
    memory: Optional[int]
    created_at: Optional[datetime]
    status: Optional[ActorStatus]
