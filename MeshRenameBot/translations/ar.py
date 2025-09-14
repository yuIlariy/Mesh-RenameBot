from dataclasses import dataclass
import random

@dataclass
class ArabicTranslations:
    LANGUAGE_NAME = "🇸🇦 العربية"
    LANGUAGE_CODE = "ar"

    WRONG_VALUE_ERROR = "❌ عذرًا! قيمة غير صالحة لـ {{ variable_name }}. حاول مرة أخرى! 🤷‍♀️"

    START_MSG = (
    "✨ **مرحبًا أيها الساحر!** ✨\n\n"
    "أنا **بوت إعادة تسمية تلقائي** 🪄، مساعدك السحري لإعادة تسمية الملفات!\n\n"
    "🔥 **لماذا ستحبني:**\n"
    "- أسمي الملفات ب ✨ برعة ودقة\n"
    "- سريع جدًا ⚡ وآمن 🔒\n"
    "- يدعم جميع أنواع الملفات! 📂🎵🎬\n\n"
    "ما عليك سوى إرسال ملف لي ودعنا نصنع السحر! 🎩\n\n"
    "🚀 **نصيحة محترف:** استخدم /mode لوضع التسمية التلقاقة المتقدمة (يجب إضافة /filters)!\n"
    "تريد المساعدة؟ /help موجود لمساعدتك!\n\n"
    "🛸 **مدعوم بواسطة** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ تم إلغاء إعادة التسمية! بوف! ✨ (تحديثات قريبًا!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **عذرًا! لا يوجد تطابق للفلاتر!**\n\n"
        "حاولت استخدام الفلاتر ولكن لم أجد شيئًا 🎩🐇\n"
        "يمكنك إدارة الفلاتر الخاصة بك باستخدام /filters ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **تم تفعيل قوة الفلاتر!**\n"
        "أستخدم الفلاتر لأنك لم تحدد اسمًا\n"
        "يمكنك تعديلها باستخدام /filters ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **لم يتم العثور على فلاتر!**\n\n"
        "الرجاء إضافة /filters 🎨 لاختيار فلاتر إعادة التسمية التلقائية."
    )

    RENAME_CANCEL = "❌ لا، دعنا نلغي هذا ✌️"

    RENAMING_FILE = "🌀 **جاري تحويل الملف...**"

    DL_RENAMING_FILE = "📥 **جاري تحميل كنزك الرقمي...**"

    RENAME_ERRORED_REPORT = "💥 **يا للأسف! حدث خطأ ما!** الرجاء الإبلاغ عن هذا 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **لقد لوحت بعصا الإلغاء!** ✨"

    FLTR_ADD_LEFT_STR = "➕ تمت إضافة الفلتر: `<code>{{ text_1 }}</code>` **إلى اليسار**."
    FLTR_ADD_RIGHT_STR = (
        "➕ تمت إضافة الفلتر: `<code>{{ text_1 }}</code>` **إلى اليمين**."
    )
    FLTR_RM_STR = "❌ إزالة الفلتر: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 استبدال الفلتر: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **لوحة تحكم الفلاتر الخاصة بك:**"
    ADD_FLTR = "➕ إضافة فلتر"
    RM_FLTR = "❌ إزالة فلتر"

    FILTERS_INTRO = (
        "🛠 **دليل الفلاتر:**\n"
        "هناك 3 أنواع من الفلاتر:\n\n"
        "🔄 **فلتر الاستبدال:** استبدال كلمة معينة بأخرى.\n"
        "➕ **فلتر الإضافة:** إضافة كلمة في البداية أو النهاية.\n"
        "❌ **فلتر الإزالة:** إزالة كلمة من اسم الملف."
    )

    ADD_REPLACE_FLTR = "➕ إضافة فلتر استبدال"
    ADD_ADDITION_FLTR = "➕ إضافة فلتر إضافة"
    ADD_REMOVE_FLTR = "➕ إضافة فلتر إزالة"
    BACK = "🔙 رجوع"

    REPALCE_FILTER_INIT_MSG = "✍️ أرسل التنسيق: `<code>ما_يتم_استبداله | البديل</code>` أو /ignore للعودة."

    NO_INPUT_FROM_USER = "🤷‍♂️ **صمت...** لم يتم اكتشاف أي إدخال!"
    INPUT_IGNORE = "👍 **تم التجاهل!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **عذرًا!** تنسيق خاطئ! تحقق من التنسيق المقدم وحاول مرة أخرى!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **تمت إضافة فلتر الاستبدال:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ أدخل النص للإضافة بين `<code>|</code>`\n"
        "مثال: `<code>| النص المراد إضافته |</code>`\n"
        "أو /ignore للعودة."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ تمت إضافة الفلتر: `<code>{{ text_1 }}</code>` **إلى اليسار**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ تمت إضافة الفلتر: `<code>{{ text_1 }}</code>` **إلى اليمين**."
    )

    ADDITION_LEFT = "🔄 إضافة إلى اليسار"
    ADDITION_RIGHT = "🔄 إضافة إلى اليمين"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **أين تريد إضافة النص؟**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ أدخل النص الذي تريد إزالته أو /ignore للعودة."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **تمت إضافة فلتر الإزالة:** سيتم إزالة `<code>{{ text_1 }}</code>`."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 اكتمل التحميل! جاهز للسحر...",
        "📦 تم الحصول على الملف! جاهز لسحر التسمية...",
        "✨ التحميل ناجح! بدء الطلاسم...",
        "⚡ تم تأمين البيانات! محركات إعادة التسمية تشتعل...",
        "💾 تم التقاط الملف! جاهز لإعادة الميلاد المجيدة..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **إنطلاق!** تم إطلاق الملف المُعاد تسميته!",
        "🎉 **ها هو!** ملفك المُسمى جديدًا جاهز!",
        "📤 اكتمل الرفع! استمتح بتحفتك!",
        "🌟 اكتمل تحول الملف!",
        "🏁 انتهى السباق! ملفك عبر خط النهاية!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **أوقف!** تم مقاطعة تعويذة التحميل!",
        "🚧 عذرًا! أوقفت قطار التحميل!",
        "🎭 انتهى العرض قبل أن يبدأ!",
        "📵 تم إنهاء اتصال التحميل!",
        "👋 لقد غادرت التحميل! إلى اللقاء!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **انتظر!** تم إيقاف الرفع في منتصف الطريق!",
        "🚫 لا توصيل اليوم! تم إلغاء الرفع!",
        "🌪️ تبدد إعصار الرفع!",
        "📴 اتصال مفقود في الفراغ!",
        "🤷‍♂️ لقد غيرت رأيك! تم إحباط الرفع!"
    ]

    REPLY_TO_MEDIA = "📎 **بس!** رد `/rename` على ملف!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **انفجار!** فشلت تعويذة إعادة التسمية!"

    DOWNLOADING_THE_FILE = "📥 **جاري جلب ملفك...**"
    UPLOADING_THE_FILE = "📤 **جاري الإطلاق:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **بدأت مهمة إعادة التسمية**\n"
        "🆔 معرف المهمة: `{{ uid }}`\n\n"
        "👤 **العميل:** @{{ username }}\n"
        "📛 **الاسم الرمزي:** {{ name }}\n"
        "🪪 **الهوية:** `{{ user_id }}`\n"
        "📜 **الملف:** `{{ file_name }}`\n\n"
        "`⚡ تم تشغيل الدفع الفائق!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **تمت إضافة مهمة إعادة التسمية إلى قائمة الانتظار**\n\n"
        "👤 **العميل:** @{{ username }}\n"
        "📛 **الاسم الرمزي:** {{ name }}\n"
        "🪪 **الهوية:** `{{ user_id }}`\n\n"
        "`⏳ في انتظار النشر...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **نصيحة محترف:** استخدم /setcaption لإضافة لمسة جمالية!\n"
        "✨ استخدم `/setcaption {file_name}` لملء اسم الملف تلقائيًا في التسمية التوضيحية!"
    )

    DELETE_CAPTION = "🗑️ حذف التسمية"
    CLOSE = "🚪 خروج"

    CAPTION_CURRENT = "📝 **التسمية الحالية:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **التسمية فارغة!** وحيدة جدًا..."
    CAPTION_SET = "✅ **تسمية جديدة:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **تم حذف التسمية بنجاح.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **إعادة التسمية في قائمة الانتظار**\n"
        "🆔 **معرف DC:** {{ dc_id }}\n"
        "📦 **معرف الوسائط:** {{ media_id }}\n\n"
        "`⏳ اصبر يا بادوان الصغير...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **إحصائيات قائمة الانتظار:**\n"
        "📊 **إجمالي المهام:** {{ total_tasks }}\n"
        "⚡ **السعة:** {{ queue_capacity }}\n"
        "⏳ **قيد المعالجة:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **ملفك يجري تحويله بالسحر!**\n"
        "🆔 **معرف المهمة:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **مكانك في الطابور:** {{ task_number }}\n"
        "🆔 **معرف المهمة:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **لقد تم طردك!** لا بوت لك!"
    USER_NOT_PARTICIPANT = (
        "🔒 **تنبيه نادي السري!**\n\n"
        "انضم إلى قناتنا لفتح السحر!\n\n"
        "`🦄 وحيد القرن فقط بعد هذه النقطة`"
    )
    
    JOIN_CHANNEL = "🔗 الانضمام إلى النادي السري"

    MODE_INITIAL_MSG = (
        "🎛️ **أداة اختيار وضع الإخراج:**\n\n"
        "1️⃣ **الحفاظ على التنسيق الأصلي**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **فرض وضع المستند**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **وضع الوسائط العامة**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **نمط إعادة التسمية:**\n"
        "🅰️ **إعادة تسمية بالأمر**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **إعادة تسمية تلقائية**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ وضع OG"
    MODE_SET_1 = "2️⃣ وضع المستند"
    MODE_SET_2 = "3️⃣ وضع الوسائط"
    COMMAND_MODE_SET_3 = "🅰️ أمر"
    COMMAND_MODE_SET_4 = "🅱️ تلقائي"

    THUMB_REPLY_TO_MEDIA = "🖼️ **رد على صورة** لتعيينها كصورة مصغرة"
    THUMB_SET_SUCCESS = "✅ **تم تعيين الصورة المصغرة!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **لم يتم اكتشاف صورة مصغرة!**"
    THUMB_CLEARED = "🧹 **تم مسح الصورة المصغرة!**"

    HELP_STR = (
        "📚 **كتاب التعاويذ السحرية:**\n"
        "`{{ startcmd }}` - تحقق إذا كنت على قيد الحياة! 💓\n"
        "`{{ renamecmd }}` - أعد تسمية الملفات مثل رئيس! 🎩\n"
        "`{{ filterscmd }}` - خصص فلاتر إعادة التسمية الخاصة بك! ✨\n"
        "`{{ setthumbcmd }}` - تعيين صورة مصغرة دائمة! 🖼️\n"
        "`{{ getthumbcmd }}` - ألق نظرة على الصورة المصغرة الحالية! 👀\n"
        "`{{ clrthumbcmd }}` - حذف الصورة المصغرة! 🗑️\n"
        "`{{ modecmd }}` - تبديل أوضاع الإخراج:\n"
        "   - 📝 التنسيق الأصلي\n"
        "   - 📂 فرض مستند\n"
        "   - 🎥 وضع الوسائط\n\n"
        "   تبديل أنماط إعادة التسمية:\n"
        "   - 🏷️ قائم على الأمر\n"
        "   - 🤖 إعادة تسمية تلقائية (يجب إضافة /filters)\n\n"
        "`{{ queuecmd }}` - تحقق من طابور إعادة التسمية 📊\n"
        "`{{ setcaptioncmd }}` - تعيين تسميات توضيحية فاخرة 🎨\n"
        "`{{ helpcmd }}` - هذا الكتاب السحري! 📖\n"
        "`{{ pingcmd }}` - بينغ-بونغ! 🏓\n"
        "`{{ infocmd }}` - مواصفات البوت! 🤖\n"
        "`{{ profilecmd }}` - إحصائياتك! 📈\n"
        "`{{ statuscmd }}` - مؤشرات حيوية للبوت! 💓\n"
        "`{{ statscmd }}` - أرقام عالمية! 🌍\n"
        "`{{ broadcastcmd }}` - إعلان ضخم! 📢\n"
        "`{{ leaderboardcmd }}` - أفضل المستخدمين! 🏆\n"
        "`{{ setlanguagecmd }}` - تغيير اللغة! 🌐"
    )

    CURRENT_LOCALE = "🌍 **لغتك:** {{ user_locale }}"
