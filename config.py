# ══════════════════════════════════════════════════════════════════
#  config.py  —  Edit ONLY this file before deploying
# ══════════════════════════════════════════════════════════════════

# ── Credentials (from https://my.telegram.org/apps) ──────────────
API_ID       = 123456            # ← your api_id   (integer)
API_HASH     = "your_api_hash"   # ← your api_hash (string)
SESSION_NAME = "forwarder"       # session file name (auto-created)

# ── Channel → Group mapping ───────────────────────────────────────
# Format: ("@source_channel", "@target_group")
# Use @username OR numeric ID like -1001234567890
CHANNEL_MAP = [
    ("@channel_one",    "@my_target_group"),
    ("@channel_two",    "@my_target_group"),
    ("@channel_three",  "@my_target_group"),
    ("@channel_four",   "@my_target_group"),
    ("@channel_five",   "@my_target_group"),
    ("@channel_six",    "@my_target_group"),
    ("@channel_seven",  "@my_target_group"),
    ("@channel_eight",  "@my_target_group"),
    ("@channel_nine",   "@my_target_group"),
    ("@channel_ten",    "@my_target_group"),
    # Add more rows as needed ↑
]

# ── Delay settings ────────────────────────────────────────────────
DELAY_BETWEEN_MESSAGES = 3    # seconds between each forwarded message
DELAY_ON_FLOOD_EXTRA   = 10   # extra sleep added on top of Telegram's FloodWait

# ── Bulk history mode ─────────────────────────────────────────────
# True  = forward ALL existing (old) messages first, then go live
# False = only forward NEW messages from now on
BULK_MODE  = True
BULK_LIMIT = 0     # 0 = unlimited; e.g. 500 = last 500 msgs per channel

# ── Media filters ─────────────────────────────────────────────────
FORWARD_PHOTOS    = True
FORWARD_VIDEOS    = True
FORWARD_DOCUMENTS = True
FORWARD_AUDIO     = True
FORWARD_STICKERS  = False

# ── Anonymous forwarding ──────────────────────────────────────────
# True  = no "Forwarded from …" tag shown
# False = keep original source attribution
ANONYMOUS = False
