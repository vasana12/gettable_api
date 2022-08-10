import config
from model import *
from typing import Dict
from fastapi import FastAPI, status, Request, Body, HTTPException
from datetime import datetime

app = FastAPI(title=config.APP_TITLE, description=config.APP_DESCRIPTION, version=config.APP_VERSION)

@app.post("/actor", status_code=status.HTTP_201_CREATED,response_model=Actor)
async def build_actor(patch: ActorRegisterPatchSchema = Body(example={"github_repository": "https://github.com/dtcast/gettable_client"})):

    # ##github 주소로 중복 액터 체크
    # query_filter = {"github_link": patch.github_link}
    # actor = await engine.find_one(Actor, query_filter)
    # if actor is not None:
    #     raise HTTPException(400, detail=f"{actor.github_link}는 이미 존재하는 액터 입니다.")

    insert_field = {
        "status": ActorStatus.buildRequest,
        "created_at": datetime.now().replace(microsecond=0),
        "local_repository": patch.github_repository.replace("https://github.com/", "").replace("/", "-")
    }
    actor = await engine.save(Actor(**insert_field, **patch.dict()))
    return actor

@app.post("/actor", status_code=status.HTTP_201_CREATED,response_model=Actor)
async def create_task(patch: ActorRegisterPatchSchema = Body(example={"github_repository": "https://github.com/dtcast/gettable_client"})):

    # ##github 주소로 중복 액터 체크
    # query_filter = {"github_link": patch.github_link}
    # actor = await engine.find_one(Actor, query_filter)
    # if actor is not None:
    #     raise HTTPException(400, detail=f"{actor.github_link}는 이미 존재하는 액터 입니다.")

    insert_field = {
        "status": ActorStatus.buildRequest,
        "created_at": datetime.now().replace(microsecond=0),
        "local_repository": patch.github_repository.replace("https://github.com/", "").replace("/", "-")
    }
    actor = await engine.save(Actor(**insert_field, **patch.dict()))
    return actor



