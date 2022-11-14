import os, logging

from slack_logger import SlackHandler, SlackFormatter
from dotenv import load_dotenv

load_dotenv(verbose=True)
def __get_env(key: str) -> str:
    return os.getenv(key)

sh = SlackHandler(__get_env('SLACK_WEBHOOK_URL'))
sh.setFormatter(SlackFormatter())
logging.basicConfig(handlers=[sh])
logging.warning('Hello Slack')
