from telethon import TelegramClient
import logging
import time
openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6259911760:AAHN8Qm26EM7hIMe148XYtX7X5nJ1BpwjKY"

bot = TelegramClient("daya_drasti_bot",api_id, api_hash).start(bot_token = bot_token)