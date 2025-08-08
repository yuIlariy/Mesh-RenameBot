from dataclasses import dataclass
import random

@dataclass
class ArabicTranslations:
    LANGUAGE_NAME = "العربية"
    LANGUAGE_CODE = "ar"

    WRONGVALUEERROR = "❌ قيم غير صالحة تم إدخالها للمتغير <code>{{ variable_name }}</code>."

    START_MSG = (
    "مرحباً! 👋\n"
    "أنا بوت إعادة تسمية الملفات، مساعدك لإعادة تسمية الملفات على تيليجرام بسهولة.\n\n"
    "✨ **الميزات الرئيسية:**\n"
    "- إعادة تسمية الملفات بأسماء وامتدادات مخصصة.\n"
    "- سريع، آمن وسهل الاستخدام.\n"
    "- يدعم العديد من أنواع الملفات.\n\n"
    "ما عليك سوى إرسال ملف وسأرشدك خلال عملية إعادة التسمية!\n\n"
    "لنبدأ! استخدم /mode لتفعيل الوضع التلقائي، أو أعد التسمية دون أوامر 🚀\n"
    "أرسل /help للمزيد من المعلومات.\n\n"
    "🚀 **بواسطة** [NAm](https://t.me/xspes)"
    )

    
    CANCEL_MESSAGE = "⚠️ تم إلغاء عملية إعادة التسمية. سيتم التحديث قريباً."

    RENAMENOFILTER_MATCH = (
        "🚫 لا يوجد تطابق للفلاتر - إلغاء إعادة التسمية\n\n"
        "🔍 يتم استخدام الفلاتر لإعادة التسمية حيث لم يتم تحديد اسم.\n"
        "👻 يمكنك إدارة الفلاتر باستخدام /filters."
    )

    RENAMEFILTERMATCH_USED = (
        "✅ يتم استخدام الفلاتر لإعادة التسمية حيث لم يتم تحديد اسم.\n"
        "👻 يمكنك إدارة الفلاتر باستخدام /filters."
    )

    RENAMENOFLTRNONAME = (
        "✍️ أدخل اسم الملف الجديد بالصيغة:\n"
        "/rename اسم_ملفي_الجديد.الامتداد\n"
        "أو استخدم /filters لتعيين فلاتر إعادة التسمية."
    )

    RENAME_CANCEL = "❌ إلغاء عملية إعادة التسمية."

    RENAMING_FILE = "🔄 جاري إعادة تسمية الملف... الرجاء الانتظار."

    DLRENAMINGFILE = "📥 جاري تحميل الملف... الرجاء الانتظار."

    RENAMEERROREDREPORT = "❗ حدث خطأ أثناء التحميل. يرجى الإبلاغ عن هذه المشكلة."

    RENAMECANCELBY_USER = "🚫 تم الإلغاء من قبل المستخدم."

    FLTRADDLEFTSTR = "➕ تمت إضافة فلتر: <code>{{ text1 }}</code> إلى اليسار."
    FLTRADDRIGHT_STR = (
        "➕ تمت إضافة فلتر: <code>{{ text_1 }}</code> إلى اليمين."
    )
    FLTRRMSTR = "❌ تم إزالة الفلتر: <code>{{ text_1 }}</code>."
    FLTRREPLACESTR = (
        "🔄 تم استبدال الفلتر: <code>{{ text1 }}</code> → <code>{{ text2 }}</code>."
    )

    CURRENT_FLTRS = "⚙️ الفلاتر الحالية:"
    ADD_FLTR = "➕ إضافة فلتر"
    RM_FLTR = "❌ إزالة فلتر"

    FILTERS_INTRO = (
        "🛠 دليل الفلاتر:\n"
        "هناك 3 أنواع من الفلاتر:\n\n"
        "🔄 فلتر الاستبدال: استبدال كلمة معينة بأخرى.\n"
        "➕ فلتر الإضافة: إضافة كلمة في البداية أو النهاية.\n"
        "❌ فلتر الإزالة: إزالة كلمة من اسم الملف."
    )

    ADDREPLACEFLTR = "➕ إضافة فلتر استبدال"
    ADDADDITIONFLTR = "➕ إضافة فلتر إضافة"
    ADDREMOVEFLTR = "➕ إضافة فلتر إزالة"
    BACK = "🔙 رجوع"

    REPALCEFILTERINITMSG = "✍️ أرسل الصيغة: <code>ما_يتم_استبداله | البديل</code> أو /ignore للرجوع."

    NOINPUTFROM_USER = "⚠️ لم يتم استقبال أي مدخلات منك."
    INPUT_IGNORE = "✅ تم التجاهل."
    WRONGINPUTFORMAT = "❌ صيغة غير صالحة. يرجى مراجعة الصيغة المقدمة."
    REPLACEFILTERSUCCESS = (
        "✅ تمت إضافة فلتر الاستبدال:\n" "'{{ text1 }}' → '{{ text2 }}'"
    )

    ADDITIONFILTERINIT_MSG = (
        "✍️ أدخل النص المراد إضافته بين <code>|</code>\n"
        "مثال: <code>| النص المضاف |</code>\n"
        "أو /ignore للرجوع."
    )

    ADDITIONFILTERSUCCESS_LEFT = (
        "✅ تمت إضافة الفلتر: <code>{{ text_1 }}</code> إلى اليسار."
    )
    ADDITIONFILTERSUCCESS_RIGHT = (
        "✅ تمت إضافة الفلتر: <code>{{ text_1 }}</code> إلى اليمين."
    )

    ADDITION_LEFT = "🔄 إضافة إلى اليسار"
    ADDITION_RIGHT = "🔄 إضافة إلى اليمين"

    ADDITIONPOSITIONPROMPT = "📍 أين تريد إضافة النص؟"

    REMOVEFILTERINIT_MSG = (
        "✍️ أدخل النص الذي تريد إزالته أو /ignore للرجوع."
    )

    REMOVEFILTERSUCCESS = (
        "✅ تمت إضافة فلتر الإزالة: سيتم إزالة <code>{{ text_1 }}</code>."
    )

    RENAMETHEMESDOWNLOADING = [
        "✅ اكتمل التحميل. بدء سحر إعادة التسمية...",
        "📦 تم جلب الملف! جاهز لمنحه اسمًا جديدًا...",
        "🪄 اكتمل التحميل. ✨ لنبدأ طقوس إعادة التسمية...",
        "🔧 تم الحصول على البيانات. محرك إعادة التسمية يعمل...",
        "💾 تم الحفظ والإغلاق. الآن لإعادة التسمية بأناقة...",
    ]

    RENAMETHEMESUPLOADING = [
        "✅ اكتملت إعادة التسمية! التحميل انتهى.",
        "🚀 تمت إعادة تسمية الملف بنجاح وإطلاقه.",
        "📤 اكتمل التحميل. تحفة إعادة التسمية جاهزة!",
        "🌟 اكتملت إعادة تسمية الملف. تم التسليم إلى الكون!",
        "📁 اكتملت المهمة. تمت إعادة تسمية الملف.",
    ]

    RENAMETHEMESDOWNLOAD_CANCELLED = [
        "🛑 تم إيقاف التحميل. حلم إعادة التسمية يتلاشى...",
        "🚫 لقد أوقفت العملية. تم إلغاء التحميل.",
        "❌ تم إلغاء العملية أثناء التنفيذ. لم يتم جلب الملف.",
        "📴 تم إلغاء إعادة التسمية أثناء التحميل. المهمة ألغيت.",
        "👋 قام المستخدم بالإلغاء أثناء التحميل. وداعاً أيها الملف.",
    ]

    RENAMETHEMESUPLOAD_CANCELLED = [
        "🛑 تم إلغاء التحميل. الملف باقٍ محلياً دون استخدام.",
        "🚫 تم التراجع عن إعادة التسمية. تم إيقاف التحميل.",
        "❌ تمت مقاطعة المرحلة النهائية. تم التخلي عن إعادة التسمية.",
        "📴 تم رفض التحميل. الملف المعاد تسميته لن يذهب لأي مكان.",
        "👋 قال المستخدم 'لا' أثناء التحميل. تم إيقاف الملف.",
    ]

    REPLYTOMEDIA = "📂 رد على ملف وسائط باستخدام /rename."

    RENAMEDOWNLOADINGDONE = random.choice(RENAMETHEMESDOWNLOADING)
    RENAMEUPLOADINGDONE = random.choice(RENAMETHEMESUPLOADING)
    RENAMECANCELBYUSER = random.choice(RENAMETHEMESDOWNLOADCANCELLED)
    RENAMEUPLOADCANCELLEDBYUSER = random.choice(RENAMETHEMESUPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ حدث خطأ في عملية إعادة التسمية."

    UPLOADINGTHEFILE = "📤 جاري تحميل الملف: {{ newfilename }}"

    TRACKMESSAGEEXECUTION_START = (
        "🚀 بدء التنفيذ لمهمة إعادة التسمية\n"
        "🆔 معرف المهمة: {{ uid }}\n\n"
        "👤 اسم المستخدم: @{{ username }}\n"
        "📛 الاسم: {{ name }}\n"
        "🆔 معرف المستخدم: <code>{{ user_id }}</code>\n"
        "📂 اسم الملف: <code>{{ file_name }}</code>"
    )
    
    TRACKMESSAGEADDED_RENAME = (
        "✅ تمت إضافة مهمة إعادة التسمية\n\n"
        "👤 اسم المستخدم: @{{ username }}\n"
        "📛 الاسم: {{ name }}\n"
        "🆔 معرف المستخدم: <code>{{ user_id }}</code>"
    )

    CAPTIONFOOTNOTE = (
        "☄️ ملاحظة: يمكنك تعيين التسمية باستخدام /setcaption متبوعاً بالنص المطلوب.\n"
        "📂 استخدم <code>{file_name}</code> لإدراج اسم الملف المعاد تسميته ديناميكياً في التسمية."
    )

    DELETE_CAPTION = "🗑 حذف التسمية"
    CLOSE = "❌ إغلاق"

    CAPTION_CURRENT = "📝 التسمية الحالية: {{ caption }}"
    CAPTIONNOTSET = "⚠️ لا توجد تسمية معينة."
    CAPTION_SET = "✅ تم تحديث التسمية إلى: {{ caption }}"
    CAPTION_DELETED = "🗑 تم حذف التسمية بنجاح."

    RENAMEADDEDTO_QUEUE = (
        "📥 تمت إضافة مهمة إعادة التسمية إلى قائمة الانتظار\n"
        "🆔 معرف DC: {{ dc_id }}\n"
        "👻 معرف الوسائط: {{ media_id }}"
    )

    RENAMEQUEUESTATUS = (
        "📊 حالة قائمة انتظار إعادة التسمية:\n"
        "☄️ إجمالي المهام في قائمة الانتظار: {{ total_tasks }}\n"
        "⚡ سعة قائمة الانتظار: {{ queue_capacity }}\n"
        "⏳ جاري المعالجة حالياً: {{ current_task }}"
    )

    RENAMEQUEUEUSER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ مهمتك قيد التنفيذ حالياً\n"
        "🆔 معرف المهمة: {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ موقع مهمتك في قائمة الانتظار: {{ task_number }}\n"
        "🆔 معرف المهمة: {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 تمت إزالتك من الدردشة. لا يمكنك استخدام هذا البوت."
    USERNOTPARTICIPANT = "👻 يرجى الانضمام إلى الدردشة المطلوبة لاستخدام هذا البوت."
    JOIN_CHANNEL = "🔗 انضم لقناة التحديثات"

    MODEINITIALMSG = (
        "📂 وضع إخراج الملف:\n\n"
        "1️⃣ نفس الصيغة المرسلة."
        "{% if mode == udb.MODESAMEAS_SENT %} ✅{% endif %}\n"
        "2️⃣ إجبار كوثيقة."
        "{% if mode == udb.MODEASDOCUMENT %} ✅{% endif %}\n"
        "3️⃣ تحميل كوسائط عامة."
        "{% if mode == udb.MODEASGMEDIA %} ✅{% endif %}\n\n"
        "👻 اختر وضع إعادة التسمية:\n"
        "🅰️ إعادة التسمية بالأمر."
        "{% if commandmode == udb.MODERENAMEWITHCOMMAND %} ✅{% endif %}\n"
        "🅱️ إعادة التسمية بدون أمر."
        "{% if commandmode == udb.MODERENAMEWITHOUTCOMMAND %} ✅{% endif %}"
    )

    MODESET0 = "1️⃣"
    MODESET1 = "2️⃣"
    MODESET2 = "3️⃣"
    COMMANDMODESET_3 = "🅰️"
    COMMANDMODESET_4 = "🅱️"

    THUMBREPLYTO_MEDIA = "📸 رد على صورة لتعيينها كصورة مصغرة."
    THUMBSETSUCCESS = "✅ تم تعيين الصورة المصغرة بنجاح."
    THUMBNOTFOUND = "⚠️ لم يتم العثور على صورة مصغرة."
    THUMB_CLEARED = "🗑 تم مسح الصورة المصغرة بنجاح."

    HELP_STR = (
        "📖 أوامر البوت:\n"
        "{{ startcmd }} - ✅ التحقق من عمل البوت.\n"
        "{{ renamecmd }} - ✍️ رد على ملف وسائط مع /rename اسم_الملف.الامتداد لإعادة تسميته.\n"
        "{{ filterscmd }} - ⚙️ إدارة فلاتر إعادة التسمية.\n"
        "{{ setthumbcmd }} - 📷 تعيين صورة مصغرة دائمة (الرد على صورة).\n"
        "{{ getthumbcmd }} - 📸 الحصول على الصورة المصغرة الحالية.\n"
        "{{ clrthumbcmd }} - ❌ إزالة الصورة المصغرة المعينة.\n"
        "{{ modecmd }} - 🔄 التبديل بين 3 أوضاع إخراج:\n"
        "    - 📝 نفس الصيغة المرسلة.\n"
        "    - 📂 وثيقة مجبرة.\n"
        "    - 🎥 وسائط عامة (فيديو/صوت قابل للبث).\n\n"
        "    🔄 التبديل بين أوضاع إعادة التسمية:\n"
        "    - 🏷 إعادة التسمية بالأمر.\n"
        "    - ✨ إعادة التسمية بدون أمر/تلقائي.\n\n"
        "{{ queuecmd }} - 📊 عرض حالة قائمة انتظار إعادة التسمية.\n"
        "{{ setcaptioncmd }} - 📝 تعيين تسمية للملفات المعاد تسميتها.\n"
        "{{ helpcmd }} - 📖 عرض رسالة المساعدة هذه.\n"
        "{{ pingcmd }} - 🎈 اختبار البوت.\n"
        "{{ infocmd }} - 🧑‍💻 عرض معلومات البوت.\n"
        "{{ profilecmd }} - ☄️ إحصائيات استخدامك.\n"
        "{{ statuscmd }} - 🗿 حالة البوت.\n"
        "{{ statscmd }} - 👻 إحصائيات البوت العالمية.\n"
        "{{ broadcastcmd }} - ☄️ البث.\n"
        "{{ leaderboardcmd }} - 👻 لوحة المتصدرين للمستخدمين.\n"
        "{{ setlanguagecmd }} - 🌐 تغيير لغة البوت."
    )

    CURRENTLOCALE = "🌐 لغتك الحالية: {{ userlocale }}"



