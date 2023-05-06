class Selectors:
    QR_CODE = 'div[data-testid="qrcode"]'

    ANIMATING = 'div.app-animating'

    MESSAGE_BOX = 'div[data-testid="conversation-compose-box-input"]'
    SEND_BUTTON = 'div[aria-label="Send"]'

    SEARCH_BAR = 'div[data-testid="chat-list-search"]'
    SEARCH_BAR_CLEAR = 'button[aria-label="Cancel search"]'

    INFO_DRAWER = 'div[data-testid="chat-info-drawer"]'
    CURRENT_CHAT = 'span[data-testid="conversation-info-header-chat-title"]'

    CONVERSATION_HEADER = 'header[data-testid="conversation-header"]'
    CONVERSATION_MESSAGES = 'div.message-in div[data-testid="msg-container"]'

    CHAT_INPUT = 'div[data-testid="conversation-compose-box-input"]'
    CHAT_INFO_TEXT = INFO_DRAWER + ' span[dir="auto"].copyable-text.selectable-text'
    CHAT_INFO_PIC = INFO_DRAWER + ' section > div img'
    CHAT_DEFAULT_PIC = INFO_DRAWER + ' span[data-testid="default-user"]'

    GROUP_SUBJECT = INFO_DRAWER + ' div[data-testid="group-info-drawer-subject-input"]'
    GROUP_PARTICIPANTS = INFO_DRAWER + ' div[data-testid="group-info-top-card-subtitle"] > span > span > button'
    GROUP_INFO_PIC = CHAT_INFO_PIC
    GROUP_DEFAULT_PIC = INFO_DRAWER + ' span[data-testid="default-group"]'
    GROUP_DESCRIPTION = INFO_DRAWER + ' span[data-testid="group-info-drawer-description-title-input-read-only"]'
    GROUP_READ_MORE = GROUP_DESCRIPTION + ' + button'

    UNREAD_BADGE = 'span[data-testid="icon-unread-count"]'
    UNREAD_TITLE = 'div[data-testid="cell-frame-title"] > span'
    UNREAD_LAST_MESSAGE = 'span[data-testid="last-msg-status"]'
    UNREAD_CONVERSATIONS_XPATH = '//span[@data-testid="icon-unread-count"]/ancestor::div[@data-testid="cell-frame-container"]'

    MY_PROFILE_TEXT = 'div[data-testid="drawer-left"] span[data-testid="col-main-profile-input-read-only"]'
    MY_PROFILE_PIC = 'div[data-testid="profile-pic-picker"] img'
    MY_PROFILE_DEFAULT_PIC = 'div[data-testid="profile-pic-picker"] span[data-testid="default-user"]'

    MEDIA_CAPTION = 'div[data-testid="media-caption-input-container"]'

    ATTATCHMENT_MENU = 'div[data-testid="conversation-clip"] > div'
    INPUT_DOCUMENTS = 'span[data-testid="attach-document"] + input'
    INPUT_MIDIA = 'span[data-testid="attach-image"] + input'
