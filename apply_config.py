import json
from pathlib import Path

#---------------------------------------------------------------------------------------------------
# conditions
#---------------------------------------------------------------------------------------------------

# windows supported applications
BUNDLES_WINDOWS = [
    "^com\\.parallels\\.desktop\\.console$",
    "^com\\.vmware\\.horizon$",
    "^com\\.citrix\\.receiver\\.icaviewer\\.mac$",
    "^com\\.microsoft\\.rdc\\.macos$",
]

BUNDLES_EXCEPTS = BUNDLES_WINDOWS + [
    "^com\\.googlecode\\.iterm2$",
    "^com\\.mitchellh\\.ghostty$",
    "^com\\.jetbrains\\..*$",
    "^com\\.microsoft\\.VSCode$"
]

# mac-book keyboard
DEVICE_MACBOOK_KEYBOARD = [{"vendor_id": 1452, "product_id": 835}]


#---------------------------------------------------------------------------------------------------
# rules
#---------------------------------------------------------------------------------------------------

# switch input source
RULE_INPUT_SOURCE: dict = {
    "description": "(Right)Alt => F19(한/영) (입력소스 설정에서 단축키 F19 등록 필요)",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"optional": ["caps_lock"]}, "key_code": "right_command"},
            "to": [{"key_code": "f19", "repeat": False}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_WINDOWS}]
        }
    ]
}

# Windows keyboard
RULE_WINDOWS: dict = {
    "description": "Windows Keyboard on Mac :: Swap [⌘ and ⌥] & Allow [Screen Shot, Lock Screen]",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"optional": ["any"]}, "key_code": "left_command"},
            "to": [{"key_code": "left_option"}],
            "conditions": [{"type": "frontmost_application_if", "bundle_identifiers": BUNDLES_WINDOWS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"optional": ["any"]}, "key_code": "left_option"},
            "to": [{"key_code": "left_command"}],
            "conditions": [{"type": "frontmost_application_if", "bundle_identifiers": BUNDLES_WINDOWS}]
        },
        {
            "type": "basic",
            "from": {"key_code": "right_command"},
            "to": [{"key_code": "right_option"}],
            "conditions": [{"type": "frontmost_application_if", "bundle_identifiers": BUNDLES_WINDOWS}]
        },
        {
            "type": "basic",
            "from": {"key_code": "right_option"},
            "to": [{"key_code": "right_control"}],
            "conditions": [
                {"type": "frontmost_application_if", "bundle_identifiers": BUNDLES_WINDOWS},
                {"type": "device_if", "identifiers": DEVICE_MACBOOK_KEYBOARD}
            ]
        },
        {
            "type": "basic",
            "from": {"key_code": "right_option"},
            "to": [{"key_code": "application"}],
            "conditions": [
                {"type": "frontmost_application_if", "bundle_identifiers": BUNDLES_WINDOWS},
                {"type": "device_unless", "identifiers": DEVICE_MACBOOK_KEYBOARD}
            ]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["left_shift", "left_option"], "optional": ["left_control", "caps_lock"]}, "key_code": "4"},
            "to": [{"modifiers": ["left_shift", "left_command"], "key_code": "4"}],
            "conditions": [{"type": "frontmost_application_if", "bundle_identifiers": BUNDLES_WINDOWS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["left_control", "left_option"], "optional": ["caps_lock"]}, "key_code": "q"},
            "to": [{"modifiers": ["left_control", "left_command"], "key_code": "q"}],
            "conditions": [{"type": "frontmost_application_if", "bundle_identifiers": BUNDLES_WINDOWS}]
        }
    ]
}

# ^N, ^S, ^F
RULE_FILE: dict = {
    "description": "Ctrl+[N, S, F] => ⌘N (New), ⌘S (Save), ⌘F (Find)",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "n"},
            "to": [{"modifiers": ["left_command"], "key_code": "n"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "s"},
            "to": [{"modifiers": ["left_command"], "key_code": "s"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "f"},
            "to": [{"modifiers": ["left_command"], "key_code": "f"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        }
    ]
}

# ^A, ^C, ^V, ^X, ^Z, ^Y
RULE_EDIT: dict = {
    "description": "Ctrl+[A, C, V, X, Z, Y] => ⌘A (Select All), ⌘C (Copy), ⌘V (Paste), ⌘X (cut), ⌘Z (Undo), ⇧⌘Z (redo)",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "a"},
            "to": [{"modifiers": ["left_command"], "key_code": "a"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "c"},
            "to": [{"modifiers": ["left_command"], "key_code": "c"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "v"},
            "to": [{"modifiers": ["left_command"], "key_code": "v"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "x"},
            "to": [{"modifiers": ["left_command"], "key_code": "x"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "z"},
            "to": [{"modifiers": ["left_command"], "key_code": "z"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "y"},
            "to": [{"modifiers": ["left_command", "left_shift"], "key_code": "z"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        }
    ]
}

# Home, End
RULE_HOME_END: dict = {
    "description": "Home, End => ⌘← (Begin of Line), ⌘→ (End of Line) / Ctrl+[Home, End] => Home, End",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"optional": ["caps_lock", "shift"]}, "key_code": "home"},
            "to": [{"modifiers": ["left_command"], "key_code": "left_arrow"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"optional": ["caps_lock", "shift"]}, "key_code": "end"},
            "to": [{"modifiers": ["left_command"], "key_code": "right_arrow"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "home"},
            "to": [{"key_code": "home"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "end"},
            "to": [{"key_code": "end"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        }
    ]
}

# Left, Right, Up, Down
RULE_ARROW: dict = {
    "description": "Ctrl+[Left, Right, Up, Down] => ⌥[←, →], ⌃[PageUp, PageDown]",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock", "shift"]},
                     "key_code": "left_arrow"},
            "to": [{"modifiers": ["left_option"], "key_code": "left_arrow"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock", "shift"]},
                     "key_code": "right_arrow"},
            "to": [{"modifiers": ["left_option"], "key_code": "right_arrow"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "up_arrow"},
            "to": [{"modifiers": ["left_control"], "key_code": "page_up"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock"]}, "key_code": "down_arrow"},
            "to": [{"modifiers": ["left_control"], "key_code": "page_down"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        }
    ]
}


#---------------------------------------------------------------------------------------------------
# apply
#---------------------------------------------------------------------------------------------------

keymaps: dict = {
    "title": "xunyss key mapping",
    "rules": [
        # apply "using Windows-like key mappings"
        #RULE_INPUT_SOURCE, RULE_WINDOWS, RULE_FILE, RULE_EDIT, RULE_HOME_END, RULE_ARROW
        # apply "using Mac key mappings"
        RULE_INPUT_SOURCE, RULE_WINDOWS
    ]
}

conf_path = Path.home() / ".config/karabiner/assets/complex_modifications/xunyss_keys.json"
json.dump(keymaps, open(conf_path, "w"), ensure_ascii=False, indent=4)
print(f"karabiner configs updated: '{conf_path}'")

