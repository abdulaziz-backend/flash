
import pytest
from aiogram.types import Message
from handlers.user import cmd_start

@pytest.mark.asyncio
async def test_cmd_start():
    message = Message(text="/start")
    result = await cmd_start(message)
    assert "Welcome" in result.text
