from instabot import Bot
import utils

utils.delete_config()

bot = Bot()

INST_USERNAME = 'your_username'
INST_PASSWORD = 'your_password'


bot.login(username=INST_USERNAME, password=INST_PASSWORD)


def get_info(username):
    return bot.get_user_info(username)
