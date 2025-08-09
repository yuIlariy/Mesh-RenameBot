from dataclasses import dataclass
import random

@dataclass
class ChineseTranslations:
    LANGUAGE_NAME = "中文"
    LANGUAGE_CODE = "zh"

    WRONG_VALUE_ERROR = "❌ 变量 {{ variable_name }} 输入了无效值。"

    START_MSG = (
    "你好！👋\n"
    "我是**自动重命名机器人**，您Telegram上轻松重命名文件的得力助手。\n\n"
    "✨ **主要功能:**\n"
    "- 使用自定义名称和扩展名重命名文件\n"
    "- 快速、安全且易于使用\n"
    "- 支持多种文件类型\n\n"
    "只需发送文件给我，我将指导您完成重命名过程！\n\n"
    "让我们开始吧！使用 /mode 启用自动重命名，**无需命令重命名**🚀\n"
    "发送 /help 了解更多信息。\n\n"
    "🚀 **由** [NAm](https://t.me/xspes) **提供支持**"
    )

    CANCEL_MESSAGE = "⚠️ 重命名已被**取消**。即将更新。"

    RENAME_NO_FILTER_MATCH = (
        "🚫 **无匹配过滤器 - 中止重命名**\n\n"
        "🔍 由于未指定名称，使用过滤器进行重命名。\n"
        "👻 使用 /filters 管理您的过滤器。"
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ 由于未指定名称，使用过滤器进行重命名。\n"
        "👻 使用 /filters 管理您的过滤器。"
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ 按以下格式输入新文件名：\n"
        "```/rename 新文件名.扩展名```\n"
        "或使用 `/filters` 设置重命名过滤器。"
    )

    RENAME_CANCEL = "❌ 取消此次重命名"

    RENAMING_FILE = "🔄 正在重命名文件...请稍候。"

    DL_RENAMING_FILE = "📥 正在下载文件...请稍候。"

    RENAME_ERRORED_REPORT = "❗ 下载过程中出错。请报告此问题。"

    RENAME_CANCEL_BY_USER = "🚫 **用户已取消**"

    FLTR_ADD_LEFT_STR = "➕ 添加过滤器：`<code>{{ text_1 }}</code>` **到左侧**。"
    FLTR_ADD_RIGHT_STR = (
        "➕ 添加过滤器：`<code>{{ text_1 }}</code>` **到右侧**。"
    )
    FLTR_RM_STR = "❌ 移除过滤器：`<code>{{ text_1 }}</code>`。"
    FLTR_REPLACE_STR = (
        "🔄 替换过滤器：`<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`。"
    )

    CURRENT_FLTRS = "⚙️ **您当前的过滤器：**"
    ADD_FLTR = "➕ 添加过滤器"
    RM_FLTR = "❌ 移除过滤器"

    FILTERS_INTRO = (
        "🛠 **过滤器指南：**\n"
        "共有3种过滤器类型：\n\n"
        "🔄 **替换过滤器：** 用一个词替换另一个词\n"
        "➕ **添加过滤器：** 在开头或结尾添加词语\n"
        "❌ **移除过滤器：** 从文件名中删除词语"
    )

    ADD_REPLACE_FLTR = "➕ 添加替换过滤器"
    ADD_ADDITION_FLTR = "➕ 添加附加过滤器"
    ADD_REMOVE_FLTR = "➕ 添加移除过滤器"
    BACK = "🔙 返回"

    REPALCE_FILTER_INIT_MSG = "✍️ 发送格式：`<code>要替换的内容 | 替换为</code>` 或 `/ignore` 返回。"

    NO_INPUT_FROM_USER = "⚠️ 未收到您的输入。"
    INPUT_IGNORE = "✅ **已忽略**"
    WRONG_INPUT_FORMAT = "❌ 格式无效。请检查提供的格式。"
    REPLACE_FILTER_SUCCESS = (
        "✅ **替换过滤器已添加：**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ 在 `<code>|</code>` 之间输入要添加的文本\n"
        "示例：`<code>| 要添加的文本 |</code>`\n"
        "或 `/ignore` 返回。"
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ 过滤器已添加：`<code>{{ text_1 }}</code>` **到左侧**"
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ 过滤器已添加：`<code>{{ text_1 }}</code>` **到右侧**"
    )

    ADDITION_LEFT = "🔄 添加到左侧"
    ADDITION_RIGHT = "🔄 添加到右侧"

    ADDITION_POSITION_PROMPT = "📍 **您想将文本添加到哪里？**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ 输入您要删除的文本或 `/ignore` 返回。"
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **移除过滤器已添加：** `<code>{{ text_1 }}</code>` 将被移除。"
    )

    RENAME_THEMES_DOWNLOADING = [
        "✅ 下载完成。正在启动重命名魔法...",
        "📦 文件已获取！准备赋予新名称...",
        "🪄 下载完成。✨ 开始重命名仪式...",
        "🔧 数据已获取。重命名引擎启动中...",
        "💾 已保存并密封。现在以风格重命名...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ 全部重命名完成！上传完毕。",
        "🚀 文件成功更名并发布。",
        "📤 上传完成。您重命名的杰作已上线！",
        "🌟 文件重命名完成。已送达宇宙！",
        "📁 任务完成。文件以新名称上传。",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 下载中止。重命名梦想破灭...",
        "🚫 您拔掉了插头。下载已中止。",
        "❌ 操作中途取消。未获取文件。",
        "📴 下载期间重命名取消。任务终止。",
        "👋 用户中途退出下载。再见，文件。",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 上传取消。文件保留在本地且无人问津。",
        "🚫 重命名撤销。上传终止。",
        "❌ 最后阶段中断。重命名放弃。",
        "📴 上传被否决。重命名文件无处可去。",
        "👋 用户在上传期间说'不'。文件退役。",
    ]

    REPLY_TO_MEDIA = "📂 回复媒体文件 `/rename`。"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ 重命名过程中出错。"

    DOWNLOADING_THE_FILE = "📥 正在下载文件"
    UPLOADING_THE_FILE = "📤 正在上传文件：**{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **重命名任务执行开始**\n"
        "🆔 任务ID：`{{ uid }}`\n\n"
        "👤 **用户名：** @{{ username }}\n"
        "📛 **名称：** {{ name }}\n"
        "🆔 **用户ID：** `<code>{{ user_id }}</code>`\n"
        "📂 **文件名：** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **重命名任务已添加**\n\n"
        "👤 **用户名：** @{{ username }}\n"
        "📛 **名称：** {{ name }}\n"
        "🆔 **用户ID：** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **注意：** 您可以使用 `/setcaption` 后跟所需文本来设置标题。\n"
        "📂 使用 `<code>{file_name}</code>` 在标题中动态插入重命名的文件名。"
    )

    DELETE_CAPTION = "🗑 删除标题"
    CLOSE = "❌ 关闭"

    CAPTION_CURRENT = "📝 **您当前的标题：** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **未设置标题**"
    CAPTION_SET = "✅ **标题已更新为：** {{ caption }}"
    CAPTION_DELETED = "🗑 **标题已成功删除**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **重命名任务已添加到队列**\n"
        "🆔 **DC ID：** {{ dc_id }}\n"
        "👻 **媒体ID：** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **重命名队列状态：**\n"
        "☄️ **队列中的总任务：** {{ total_tasks }}\n"
        "⚡ **队列容量：** {{ queue_capacity }}\n"
        "⏳ **当前正在处理：** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **您的任务当前正在执行**\n"
        "🆔 **任务ID：** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **您的任务在队列中的位置：** {{ task_number }}\n"
        "🆔 **任务ID：** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **您已被移出聊天。无法使用此机器人。**"
    USER_NOT_PARTICIPANT = "👻 **请加入所需聊天以使用此机器人。**"
    JOIN_CHANNEL = "🔗 加入更新频道"

    MODE_INITIAL_MSG = (
        "📂 **文件输出模式：**\n\n"
        "1️⃣ **与发送格式相同**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **强制为文档**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **作为通用媒体上传**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **选择重命名模式：**\n"
        "🅰️ **使用命令重命名**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **无需命令重命名**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 回复图片将其设置为缩略图。"
    THUMB_SET_SUCCESS = "✅ **缩略图设置成功**"
    THUMB_NOT_FOUND = "⚠️ **未找到缩略图**"
    THUMB_CLEARED = "🗑 **缩略图已清除**"

    HELP_STR = (
        "📖 **机器人命令：**\n"
        "`{{ startcmd }}` - ✅ 检查机器人是否运行\n"
        "`{{ renamecmd }}` - ✍️ 回复媒体文件 `/rename 文件名.扩展名` 进行重命名\n"
        "`{{ filterscmd }}` - ⚙️ 管理重命名过滤器\n"
        "`{{ setthumbcmd }}` - 📷 设置永久缩略图(回复图片)\n"
        "`{{ getthumbcmd }}` - 📸 获取当前设置的缩略图\n"
        "`{{ clrthumbcmd }}` - ❌ 移除设置的缩略图\n"
        "`{{ modecmd }}` - 🔄 在3种输出模式间切换：\n"
        "    - 📝 与发送格式相同\n"
        "    - 📂 强制为文档\n"
        "    - 🎥 通用媒体(可流式视频/音频)\n\n"
        "    🔄 在重命名模式间切换：\n"
        "    - 🏷 **使用命令重命名**\n"
        "    - ✨ **无需命令/自动重命名**\n\n"
        "`{{ queuecmd }}` - 📊 查看机器人重命名队列状态\n"
        "`{{ setcaptioncmd }}` - 📝 为重命名文件设置标题\n"
        "`{{ helpcmd }}` - 📖 显示此帮助信息\n"
        "`{{ pingcmd }}` - 🎈Ping机器人\n"
        "`{{ infocmd }}` - 🧑‍💻 查看机器人信息\n"
        "`{{ profilecmd }}` - ☄️ 您的使用统计\n"
        "`{{ statuscmd }}` - 🗿 机器人状态\n"
        "`{{ statscmd }}` - 👻 全局机器人统计\n"
        "`{{ broadcastcmd }}` - ☄️进行广播\n"
        "`{{ leaderboardcmd }}` - 👻 用户排行榜\n"
        "`{{ setlanguagecmd }}` - 🌐 更改机器人语言"
    )

    CURRENT_LOCALE = "🌐 **您的当前语言：** {{ user_locale }}"





