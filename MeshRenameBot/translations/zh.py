from dataclasses import dataclass
import random

@dataclass
class ChineseTranslations:
    LANGUAGE_NAME = "🇨🇳 中文"
    LANGUAGE_CODE = "zh"

    WRONG_VALUE_ERROR = "❌ 哎呀！{{ variable_name }}的值无效。请重试！🤷‍♀️"

    START_MSG = (
    "✨ **你好，文件魔法师！** ✨\n\n"
    "我是**自动重命名机器人** 🪄，你的神奇文件重命名助手！\n\n"
    "🔥 **你会喜欢我的原因：**\n"
    "- 用✨闪光和精确度重命名文件\n"
    "- 极速⚡且安全🔒\n"
    "- 支持所有文件类型！📂🎵🎬\n\n"
    "只需发送文件给我，让我们施展魔法吧！🎩\n\n"
    "🚀 **专业提示：** 使用/mode开启自动重命名忍者模式（必须添加/filters）！\n"
    "需要帮助？/help为你提供支持！\n\n"
    "🛸 **由** [NAm](https://t.me/xspes) **提供支持**"
    )

    CANCEL_MESSAGE = "❗ 重命名已取消！噗！✨（即将更新！）"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **哎呀！没有匹配的过滤器！**\n\n"
        "尝试使用过滤器但一无所获 🎩🐇\n"
        "使用/filters管理你的过滤器 ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **过滤器力量已激活！**\n"
        "由于您未指定名称，使用过滤器\n"
        "使用/filters调整它们 ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **未找到过滤器！**\n\n"
        "请添加/filters 🎨 用于自动选择重命名过滤器。"
    )

    RENAME_CANCEL = "❌ 不，取消这个吧 ✌️"

    RENAMING_FILE = "🌀 **文件转换进行中...**"

    DL_RENAMING_FILE = "📥 **正在下载您的数字宝藏...**"

    RENAME_ERRORED_REPORT = "💥 **哎呀！出问题了！** 请报告此问题 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **你挥动了取消魔杖！** ✨"

    FLTR_ADD_LEFT_STR = "➕ 添加过滤器：`<code>{{ text_1 }}</code>` **到左侧**。"
    FLTR_ADD_RIGHT_STR = (
        "➕ 添加过滤器：`<code>{{ text_1 }}</code>` **到右侧**。"
    )
    FLTR_RM_STR = "❌ 移除过滤器：`<code>{{ text_1 }}</code>`。"
    FLTR_REPLACE_STR = (
        "🔄 替换过滤器：`<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`。"
    )

    CURRENT_FLTRS = "🎛️ **您的过滤器仪表板：**"
    ADD_FLTR = "➕ 添加过滤器"
    RM_FLTR = "❌ 移除过滤器"

    FILTERS_INTRO = (
        "🛠 **过滤器指南：**\n"
        "有三种类型的过滤器：\n\n"
        "🔄 **替换过滤器：** 将一个词替换为另一个词。\n"
        "➕ **添加过滤器：** 在开头或结尾添加一个词。\n"
        "❌ **移除过滤器：** 从文件名中移除一个词。"
    )

    ADD_REPLACE_FLTR = "➕ 添加替换过滤器"
    ADD_ADDITION_FLTR = "➕ 添加添加过滤器"
    ADD_REMOVE_FLTR = "➕ 添加移除过滤器"
    BACK = "🔙 返回"

    REPALCE_FILTER_INIT_MSG = "✍️ 发送格式：`<code>要替换的内容 | 替换内容</code>` 或 /ignore 返回。"

    NO_INPUT_FROM_USER = "🤷‍♂️ **寂静...** 未检测到输入！"
    INPUT_IGNORE = "👍 **已忽略！**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **哎呀！** 格式错误！检查提供的格式并重试！"
    REPLACE_FILTER_SUCCESS = (
        "✅ **替换过滤器已添加：**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ 在 `<code>|</code>` 内输入要添加的文本\n"
        "示例：`<code>| 要添加的文本 |</code>`\n"
        "或 /ignore 返回。"
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ 过滤器已添加：`<code>{{ text_1 }}</code>` **到左侧**。"
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ 过滤器已添加：`<code>{{ text_1 }}</code>` **到右侧**。"
    )

    ADDITION_LEFT = "🔄 添加到左侧"
    ADDITION_RIGHT = "🔄 添加到右侧"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **您想在哪里添加文本？**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ 输入您要删除的文本或 /ignore 返回。"
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **移除过滤器已添加：** `<code>{{ text_1 }}</code>` 将被移除。"
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 下载完成！准备魔法...",
        "📦 文件已获取！准备命名魔法...",
        "✨ 下载成功！咒语开始...",
        "⚡ 数据已保护！重命名引擎启动中...",
        "💾 文件已捕获！准备光荣重生..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **发射！** 重命名文件已启动！",
        "🎉 **嗒-哒！** 您的新命名文件已准备就绪！",
        "📤 上传完成！享受您的杰作！",
        "🌟 文件变形完成！",
        "🏁 比赛结束！您的文件已越过终点线！"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **中止！** 下载咒语中断！",
        "🚧 哎呀！您停止了下载列车！",
        "🎭 演出在开始前就结束了！",
        "📵 下载连接终止！",
        "👋 您离开了下载！再见！"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **等等！** 上传在飞行中停止！",
        "🚫 今天没有交付！上传已取消！",
        "🌪️ 上传龙卷风消散！",
        "📴 连接在虚空中丢失！",
        "🤷‍♂️ 您改变了主意！上传中止！"
    ]

    REPLY_TO_MEDIA = "📎 **嘘！** 回复文件 `/rename`！"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **轰！** 重命名咒语失败！"

    DOWNLOADING_THE_FILE = "📥 **获取您的文件...**"
    UPLOADING_THE_FILE = "📤 **正在启动：** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **重命名任务已启动**\n"
        "🆔 任务ID：`{{ uid }}`\n\n"
        "👤 **代理：** @{{ username }}\n"
        "📛 **代号：** {{ name }}\n"
        "🪪 **ID：** `{{ user_id }}`\n"
        "📜 **文件：** `{{ file_name }}`\n\n"
        "`⚡ 超光速引擎已启动！`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **重命名任务已加入队列**\n\n"
        "👤 **代理：** @{{ username }}\n"
        "📛 **代号：** {{ name }}\n"
        "🪪 **ID：** `{{ user_id }}`\n\n"
        "`⏳ 等待部署...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **专业提示：** 使用/setcaption添加风格！\n"
        "✨ 使用 `/setcaption {file_name}` 自动在标题中填充文件名！"
    )

    DELETE_CAPTION = "🗑️ 删除标题"
    CLOSE = "🚪 退出"

    CAPTION_CURRENT = "📝 **当前标题：** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **标题为空！** 如此孤独..."
    CAPTION_SET = "✅ **新标题：** {{ caption }}"
    CAPTION_DELETED = "🗑️ **标题已成功删除。**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **重命名排队中**\n"
        "🆔 **DC ID：** {{ dc_id }}\n"
        "📦 **媒体ID：** {{ media_id }}\n\n"
        "`⏳ 耐心点，年轻的学徒...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **队列状态：**\n"
        "📊 **总任务数：** {{ total_tasks }}\n"
        "⚡ **容量：** {{ queue_capacity }}\n"
        "⏳ **处理中：** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **您的文件正在被魔法处理！**\n"
        "🆔 **任务ID：** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **您在队列中的位置：** {{ task_number }}\n"
        "🆔 **任务ID：** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **您已被踢出！** 没有机器人给您！"
    USER_NOT_PARTICIPANT = (
        "🔒 **秘密俱乐部警报！**\n\n"
        "加入我们的频道解锁魔法！\n\n"
        "`🦄 此点之后仅限独角兽`"
    )
    
    JOIN_CHANNEL = "🔗 加入秘密俱乐部"

    MODE_INITIAL_MSG = (
        "🎛️ **输出模式选择器：**\n\n"
        "1️⃣ **保持原始格式**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **强制文档模式**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **通用媒体模式**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **重命名风格：**\n"
        "🅰️ **命令重命名**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **自动重命名**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ OG模式"
    MODE_SET_1 = "2️⃣ 文档模式"
    MODE_SET_2 = "3️⃣ 媒体模式"
    COMMAND_MODE_SET_3 = "🅰️ 命令"
    COMMAND_MODE_SET_4 = "🅱️ 自动"

    THUMB_REPLY_TO_MEDIA = "🖼️ **回复图片** 设置为缩略图"
    THUMB_SET_SUCCESS = "✅ **缩略图已锁定！**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **未检测到缩略图！**"
    THUMB_CLEARED = "🧹 **缩略图已清除！**"

    HELP_STR = (
        "📚 **魔法咒语书：**\n"
        "`{{ startcmd }}` - 检查我是否活着！💓\n"
        "`{{ renamecmd }}` - 像老板一样重命名文件！🎩\n"
        "`{{ filterscmd }}` - 自定义您的重命名过滤器！✨\n"
        "`{{ setthumbcmd }}` - 设置永久缩略图！🖼️\n"
        "`{{ getthumbcmd }}` - 查看当前缩略图！👀\n"
        "`{{ clrthumbcmd }}` - 删除缩略图！🗑️\n"
        "`{{ modecmd }}` - 切换输出模式：\n"
        "   - 📝 原始格式\n"
        "   - 📂 强制文档\n"
        "   - 🎥 媒体模式\n\n"
        "   切换重命名风格：\n"
        "   - 🏷️ 基于命令\n"
        "   - 🤖 自动重命名（必须添加/filters）\n\n"
        "`{{ queuecmd }}` - 检查重命名队列 📊\n"
        "`{{ setcaptioncmd }}` - 设置花式标题 🎨\n"
        "`{{ helpcmd }}` - 这本魔法书！📖\n"
        "`{{ pingcmd }}` - 乒乓！🏓\n"
        "`{{ infocmd }}` - 机器人规格！🤖\n"
        "`{{ profilecmd }}` - 您的统计数据！📈\n"
        "`{{ statuscmd }}` - 机器人生命体征！💓\n"
        "`{{ statscmd }}` - 全球数字！🌍\n"
        "`{{ broadcastcmd }}` - 超级公告！📢\n"
        "`{{ leaderboardcmd }}` - 顶级用户！🏆\n"
        "`{{ setlanguagecmd }}` - 更改语言！🌐"
    )

    CURRENT_LOCALE = "🌍 **您的语言：** {{ user_locale }}"
