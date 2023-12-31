import json
from urllib.request import Request, urlopen
import os

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def post_discord(message: str, webhook_url: str = DISCORD_WEBHOOK_URL):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
    }
    data = {"content": message}
    request = Request(
        webhook_url,
        data=json.dumps(data).encode(),
        headers=headers,
    )

    with urlopen(request) as res:
        assert res.getcode() == 204