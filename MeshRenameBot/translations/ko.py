from dataclasses import dataclass
import random

@dataclass
class KoreanTranslations:
    LANGUAGE_NAME = "🇰🇷 한국어"
    LANGUAGE_CODE = "ko"

    WRONG_VALUE_ERROR = "❌ 이런! {{ variable_name }}에 대한 잘못된 값입니다. 다시 시도하세요! 🤷‍♀️"

    START_MSG = (
    "✨ **안녕하세요, 파일 마법사님!** ✨\n\n"
    "저는 **자동 이름 변경 봇** 🪄입니다, 여러분의 마법 같은 파일 이름 변경 도우미!\n\n"
    "🔥 **저를 사랑할 이유:**\n"
    "- ✨ 빛나는 정확도로 파일 이름 변경\n"
    "- 번개처럼 빠른 ⚡ 보안 🔒\n"
    "- 모든 파일 형식 지원! 📂🎵🎬\n\n"
    "파일을 보내주시면 마법을 시작해요! 🎩\n\n"
    "🚀 **프로 팁:** 자동 이름 변경 닌자 모드를 위해 /mode 사용 (/filters 추가 필수)!\n"
    "도움이 필요하세요? /help가 있습니다!\n\n"
    "🛸 **제공:** [NAm](https://t.me/xspes)"
    )

    CANCEL_MESSAGE = "❗ 이름 변경 취소! 퐁! ✨ (곧 업데이트 예정!)"

    RENAME_NO_FILTER_MATCH = (
        "🔮 **이런! 필터 일치 없음!**\n\n"
        "필터를 사용해봤지만 아무것도 찾지 못했어요 🎩🐇\n"
        "/filters로 필터 관리하기 ✏️"
    )

    RENAME_FILTER_MATCH_USED = (
        "🎯 **필터 파워 활성화!**\n"
        "이름을 지정하지 않아 필터 사용 중\n"
        "/filters로 조정하기 ⚙️"
    )

    RENAME_NOFLTR_NONAME = (
        "📝 **필터를 찾을 수 없습니다!**\n\n"
        "자동 선택 이름 변경 필터를 위해 /filters 🎨를 추가해주세요."
    )

    RENAME_CANCEL = "❌ 아니요, 취소할게요 ✌️"

    RENAMING_FILE = "🌀 **파일 변환 진행 중...**"

    DL_RENAMING_FILE = "📥 **디지털 보물 다운로드 중...**"

    RENAME_ERRORED_REPORT = "💥 **이런! 뭔가 고장났어요!** 이 문제를 신고해주세요 🚨"

    RENAME_CANCEL_BY_USER = "🙅‍♂️ **취소 지팡이를 휘둘렀어요!** ✨"

    FLTR_ADD_LEFT_STR = "➕ 필터 추가: `<code>{{ text_1 }}</code>` **왼쪽으로**."
    FLTR_ADD_RIGHT_STR = (
        "➕ 필터 추가: `<code>{{ text_1 }}</code>` **오른쪽으로**."
    )
    FLTR_RM_STR = "❌ 필터 제거: `<code>{{ text_1 }}</code>`."
    FLTR_REPLACE_STR = (
        "🔄 필터 교체: `<code>{{ text_1 }}</code>` → `<code>{{ text_2 }}</code>`."
    )

    CURRENT_FLTRS = "🎛️ **필터 대시보드:**"
    ADD_FLTR = "➕ 필터 추가"
    RM_FLTR = "❌ 필터 제거"

    FILTERS_INTRO = (
        "🛠 **필터 가이드:**\n"
        "3가지 유형의 필터가 있습니다:\n\n"
        "🔄 **교체 필터:** 주어진 단어를 다른 단어로 교체합니다.\n"
        "➕ **추가 필터:** 시작이나 끝에 단어를 추가합니다.\n"
        "❌ **제거 필터:** 파일 이름에서 단어를 제거합니다."
    )

    ADD_REPLACE_FLTR = "➕ 교체 필터 추가"
    ADD_ADDITION_FLTR = "➕ 추가 필터 추가"
    ADD_REMOVE_FLTR = "➕ 제거 필터 추가"
    BACK = "🔙 뒤로"

    REPALCE_FILTER_INIT_MSG = "✍️ 형식 보내기: `<code>바꿀_내용 | 교체_내용</code>` 또는 /ignore로 돌아가기."

    NO_INPUT_FROM_USER = "🤷‍♂️ **귀뚜라미...** 입력이 감지되지 않았습니다!"
    INPUT_IGNORE = "👍 **무시됨!**"
    WRONG_INPUT_FORMAT = "🤦‍♂️ **이런!** 잘못된 형식입니다! 제공된 형식을 확인하고 다시 시도하세요!"
    REPLACE_FILTER_SUCCESS = (
        "✅ **교체 필터 추가됨:**\n" "`'{{ text_1 }}'` → `'{{ text_2 }}'`"
    )

    ADDITION_FILTER_INIT_MSG = (
        "✍️ `<code>|</code>` 안에 추가할 텍스트 입력\n"
        "예시: `<code>| 추가할 텍스트 |</code>`\n"
        "또는 /ignore로 돌아가기."
    )

    ADDITION_FILTER_SUCCESS_LEFT = (
        "✅ 필터 추가: `<code>{{ text_1 }}</code>` **왼쪽으로**."
    )
    ADDITION_FILTER_SUCCESS_RIGHT = (
        "✅ 필터 추가: `<code>{{ text_1 }}</code>` **오른쪽으로**."
    )

    ADDITION_LEFT = "🔄 왼쪽에 추가"
    ADDITION_RIGHT = "🔄 오른쪽에 추가"

    ADDITION_POSITION_PROMPT = "🧙‍♂️ **텍스트를 어디에 추가하시겠어요?**"

    REMOVE_FILTER_INIT_MSG = (
        "✍️ 제거하려는 텍스트 입력 또는 /ignore로 돌아가기."
    )

    REMOVE_FILTER_SUCCESS = (
        "✅ **제거 필터 추가됨:** `<code>{{ text_1 }}</code>`이(가) 제거됩니다."
    )

    RENAME_THEMES_DOWNLOADING = [
        "🎩 다운로드 완료! 마법 준비 중...",
        "📦 파일 획득! 이름 지정 마법 준비 완료...",
        "✨ 다운로드 성공! 주문 시작...",
        "⚡ 데이터 보안 완료! 이름 변경 엔진 가동 중...",
        "💾 파일 캡처! 영광스러운 재탄생 준비 중..."
    ]

    RENAME_THEMES_UPLOADING = [
        "🚀 **발사!** 이름 변경된 파일 발사!",
        "🎉 **짜잔!** 새 이름의 파일이 준비되었습니다!",
        "📤 업로드 완료! 여러분의 걸작을 즐기세요!",
        "🌟 파일 변환 완료!",
        "🏁 레이스 끝! 파일이 결승선을 통과했습니다!"
    ]

    RENAME_THEMES_DOWNLOAD_CANCELLED = [
        "🛑 **중단!** 다운로드 마법 중단!",
        "🚧 이런! 다운로드 열차를 멈췄어요!",
        "🎭 쇼가 시작되기 전에 끝났어요!",
        "📵 다운로드 연결 종료!",
        "👋 다운로드를 떠나셨네요! 안녕히 가세요!"
    ]

    RENAME_THEMES_UPLOAD_CANCELLED = [
        "✋ **잠깐!** 업로드 중간에 중단!",
        "🚫 오늘은 배송 없음! 업로드 취소!",
        "🌪️ 업로드 토네이도 사라짐!",
        "📴 연결이 공허 속으로 사라짐!",
        "🤷‍♂️ 마음이 바뀌셨네요! 업로드 중단!"
    ]

    REPLY_TO_MEDIA = "📎 **쉿!** 파일에 `/rename`으로 답장하세요!"

    RENAME_DOWNLOADING_DONE = random.choice(RENAME_THEMES_DOWNLOADING)
    RENAME_UPLOADING_DONE = random.choice(RENAME_THEMES_UPLOADING)
    RENAME_CANCEL_BY_USER = random.choice(RENAME_THEMES_DOWNLOAD_CANCELLED)
    RENAME_UPLOAD_CANCELLED_BY_USER = random.choice(RENAME_THEMES_UPLOAD_CANCELLED)
    RENAME_ERRORED = "💥 **쾅!** 이름 변경 마법 실패!"

    DOWNLOADING_THE_FILE = "📥 **파일 가져오는 중...**"
    UPLOADING_THE_FILE = "📤 **발사 중:** `{{ new_file_name }}` 🚀"

    TRACK_MESSAGE_EXECUTION_START = (
        "🚀 **이름 변경 미션 시작**\n"
        "🆔 미션 ID: `{{ uid }}`\n\n"
        "👤 **에이전트:** @{{ username }}\n"
        "📛 **코드명:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n"
        "📜 **파일:** `{{ file_name }}`\n\n"
        "`⚡ 하이퍼드라이브 가동!`"
    )
    
    TRACK_MESSAGE_ADDED_RENAME = (
        "📥 **이름 변경 미션 대기 중**\n\n"
        "👤 **에이전트:** @{{ username }}\n"
        "📛 **코드명:** {{ name }}\n"
        "🪪 **ID:** `{{ user_id }}`\n\n"
        "`⏳ 배포 대기 중...`"
    )

    CAPTION_FOOT_NOTE = (
        "💡 **프로 팁:** 스타일을 더하려면 /setcaption 사용!\n"
        "✨ 캡션에 파일 이름을 자동으로 채우려면 `/setcaption {file_name}` 사용!"
    )

    DELETE_CAPTION = "🗑️ 캡션 삭제"
    CLOSE = "🚪 나가기"

    CAPTION_CURRENT = "📝 **현재 캡션:** {{ caption }}"
    CAPTION_NOT_SET = "🫗 **캡션 비어있음!** 너무 외로워요..."
    CAPTION_SET = "✅ **새 캡션:** {{ caption }}"
    CAPTION_DELETED = "🗑️ **캡션 성공적으로 삭제됨.**"

    RENAME_ADDED_TO_QUEUE = (
        "📊 **이름 변경 대기 중**\n"
        "🆔 **DC ID:** {{ dc_id }}\n"
        "📦 **미디어 ID:** {{ media_id }}\n\n"
        "`⏳ 인내심을 가져요, 어린 파다완...`"
    )

    RENAME_QUEUE_STATUS = (
        "📈 **대기열 상태:**\n"
        "📊 **총 작업:** {{ total_tasks }}\n"
        "⚡ **용량:** {{ queue_capacity }}\n"
        "⏳ **처리 중:** {{ current_task }}"
    )

    RENAME_QUEUE_USER_STATUS = (
        "{% if is_executing %}\n"
        "⚡ **파일이 마법 중입니다!**\n"
        "🆔 **작업 ID:** {{ task_id }}\n"
        "{% endif %}"
        "{% if is_pending %}\n"
        "⏳ **대기열에서您的 위치:** {{ task_number }}\n"
        "🆔 **작업 ID:** {{ task_id }}\n"
        "{% endif %}"
    )

    USER_KICKED = "👢 **추방되었습니다!** 봇 사용 불가!"
    USER_NOT_PARTICIPANT = (
        "🔒 **비밀 클럽 알림!**\n\n"
        "마법을 해제하려면 우리 채널에 가입하세요!\n\n"
        "`🦄 이 지점 이후로는 유니콘만`"
    )
    
    JOIN_CHANNEL = "🔗 비밀 클럽 가입"

    MODE_INITIAL_MSG = (
        "🎛️ **출력 모드 선택기:**\n\n"
        "1️⃣ **원본 형식 유지**"
        "{% if mode == udb.MODE_SAME_AS_SENT %} ✅{% endif %}\n"
        "2️⃣ **문서 모드 강제**"
        "{% if mode == udb.MODE_AS_DOCUMENT %} ✅{% endif %}\n"
        "3️⃣ **일반 미디어 모드**"
        "{% if mode == udb.MODE_AS_GMEDIA %} ✅{% endif %}\n\n"
        "✨ **이름 변경 스타일:**\n"
        "🅰️ **명령어 이름 변경**"
        "{% if command_mode == udb.MODE_RENAME_WITH_COMMAND %} ✅{% endif %}\n"
        "🅱️ **자동 이름 변경**"
        "{% if command_mode == udb.MODE_RENAME_WITHOUT_COMMAND %} ✅{% endif %}"
    )

    MODE_SET_0 = "1️⃣ OG 모드"
    MODE_SET_1 = "2️⃣ 문서 모드"
    MODE_SET_2 = "3️⃣ 미디어 모드"
    COMMAND_MODE_SET_3 = "🅰️ 명령어"
    COMMAND_MODE_SET_4 = "🅱️ 자동"

    THUMB_REPLY_TO_MEDIA = "🖼️ **썸네일로 설정할 이미지에 답장**"
    THUMB_SET_SUCCESS = "✅ **썸네일 설정 완료!**"
    THUMB_NOT_FOUND = "🕵️‍♂️ **썸네일을 찾을 수 없습니다!**"
    THUMB_CLEARED = "🧹 **썸네일 제거됨!**"

    HELP_STR = (
        "📚 **마법 주문서:**\n"
        "`{{ startcmd }}` - 제가 살아있는지 확인! 💓\n"
        "`{{ renamecmd }}` - 보스처럼 파일 이름 변경! 🎩\n"
        "`{{ filterscmd }}` - 이름 변경 필터 사용자 정의! ✨\n"
        "`{{ setthumbcmd }}` - 영구 썸네일 설정! 🖼️\n"
        "`{{ getthumbcmd }}` - 현재 썸네일 확인! 👀\n"
        "`{{ clrthumbcmd }}` - 썸네일 삭제! 🗑️\n"
        "`{{ modecmd }}` - 출력 모드 전환:\n"
        "   - 📝 원본 형식\n"
        "   - 📂 문서 강제\n"
        "   - 🎥 미디어 모드\n\n"
        "   이름 변경 스타일 전환:\n"
        "   - 🏷️ 명령어 기반\n"
        "   - 🤖 자동 이름 변경 (/filters 추가 필수)\n\n"
        "`{{ queuecmd }}` - 이름 변경 대기열 확인 📊\n"
        "`{{ setcaptioncmd }}` - 팬시 캡션 설정 🎨\n"
        "`{{ helpcmd }}` - 이 마법 책! 📖\n"
        "`{{ pingcmd }}` - 핑-퐁! 🏓\n"
        "`{{ infocmd }}` - 봇 사양! 🤖\n"
        "`{{ profilecmd }}` - 여러분의 통계! 📈\n"
        "`{{ statuscmd }}` - 봇 생체 신호! 💓\n"
        "`{{ statscmd }}` - 글로벌 숫자! 🌍\n"
        "`{{ broadcastcmd }}` - 메가-공지! 📢\n"
        "`{{ leaderboardcmd }}` - 최고 사용자! 🏆\n"
        "`{{ setlanguagecmd }}` - 언어 변경! 🌐"
    )

    CURRENT_LOCALE = "🌍 **사용자 언어:** {{ user_locale }}"
