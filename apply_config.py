import json
from pathlib import Path


#---------------------------------------------------------------------------------------------------
# conditions
#---------------------------------------------------------------------------------------------------

# Windows-supported applications
BUNDLES_WINDOWS = [
    "^com\\.parallels\\.desktop\\.console$",
    "^com\\.vmware\\.horizon$",
    "^com\\.citrix\\.receiver\\.icaviewer\\.mac$",
    "^com\\.microsoft\\.rdc\\.macos$",
]

BUNDLES_EXCEPTS = BUNDLES_WINDOWS + [
    "^com\\.googlecode\\.iterm2$",
    "^com\\.mitchellh\\.ghostty$",
    "^dev\\.warp\\.Warp-Stable$",
    "^com\\.jetbrains\\..*$",
]


#---------------------------------------------------------------------------------------------------
# devices
#---------------------------------------------------------------------------------------------------

# MacBook internal keyboard
DEVICE_MACBOOK_KEYBOARD = [{ "is_built_in_keyboard": True }]

# KeyChron k8
DEVICE_KEYCHRON_K8 = [{ "vendor_id": 1452, "product_id": 591 }]

# AURORA 80
DEVICE_AURORA_80 = [{ "vendor_id": 14000, "product_id": 12292 }]

# RS 8
DEVICE_RS_8 = [{ "vendor_id": 14000, "product_id": 12293 }]


#---------------------------------------------------------------------------------------------------
# rules
#---------------------------------------------------------------------------------------------------

# switch input source
RULE_INPUT_SOURCE: dict = {
    "description": "Input Source :: Right ⌘ => F19 (Set F19 as the Input Source shortcut)",
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
    "description": "Windows on Mac :: Swap [⌘ and ⌥] & Allow [Screen Shot, Lock Screen]",
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
    "description": "Ctrl+[A, C, V, X, Z, Y] => ⌘A (Select All), ⌘C (Copy), ⌘V (Paste), ⌘X (Cut), ⌘Z (Undo), ⇧⌘Z (Redo)",
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
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock", "shift"]}, "key_code": "left_arrow"},
            "to": [{"modifiers": ["left_option"], "key_code": "left_arrow"}],
            "conditions": [{"type": "frontmost_application_unless", "bundle_identifiers": BUNDLES_EXCEPTS}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["control"], "optional": ["caps_lock", "shift"]}, "key_code": "right_arrow"},
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
# keyboards
#---------------------------------------------------------------------------------------------------

# KeyChron k8
RULE_KEYCHRON_K8: dict = {
    "description": "Keyboard [KeyChron-K8] :: 'Mic' key => ⌘space (Spotlight)",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"mandatory": ["fn"], "optional": ["caps_lock"] }, "key_code": "spacebar"},
            "to": [{"modifiers": ["left_command"], "key_code": "spacebar"}],
            "conditions": [{"type": "device_if", "identifiers": DEVICE_KEYCHRON_K8}]
        }
    ]
}

# RS 8
RULE_RS_8: dict = {
    "description": "Keyboard [RS-8] :: MissionControl (F13), LaunchPad (F14)",
    "manipulators": [
        {
            "type": "basic",
            "from": {"modifiers": {"optional": ["any"]}, "key_code": "f13"},
            "to": [{"apple_vendor_keyboard_key_code": "mission_control"}],
            "conditions": [{"type": "device_if", "identifiers": DEVICE_RS_8}]
        },
        {
            "type": "basic",
            "from": {"modifiers": {"optional": ["any"]}, "key_code": "f14"},
            "to": [{"apple_vendor_keyboard_key_code": "launchpad"}],
            "conditions": [{"type": "device_if", "identifiers": DEVICE_RS_8}]
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
        #RULE_INPUT_SOURCE, RULE_WINDOWS, RULE_KEYCHRON_K8
        RULE_INPUT_SOURCE, RULE_WINDOWS, RULE_RS_8
    ]
}

conf_path = Path.home() / ".config/karabiner/assets/complex_modifications/xunyss_keys.json"
json.dump(keymaps, open(conf_path, "w"), ensure_ascii=False, indent=4)
print(f"karabiner configs updated: '{conf_path}'")

