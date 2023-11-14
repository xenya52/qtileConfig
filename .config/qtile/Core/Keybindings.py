# ██╗  ██╗███████╗██╗   ██╗███████╗
# ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝
# █████╔╝ █████╗   ╚████╔╝ ███████╗
# ██╔═██╗ ██╔══╝    ╚██╔╝  ╚════██║
# ██║  ██╗███████╗   ██║   ███████║
# ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.command import lazy

from Core.Groups import groups

mod = "mod4"
terminal = "kitty"
browser = "firefox"
notes = "obsidian"
code = "code"
calculator = "qalculate-gtk"
rofi = "rofi -show drun"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    ############## Own config
    Key([mod], "F5", lazy.spawn("pactl -- set-sink-volume 0 -5%")),
    Key([mod], "F6", lazy.spawn("pactl -- set-sink-volume 0 +5%")),
    Key([mod], "F8", lazy.spawn("xbacklight -dec 5")),
    Key([mod], "F9", lazy.spawn("xbacklight -inc 5")),
    Key([mod], "f", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "o", lazy.spawn(notes), desc="Launch obsidian"),
    Key([mod], "c", lazy.spawn(code), desc="Launch vsCode"),
    Key([mod], "x", lazy.spawn(calculator), desc="Launch calculator"),
    #############
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod, "contrrol"], "q", lazy.spawn(lock), desc ="Locking you screen"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),
    #Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
    ]
)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]