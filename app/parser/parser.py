from instabot import Bot
import utils

utils.delete_config()

bot = Bot()

INST_USERNAME = 'user_name'
INST_PASSWORD = 'user_password'
username = 'searching_username'

bot.login(username=INST_USERNAME, password=INST_PASSWORD)

user_followers = bot.get_user_followers(username)
user_following = bot.get_user_following(username)
user_info = bot.get_user_info(username)

print(len(user_following))
print(len(user_followers))
print(user_info)
