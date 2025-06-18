from dataclasses import asdict

import pytest
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.models import User


@pytest.mark.asyncio
async def test_create_user(session: AsyncSession, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='test', email='teste@test', password='secret')

        session.add(new_user)
        await session.commit()

    user = await session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time,
        'updated_at': time,
        'todos': [],
    }


# TESTE DANDO ERRO APOS MUDANÇA DE DB PARA POSTGRES

# @pytest.mark.asyncio
# async def test_create_todo_error(session, user: User):
#     todo = Todo(
#         title='Test Todo',
#         description='Test Desc',
#         state='test',
#         user_id=user.id,
#     )

#     session.add(todo)
#     await session.commit()

#     with pytest.raises(LookupError):
#         await session.scalar(select(Todo))
