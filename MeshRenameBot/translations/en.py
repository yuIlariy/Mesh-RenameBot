from dataclasses import dataclass
import random

@dataclass
class EnglishTranslations:
    LANGUAGE_NAME = "🇬🇧 English"
    LANGUAGE_CODE = "en"

    WRONG_VALUE_ERROR = "❌ Oopsie! Invalid value for {{ variable_name }}. Try again! 🤷‍♀️"

    START_MSG = (
    "✨ **Hey there, file wizard!** ✨\n\n"
    "I'm **Auto Rename Bot** 🪄, your magical file-renaming assistant!\n\n"
    "🔥 **Why you'll love me:**\n"
    "- Rename files with ✨ sparkle and precision\n"
    "- Blazing fast ⚡ and secure 🔒\n"
    "- Supports ALL the file types! 📂🎵🎬\n\n"
    "Just send me a file and let's make magic happen! 🎩\n\n"
    "🚀 **Pro Tip:** Use /mode for auto-rename ninja mode!\n"
    "Need help? /help has your back!\n\n"
    "🛸 **Powered by** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ Rename cancelled! Poof! ✨ (Updates coming soon!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **Whoops! No filter match!**\n\n"
        "Tried using filters but came up empty 🎩🐇\n"
        "Manage your filters with /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **Filter power activated!**\n"
        "Using filters since you didn't specify a name\n"
        "Tweak them with /filters ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **Name your masterpiece!**\n"
        "```/rename shiny_new_name.ext```\n"
        "or play with `/filters` 🎨"
    )

    RENAME_CANCEL = "❌ Nah, let's cancel this ✌️"

    RENAMING_FILE = "🌀 **File transformation in progress...**"

    DL_RENAMING_FILE = "📥 **Downloading your digital treasure...**"

    RENAME_ERRORED_REPORT = "💥 **Yikes! Something broke!** Please report this 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **You waved the cancel wand!** ✨"

    FLTR_ADD_LEFT_STR = "👈 **Added LEFT filter:** `{{ text_1 }}`"
    FLTR_ADD_RIGHT_STR = "👉 **Added RIGHT filter:** `{{ text_1 }}`"
    FLTR_RM_STR = "🗑 **Deleted filter:** `{{ text_1 }}`"
    FLTR_REPLACE_STR = "🔄 **Swapped:** `{{ text_1 }}` → `{{ text_2 }}`"

    CURRENT_FLTRS = "🎛️ **Your Filter Dashboard:**"
    ADD_FLTR = "➕ Add Magic"
    RM_FLTR = "🗑 Remove Magic"

    FILTERS_INTRO = (
        "📜 **Filter Grimoire:**\n"
        "Three spells at your disposal:\n\n"
        "🔄 **Transmute Spell:** Change words\n"
        "➕ **Conjure Spell:** Add words\n"
        "🗑 **Vanishing Spell:** Remove words"
    )

    ADD_REPLACE_FLTR = "🔄 Transmute Spell"
    ADD_ADDITION_FLTR = "➕ Conjure Spell"
    ADD_REMOVE_FLTR = "🗑 Vanishing Spell"
    BACK = "🔙 Back to Safety"

    REPALCE_FILTER_INIT_MSG = (
        "✍️ **Transmutation Formula:**\n"
        "`old_stuff | new_stuff`\n"
        "or `/ignore` to escape 🏃‍♂️"
    )

    NO_INPUT_FROM_USER = "🤷‍♂️ **Crickets...** No input detected!"
    INPUT_IGNORE = "👍 **Spell ignored!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **Whoops!** Wrong format! Try again!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **Transmutation Complete!**\n" 
        "`{{ text_1 }}` → `{{ text_2 }}`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✨ **Conjuring Text:**\n"
        "Wrap your magic in `|text|`\n"
        "or `/ignore` to bail 🏃‍♀️"
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "👈 **Left Conjuration:** `{{ text_1 }}`"
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "👉 **Right Conjuration:** `{{ text_1 }}`"
    )

    ADDITION_LEFT = "👈 Left Side"
    ADDITION_RIGHT = "👉 Right Side"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **Where shall I place the magic?**"

    REMOVE_FILTER_INIT_MSG = (
        "🗑 **Vanishing Act:**\n"
        "What shall disappear?\n"
        "or `/ignore` to keep it ✌️"
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **Poof!** `{{ text_1 }}` will vanish!"
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 Download complete! Preparing magic...",
        "📦 File acquired! Ready for naming sorcery...",
        "✨ Download successful! Incantations beginning...",
        "⚡ Data secured! Renaming engines firing up...",
        "💾 File captured! Preparing for glorious rebirth..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **Blast off!** Renamed file launched!",
        "🎉 **Ta-da!** Your newly named file is ready!",
        "📤 Upload complete! Enjoy your masterpiece!",
        "🌟 File metamorphosis complete!",
        "🏁 Race over! Your file has crossed the finish line!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **Abort!** Download spell interrupted!",
        "🚧 Whoops! You stopped the download train!",
        "🎭 The show's over before it began!",
        "📵 Download connection terminated!",
        "👋 You ghosted the download! Bye-bye!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **Hold up!** Upload stopped mid-flight!",
        "🚫 No delivery today! Upload cancelled!",
        "🌪️ Upload tornado dissipated!",
        "📴 Connection lost in the void!",
        "🤷‍♂️ You changed your mind! Upload aborted!"
    ]

    REPLY_TO_MEDIA = "📎 **Psst!** Reply `/rename` to a file!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **Kaboom!** Renaming spell failed!"

    DOWNLOADING_THE_FILE = "📥 **Fetching your file...**"
    UPLOADING_THE_FILE = "📤 **Launching:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **Rename Mission Initiated**\n"
        "🆔 Mission ID: `{{ uid }}`\n\n"
        "👤 **Agent:** @{{ username }}\n"
        "📛 **Codename:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n"
        "📜 **File:** `{{ file_name }}`\n\n"
        "`⚡ Hyperdrive engaged!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **Rename Mission Queued**\n\n"
        "👤 **Agent:** @{{ username }}\n"
        "📛 **Codename:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n\n"
        "`⏳ Awaiting deployment...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **Pro Tip:** Use `/setcaption` to add flair!\n"
        "✨ Insert `{file_name}` to auto-fill the filename!"
    )

    DELETE_CAPTION = "🗑️ Yeet Caption"
    CLOSE = "🚪 Exit"

    CAPTION_CURRENT = "📝 **Current Caption:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **Caption empty!** So lonely..."
    CAPTION_SET = "✅ **New Caption:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **Caption vanished!** Poof!"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **Rename in Queue**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "📦 **Media ID:** {{ media_id }}\n\n"
        "`⏳ Patience, young padawan...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **Queue Stats:**\n"
        "📊 **Total Tasks:** {{ total_tasks }}\n"
        "⚡ **Capacity:** {{ queue_capacity }}\n"
        "⏳ **Processing:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **Your file is being MAGIC'D!**\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **Your place in line:** {{ task_number }}\n"
        "🆔 **Task ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **You've been booted!** No bot for you!"
    USER_NOT_PARTICIPANT = (
        "🔒 **Secret Club Alert!**\n\n"
        "Join our channel to unlock the magic!\n\n"
        "`🦄 Unicorns only beyond this point`"
    )
    
    JOIN_CHANNEL = "🔗 Join Secret Club"

    MODE_INITIAL_MSG = (
        "🎛️ **Output Mode Selector:**\n\n"
        "1️⃣ **Keep original format**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **Force Document mode**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **General Media mode**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **Rename Style:**\n"
        "🅰️ **Command rename**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **Auto-rename**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ OG Mode"
    MODE_SET_1 = "2️⃣ Doc Mode"
    MODE_SET_2 = "3️⃣ Media Mode"
    COMMAND_MODE_SET_3 = "🅰️ Command"
    COMMAND_MODE_SET_4 = "🅱️ Auto"

    THUMB_REPLY_TO_MEDIA = "🖼️ **Reply to an image** to set as thumbnail"
    THUMB_SET_SUCCESS = "✅ **Thumbnail locked in!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **No thumbnail detected!**"
    THUMB_CLEARED = "🧹 **Thumbnail swept away!**"

    HELP_STR = (
        "📚 **Magic Spellbook:**\n"
        "`{{ startcmd }}` - Check if I'm alive! 💓\n"
        "`{{ renamecmd }}` - Rename files like a boss! 🎩\n"
        "`{{ filterscmd }}` - Customize your renaming magic! ✨\n"
        "`{{ setthumbcmd }}` - Set a permanent thumbnail! 🖼️\n"
        "`{{ getthumbcmd }}` - Peek at current thumbnail! 👀\n"
        "`{{ clrthumbcmd }}` - Bye-bye thumbnail! 🗑️\n"
        "`{{ modecmd }}` - Switch output modes:\n"
        "   - 📝 Original format\n"
        "   - 📂 Force document\n"
        "   - 🎥 Media mode\n\n"
        "   Switch rename styles:\n"
        "   - 🏷️ Command-based\n"
        "   - 🤖 Auto-rename\n\n"
        "`{{ queuecmd }}` - Check rename queue 📊\n"
        "`{{ setcaptioncmd }}` - Set fancy captions 🎨\n"
        "`{{ helpcmd }}` - This magic book! 📖\n"
        "`{{ pingcmd }}` - Ping-pong! 🏓\n"
        "`{{ infocmd }}` - Bot specs! 🤖\n"
        "`{{ profilecmd }}` - Your stats! 📈\n"
        "`{{ statuscmd }}` - Bot vitals! 💓\n"
        "`{{ statscmd }}` - Global numbers! 🌍\n"
        "`{{ broadcastcmd }}` - Mega-announce! 📢\n"
        "`{{ leaderboardcmd }}` - Top users! 🏆\n"
        "`{{ setlanguagecmd }}` - Change language! 🌐"
    )

    CURRENT_LOCALE = "🌍 **Your language:** {{ user_locale }}"

