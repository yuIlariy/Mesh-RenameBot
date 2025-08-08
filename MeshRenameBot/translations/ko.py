from dataclasses import dataclass
import random

@dataclass
class KoreanTranslations:
    LANGUAGE_NAME = "한국어"
    LANGUAGE_CODE = "ko"

    WRONG_VALUE_ERROR = "❌ {{ variable_name }} 변수에 잘못된 값이 입력되었습니다."

    START_MSG = (
    "안녕하세요! 👋\n"
    "저는 **파일 이름 변경 봇**입니다. 텔레그램에서 쉽게 파일 이름을 변경할 수 있도록 도와드립니다.\n\n"
    "✨ **주요 기능:**\n"
    "- 사용자 지정 이름과 확장자로 파일 이름 변경\n"
    "- 빠르고 안전하며 사용하기 쉬움\n"
    "- 다양한 파일 형식 지원\n\n"
    "파일을 보내주시면 이름 변경 과정을 안내해 드리겠습니다!\n\n"
    "시작해볼까요? /mode로 자동 이름 변경을 활성화하세요, **명령 없이 이름 변경**🚀\n"
    "더 알아보려면 /help를 보내주세요.\n\n"
    "🚀 **제공** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "⚠️ 이름 변경이 **취소**되었습니다. 곧 업데이트될 예정입니다."

    RENAME_NO_FILTER_MATCH = (
        "🚫 **일치하는 필터 없음 - 이름 변경 중단**\n\n"
        "🔍 이름이 지정되지 않아 필터를 사용하여 이름을 변경합니다.\n"
        "👻 /filters로 필터를 관리하세요."
    )

    RENAME_FILTER_MATCH_USED = (
        "✅ 이름이 지정되지 않아 필터를 사용하여 이름을 변경합니다.\n"
        "👻 /filters로 필터를 관리하세요."
    )

    RENAME_NOFLTR_NONAME = (
        "✍️ 새 파일 이름을 다음 형식으로 입력하세요:\n"
        "```/rename 새_파일_이름.확장자```\n"
        "또는 `/filters`로 이름 변경 필터를 설정하세요."
    )

    RENAME_CANCEL = "❌ 이 이름 변경 취소"

    RENAMING_FILE = "🔄 파일 이름 변경 중... 잠시 기다려주세요."

    DL_RENAMING_FILE = "📥 파일 다운로드 중... 잠시 기다려주세요."

    RENAME_ERRORED_REPORT = "❗ 다운로드 중 오류가 발생했습니다. 이 문제를 보고해주세요."

    RENAME_CANCEL_BY_USER = "🚫 **사용자에 의해 취소됨**"

    FLTR_ADD_LEFT_STR = "➕ 필터 추가: `<code>{{ text_1 }}</code>` **왼쪽에**."
    FLTR_ADD_RIGHT_STR = (
        "➕ 추가 필터: `<code>{{ text_1 }}</code>` **오른쪽에**."
    )
    FLTR_RM_STR = "❌ 필터 제거: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 필터 교체: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "⚙️ **현재 필터:**"
    ADD_FLTR = "➕ 필터 추가"
    RM_FLTR = "❌ 필터 제거"

    FILTERS_INTRO = (
        "🛠 **필터 가이드:**\n"
        "3가지 유형의 필터가 있습니다:\n\n"
        "🔄 **교체 필터:** 주어진 단어를 다른 단어로 교체\n"
        "➕ **추가 필터:** 시작 또는 끝에 단어 추가\n"
        "❌ **제거 필터:** 파일 이름에서 단어 제거"
    )

    ADD_REPLACE_FLTR = "➕ 교체 필터 추가"
    ADD_ADDITION_FLTR = "➕ 추가 필터 추가"
    ADD_REMOVE_FLTR = "➕ 제거 필터 추가"
    BACK = "🔙 뒤로"

    REPALCE_FILTER_INIT_MSG = "✍️ 형식 보내기: `<code>바꿀_단어 | 교체_단어</code>` 또는 `/ignore`로 돌아가기"

    NO_INPUT_FROM_USER = "⚠️ 입력이 없습니다."
    INPUT_IGNORE = "✅ **무시됨**"
    WRONG_INPUT_FORMAT = "❌ 잘못된 형식입니다. 제공된 형식을 확인하세요."
    REPLACE_FILTER_SUCCESS = (
        "✅ **교체 필터 추가됨:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ 추가할 텍스트를 `<code>|</code>` 사이에 입력하세요\n"
        "예: `<code>| 추가할 텍스트 |</code>`\n"
        "또는 `/ignore`로 돌아가기"
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ 필터 추가됨: `<code>{{ text_1 }}</code>` **왼쪽에**"
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ 필터 추가됨: `<code>{{ text_1 }}</code>` **오른쪽에**"
    )

    ADDITION_LEFT = "🔄 왼쪽에 추가"
    ADDITION_RIGHT = "🔄 오른쪽에 추가"

    ADDITION_POSITION_PROMPT = "📍 **텍스트를 어디에 추가하시겠습니까?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ 제거할 텍스트를 입력하거나 `/ignore`로 돌아가기"
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **제거 필터 추가됨:** `<code>{{ text_1 }}</code>`가 제거됩니다."
    )

    RENAME_THEMES_DOWNLOADING = [
        "✅ 다운로드 완료. 이름 변경을 시작합니다...",
        "📦 파일 가져옴! 새 이름을 부여할 준비 완료...",
        "🪄 다운로드 완료. ✨ 이름 변경 의식을 시작합니다...",
        "🔧 데이터 획득. 이름 변경 엔진 가동 중...",
        "💾 저장 및 완료. 이제 스타일리시하게 이름을 변경합니다...",
    ]

    RENAME_THEMES_UPLOADING = [
        "✅ 모두 이름 변경 완료! 업로드 완료.",
        "🚀 파일 이름 변경 및 성공적으로 업로드됨.",
        "📤 업로드 완료. 새 이름의 파일이 준비되었습니다!",
        "🌟 파일 이름 변경 완료. 우주로 전송됨!",
        "📁 작업 완료. 파일이 새 이름으로 변경되었습니다.",
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 다운로드 중단. 이름 변경 꿈이 사라집니다...",
        "🚫 연결을 끊었습니다. 다운로드 중단됨.",
        "❌ 작업 중간에 취소됨. 파일을 가져오지 못함.",
        "📴 다운로드 중 이름 변경 취소. 미션 중단.",
        "👋 사용자가 다운로드 중간에 취소함. 안녕, 파일.",
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "🛑 업로드 취소됨. 파일은 로컬에 남아있습니다.",
        "🚫 이름 변경 되돌림. 업로드 종료.",
        "❌ 최종 단계 중단. 이름 변경 포기.",
        "📴 업로드 거부됨. 이름 변경된 파일은 어디에도 가지 않음.",
        "👋 사용자가 업로드 중 '아니오'라고 함. 파일 퇴역.",
    ]

    REPLY_TO_MEDIA = "📂 미디어 파일에 `/rename`으로 답장하세요."

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "❗ 이름 변경 과정에서 오류가 발생했습니다."

    UPLOADING_THE_FILE = "📤 파일 업로드 중: **{{ new_file_name }}**"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **이름 변경 작업 실행 시작**\n"
        "🆔 작업 ID: `{{ uid }}`\n\n"
        "👤 **사용자 이름:** @{{ username }}\n"
        "📛 **이름:** {{ name }}\n"
        "🆔 **사용자 ID:** `<code>{{ user_id }}</code>`\n"
        "📂 **파일 이름:** `<code>{{ file_name }}</code>`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "✅ **이름 변경 작업 추가됨**\n\n"
        "👤 **사용자 이름:** @{{ username }}\n"
        "📛 **이름:** {{ name }}\n"
        "🆔 **사용자 ID:** `<code>{{ user_id }}</code>`"
    )

    CAPTION_FOOT_NOTE = (
        "☄️ **참고:** `/setcaption` 다음에 원하는 텍스트를 입력하여 캡션을 설정할 수 있습니다.\n"
        "📂 캡션에 변경된 파일 이름을 동적으로 삽입하려면 `<code>{file_name}</code>`을 사용하세요."
    )

    DELETE_CAPTION = "🗑 캡션 삭제"
    CLOSE = "❌ 닫기"

    CAPTION_CURRENT = "📝 **현재 캡션:** {{ caption }}"
    CAPTION_NOT_SET = "⚠️ **캡션이 설정되지 않음**"
    CAPTION_SET = "✅ **캡션 업데이트됨:** {{ caption }}"
    CAPTION_DELETED = "🗑 **캡션 삭제 완료**"

    RENAME_ADDED_TO_QUEUE = (
        "📥 **이름 변경 작업이 대기열에 추가됨**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "👻 **미디어 ID:** {{ media_id }}"
    )

    RENAME_QUEUE_STATUS = (
        "📊 **이름 변경 대기열 상태:**\n"
        "☄️ **대기열의 총 작업:** {{ total_tasks }}\n"
        "⚡ **대기열 용량:** {{ queue_capacity }}\n"
        "⏳ **현재 처리 중:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **현재 작업 실행 중**\n"
        "🆔 **작업 ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **대기열에서의 작업 위치:** {{ task_number }}\n"
        "🆔 **작업 ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👻 **채팅에서 제거되었습니다. 이 봇을 사용할 수 없습니다.**"
    USER_NOT_PARTICIPANT = "👻 **이 봇을 사용하려면 필수 채팅에 참여하세요.**"
    JOIN_CHANNEL = "🔗 업데이트 채널 가입"

    MODE_INITIAL_MSG = (
        "📂 **파일 출력 모드:**\n\n"
        "1️⃣ **보낸 형식과 동일**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **문서로 강제**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **일반 미디어로 업로드**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "👻 **이름 변경 모드 선택:**\n"
        "🅰️ **명령으로 이름 변경**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **명령 없이 이름 변경**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣"
    MODE_SET_1 = "2️⃣"
    MODE_SET_2 = "3️⃣"
    COMMAND_MODE_SET_3 = "🅰️"
    COMMAND_MODE_SET_4 = "🅱️"

    THUMB_REPLY_TO_MEDIA = "📸 썸네일로 설정할 이미지에 답장하세요."
    THUMB_SET_SUCCESS = "✅ **썸네일 설정 완료**"
    THUMB_NOT_FOUND = "⚠️ **썸네일을 찾을 수 없음**"
    THUMB_CLEARED = "🗑 **썸네일 삭제 완료**"

    HELP_STR = (
        "📖 **봇 명령어:**\n"
        "`{{ startcmd }}` - ✅ 봇이 실행 중인지 확인\n"
        "`{{ renamecmd }}` - ✍️ 미디어 파일에 `/rename 파일이름.확장자`로 답장하여 이름 변경\n"
        "`{{ filterscmd }}` - ⚙️ 이름 변경 필터 관리\n"
        "`{{ setthumbcmd }}` - 📷 영구 썸네일 설정 (이미지에 답장)\n"
        "`{{ getthumbcmd }}` - 📸 현재 설정된 썸네일 가져오기\n"
        "`{{ clrthumbcmd }}` - ❌ 설정된 썸네일 제거\n"
        "`{{ modecmd }}` - 🔄 3가지 출력 모드 전환:\n"
        "    - 📝 보낸 형식과 동일\n"
        "    - 📂 문서로 강제\n"
        "    - 🎥 일반 미디어 (스트리밍 가능한 비디오/오디오)\n\n"
        "    🔄 이름 변경 모드 전환:\n"
        "    - 🏷 **명령으로 이름 변경**\n"
        "    - ✨ **명령 없이/자동 이름 변경**\n\n"
        "`{{ queuecmd }}` - 📊 봇의 이름 변경 대기열 상태 보기\n"
        "`{{ setcaptioncmd }}` - 📝 이름 변경된 파일에 대한 캡션 설정\n"
        "`{{ helpcmd }}` - 📖 이 도움말 메시지 표시\n"
        "`{{ pingcmd }}` - 🎈봇 핑\n"
        "`{{ infocmd }}` - 🧑‍💻 봇 정보 보기\n"
        "`{{ profilecmd }}` - ☄️ 사용 통계\n"
        "`{{ statuscmd }}` - 🗿 봇 상태\n"
        "`{{ statscmd }}` - 👻 전역 봇 통계\n"
        "`{{ broadcastcmd }}` - ☄️브로드캐스트\n"
        "`{{ leaderboardcmd }}` - 👻 사용자 순위표\n"
        "`{{ setlanguagecmd }}` - 🌐 봇 언어 변경"
    )

    CURRENT_LOCALE = "🌐 **현재 언어:** {{ user_locale }}"




