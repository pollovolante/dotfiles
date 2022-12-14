# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

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
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

group_names = [
    ("code", {"layout":"monadtall","label":"???"}),
    ("wifi", {"layout":"monadtall","label":"???"}),
    ("chat", {"layout":"monadtall","label":"???"}),
    ("misc", {"layout":"monadtall","label":"???"}),
    ("audio", {"layout":"monadtall","label":"???"}),
]

groups = [Group(name, **kwargs) for name,kwargs in group_names]

for i,(name,kwargs) in enumerate(group_names,1):
    keys.append(Key([mod],str(i),lazy.group[name].toscreen()))
    keys.append(Key([mod,'shift'],str(i),lazy.window.togroup(name)))

def init_colors():
    return [
        ["#ffffff","#ffffff"], #white
        ["#4ea9e5","#4ea9e5"], #main color
        ["#282a36","#282a36"], #background
        ["#484cef","#484cef"], #secondary color
    ]

colors = init_colors()

layouts_theme = {
    "border_width":2,
    "margin":8,
    "border_focus":colors[1],
    "border_normal":colors[2]
}
layouts = [
    layout.Columns(**layouts_theme),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(**layouts_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize=12,
    padding=2,
    background = colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    background = colors[2],
                    foreground  = colors[2],
                    linewidth = 0 ,
                    padding = 6
                ),
                widget.GroupBox(
                    font="FontAwesome",
                    fontsize = 10, 
                    margin_y = 0,
                    margin_x = 0,
                    padding_x = 5,
                    padding_y = 5,
                    borderwidth = 3,
                    active = colors[1],
                    inactive = colors[0],
                    rounded = False,
                    highlight_method='line',
                    this_current_screen_border = colors[1],
                    this_screen_border = colors[2],
                    other_current_screen_border =colors[2],
                    other_screen_border = colors[2],
                    foreground = colors[0],
                    background = colors[2]
                ),
                widget.Prompt(
                    foreground = colors[0],
                    background = colors[2]
                ),
                widget.WindowName(
                    foreground = colors[0],
                    background = colors[2]
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                    foreground = colors[0],
                    background = colors[2]
                ),
                widget.Systray(
                    foreground = colors[0],
                    background = colors[2]
                ),
                 widget.Sep(
                    background = colors[2],
                    foreground  = colors[2],
                    linewidth = 0,
                    padding = 10
                ),
                widget.Net(
                    font="FontAwesome",
                    interface = "wlan0",
                    format='???  {up} ??? {down}',
                    foreground = colors[1],
                    background = colors[2]
                ),
                widget.Sep(
                    background = colors[2],
                    foreground  = colors[2],
                    linewidth = 0 ,
                    padding = 6
                ),
                widget.CPU(
                    format='??? {load_percent}%',
                    update_interval = 2,
                    foreground = colors[0],
                    background = colors[2]
                ),
                widget.Bluetooth(
                    foreground = colors[0],
                    background = colors[2]
                ),
                widget.Sep(
                    background = colors[2],
                    foreground  = colors[2],
                    linewidth = 0 ,
                    padding = 6
                ),
                widget.Clock(
                    format="%B %d - %H:%M",
                    foreground = colors[1],
                    background = colors[2]
                ),
                widget.Sep(
                    background = colors[2],
                    foreground  = colors[2],
                    linewidth = 0 ,
                    padding = 6
                ),
                widget.QuickExit(
                    font="FontAwesome",
                    default_text = '???',
                    countdown_format ='??? {}',
                    foreground = colors[0],
                    background = colors[2]
                ),
                widget.CurrentLayout(
                    fmt= '[{}]',
                    background = colors[2],
                    foreground  = colors[1],
                ),
                widget.Sep(
                    background = colors[2],
                    foreground  = colors[2],
                    linewidth = 0 ,
                    padding = 6
                ),
            ],
            18
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
