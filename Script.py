class script(object):
    START_TXT = """đđđĨđĨđ¨ {},
đđ˛ đđđĻđ đđŦ <a href=https://t.me/{}>{}</a>, đ đđđ§ đđĢđ¨đ¯đĸđđ đđ¨đ¯đĸđđŦ đ đđ¨đŽ đđđ§ đđđ đđ đđ§ đđ¨đŽđĢ đđĢđ¨đŽđŠs đ¤­"""
    HELP_TXT = """đˇđ´đ {}
đˇđ´đđ´ đ¸đ đđˇđ´ đˇđ´đģđŋ đĩđžđ đŧđ đ˛đžđŧđŧđ°đŊđŗđ."""
    ABOUT_TXT = """â¯ đŧđ đŊđ°đŧđ´: {}
â¯ đ˛đđ´đ°đđžđ: <a href=https://t.me/Technokillerbot>Techno Mindz</a>
â¯ đģđ¸đąđđ°đđ: đŋđđđžđļđđ°đŧ
â¯ đģđ°đŊđļđđ°đļđ´: đŋđđđˇđžđŊ đš
â¯ đŗđ°đđ° đąđ°đđ´: đŧđžđŊđļđž đŗđą
â¯ đąđžđ đđ´đđđ´đ: đˇđ´đđžđēđ
â¯ đąđđ¸đģđŗ đđđ°đđđ: v1.0.1 [ đąđ´đđ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Source - https://t.me/technomindzchat  

<b>DEVS:</b>
- <a href=https://t.me/technomindzchat>Devil Hacker</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Trisha will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Trisha should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĸ /filter - <code>add a filter in chat</code>
âĸ /filters - <code>list all the filters of a chat</code>
âĸ /del - <code>delete a specific filter in chat</code>
âĸ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Trisha Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Trisha supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/JaiHindChatting)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âĸ /connect  - <code>connect a particular chat to your PM</code>
âĸ /disconnect  - <code>disconnect from a chat</code>
âĸ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Trisha

<b>Commands and Usage:</b>
âĸ /id - <code>get id of a specifed user.</code>
âĸ /info  - <code>get information about a user.</code>
âĸ /imdb  - <code>get the film information from IMDb source.</code>
âĸ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĸ /logs - <code>to get the rescent errors</code>
âĸ /stats - <code>to get status of files in db.</code>
âĸ /delete - <code>to delete a specific file from db.</code>
âĸ /users - <code>to get list of my users and ids.</code>
âĸ /chats - <code>to get list of the my chats and ids </code>
âĸ /leave  - <code>to leave from a chat.</code>
âĸ /disable  -  <code>do disable a chat.</code>
âĸ /ban  - <code>to ban a user.</code>
âĸ /unban  - <code>to unban a user.</code>
âĸ /channel - <code>to get list of total connected channels</code>
âĸ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â đđžđđ°đģ đĩđ¸đģđ´đ: <code>{}</code>
â đđžđđ°đģ đđđ´đđ: <code>{}</code>
â đđžđđ°đģ đ˛đˇđ°đđ: <code>{}</code>
â đđđ´đŗ đđđžđđ°đļđ´: <code>{}</code> đŧđđą
â đĩđđ´đ´ đđđžđđ°đļđ´: <code>{}</code> đŧđđą"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
