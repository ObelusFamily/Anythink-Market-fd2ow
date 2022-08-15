"""
- Two ways to do it!
1. Use Backend Python API to insert data but check for authorization headers.
2. Use custom API libs for faster insertion. | Building this!

"""

import os
import sys
import asyncio
import asyncpg

sys.path.insert(0,os.getcwd())

# Pre-built Libraries
from app.core.config import get_app_settings
from app.api.dependencies.database import get_repository
from app.db.repositories.users import UsersRepository
from app.db.repositories.items import ItemsRepository
from app.db.repositories.comments import CommentsRepository

seedQuantity = 100  # Mock Data Quantity


async def dataSeeding(seedQuantity):
    DATABASE_URL = get_app_settings().database_url.replace(
        "postgres://", "postgresql://"
    )
    connection = await asyncpg.connect(DATABASE_URL)
    userRepo, itemRepo, commentRepo = (
        UsersRepository(conn=connection),
        ItemsRepository(conn=connection),
        CommentsRepository(conn=connection),
    )
    for mockValue in range(1, seedQuantity + 1):
        currentUser = await userRepo.create_user(
            email=f"user-{mockValue}@email{mockValue}.com",
            username=f"user{mockValue}",
            password=f"password{mockValue}",
        )
        currentItem = await itemRepo.create_item(
            slug=f"item{mockValue}",
            title=f"title{mockValue}",
            description=f"This is a description for item{mockValue}.",
            seller=currentUser,
        )
        currentComment = await commentRepo.create_comment_for_item(
            body=f"This is a comment{mockValue}.", item=currentItem, user=currentUser
        )
    await connection.close()


asyncio.get_event_loop().run_until_complete(dataSeeding(seedQuantity))
