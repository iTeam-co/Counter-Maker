import telebot
import sys
import redis
channel = '@channelid'
r = redis.Redis('localhost')
reload(sys)
sys.setdefaultencoding('utf8')
bot = telebot.TeleBot('175532355:AAEX7Lv1qoFPZfD8iauXS8m8VngQdcIdkMQ')
blocklist = r.smembers('blocklist')
def is_block(cid):
	return str(cid) in blocklist
@bot.message_handler(content_types=['text','sticker', 'photo', 'audio', 'video', 'contact', 'location', 'document', 'venue'])
def main(m):
  if is_block(m.from_user.id):
		pass
	else:
		_hash = "anti_flood:" + str(m.from_user.id)
		msgs = 0
		if r.get(_hash):
		 	msgs = int(r.get(_hash))
		max_msgs = 2
		max_time = 1
		if msgs > max_msgs:
		 	r.sadd('blocklist', str(m.from_user.id))
		 	bot.send_message(m.from_user.id, 'You have been blocked!\nBot will not respond to you.\n<b>Reason:</b> FLOOD',parse_mode='HTML')
		r.setex(_hash, max_time, int(msgs) + 1
    if m.text == '/start':
      r.sadd('cmaker:users', str(m.from_user.id))
      bot.send_message(m.chat.id, 'Welcome to @CmakerBot\nThis bot will add counter to your messages.\nDev: @prsahrn\n Powered By: @Iteam_en') #change this
    else:
      msg = bot.forward_message(channel, m.chat.id, m.message_id)
      bot.forward_message(m.chat.id, channel, msg.message_id)
bot.polling(none_stop=True)
