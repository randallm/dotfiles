from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.manager import Drag, Click, Group, Key, Screen


##-> Theme + widget options
class Theme(object):
    bar = {
        'size': 24,
        'background': '15181a',
        }
    widget = {
        'font': 'Droid Sans',
        'fontsize': 11,
        'background': bar['background'],
        'foreground': 'eeeeee',
        }
    graph = {
        'background': '000000',
        'border_width': 0,
        'border_color': '000000',
        'line_width': 1,
        'margin_x': 0,
        'margin_y': 0,
        'width': 50,
        }

    groupbox = widget.copy()
    groupbox.update({
        'padding': 2,
        'borderwidth': 3,
        })

    sep = {
        'background': bar['background'],
        'foreground': '444444',
        'height_percent': 75,
        }

    systray = widget.copy()
    systray.update({
        'icon_size': 16,
        'padding': 3,
        })

keys = [
    Key(
        ["mod4"], "k",
        lazy.layout.down()
    ),
    Key(
        ["mod4"], "j",
        lazy.layout.up()
    ),
    Key(
        ["mod4", "control"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        ["mod4", "control"], "j",
        lazy.layout.shuffle_up()
    ),
    Key(
        ["mod4"], "space",
        lazy.layout.next()
    ),
    Key(
        ["mod4", "shift"], "space",
        lazy.layout.rotate()
    ),
    Key(
        ["mod4", "shift"], "Return",
        lazy.layout.toggle_split()
    ),
    Key(["mod4"], "h",      lazy.to_screen(1)),
    Key(["mod4"], "l",      lazy.to_screen(0)),
    Key(["mod4"], "Return", lazy.spawn("xterm")),
    Key(["mod4"], "d",      lazy.spawn("dmenu_run -b")),
    Key(["mod4"], "Tab",    lazy.nextlayout()),
    Key(["mod4"], "q",      lazy.window.kill()),
    Key(["mod4", "shift"], "q", lazy.window.kill()),

    Key(["mod4", "control"], "r", lazy.restart()),

    Key(["mod4"], "f",      lazy.window.toggle_fullscreen()),

]

groups = [
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
]
for i in groups:
    keys.append(
        Key(["mod4"], i.name, lazy.group[i.name].toscreen())
    )
    keys.append(
        Key(["mod4", "shift"], i.name, lazy.window.togroup(i.name))
    )

layouts = [
    layout.Max(),
    layout.Stack(stacks=2)
]

#@hook.subscribe.startup
#def runner():
#    import subprocess
#    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])
#    subprocess.Popen(['bitlbee'])


##-> Screens
screens = [
    Screen(
        top=bar.Bar(widgets=[
            widget.GroupBox(**Theme.groupbox),
            widget.WindowName(**Theme.widget),

            widget.CPUGraph(graph_color='18BAEB', fill_color='1667EB.3', **Theme.graph),
            widget.MemoryGraph(graph_color='00FE81', fill_color='00B25B.3', **Theme.graph),
            widget.NetGraph(graph_color='ffff00', fill_color='4d4d00', interface='wlan0', **Theme.graph),

            widget.CurrentLayout(**Theme.widget),
            widget.Systray(**Theme.systray),
            widget.Sep(**Theme.sep),
            widget.Clock(fmt='%a %d %b %I:%M %p', **Theme.widget),
            ], **Theme.bar),
    ),
]


# screens = [
#     Screen(
#         bottom = bar.Bar(
#                     [
#                         widget.GroupBox(),
#                         widget.WindowName(),
#                         widget.TextBox("default", "default config"),
#                         widget.Systray(),
#                         widget.Clock('%Y-%m-%d %a %I:%M %p'),
#                     ],
#                     30,
#                 ),
#     ),
# ]

main = None
follow_mouse_focus = True
cursor_warp = False
floating_layout = layout.Floating()
# mouse = ()

mouse = [
    # pop tile
    Drag(["mod1"], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    # resize float
    Drag(["mod1"], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    # show float
    Click(["mod1"], "Button2", lazy.window.bring_to_front()),
]