from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.manager import Drag, Click, Group, Key, Screen
import socket


##-> Theme + widget options
class Theme(object):
    bar = {
        'size': 24,
        'background': '15181a',
        }

    if socket.gethostname() == 'skynet':
        widget = {
            'font': 'Droid Sans',
            'fontsize': 11,
            'background': bar['background'],
            'foreground': 'eeeeee',
         }
    else:
        widget = {
            'font': 'Droid Sans',
            'fontsize': 13,
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
        'background': bar['background'],
        'icon_size': 24,
        'padding': 0,
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
        ["mod4", "shift"], "k",
        lazy.layout.shuffle_down()
    ),
    Key(
        ["mod4", "shift"], "j",
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

    Key(
        ["mod4", "shift"], "Tab",
        lazy.layout.client_to_next()
    ),

    Key(["mod4"], "m",      lazy.window.toggle_minimize()),
    Key(["mod4"], "n",      lazy.window.disable_minimize()),

    Key(["mod4"], "h",      lazy.to_screen(1)),
    Key(["mod4"], "l",      lazy.to_screen(0)),
    Key(["mod4"], "Return", lazy.spawn("xterm")),
    Key(["mod4"], "d",      lazy.spawn("dmenu_run -b")),
    Key(["mod4"], "Tab",    lazy.nextlayout()),

    Key(["mod4"], "q",      lazy.window.kill()),
    Key(["mod4", "shift"], "q", lazy.window.kill()),

    Key(["mod4", "control"], "r", lazy.restart()),

    Key(["mod4"], "f",      lazy.window.toggle_fullscreen()),

    Key(["mod4"], "t",      lazy.window.toggle_floating()),

    Key(["mod4"], "Left",   lazy.window.move_floating(-35, 0)),
    Key(["mod4"], "Right",  lazy.window.move_floating(35, 0)),
    Key(["mod4", "control"], "Left",    lazy.window.move_floating(-960, 0)),  # 1920 / 2
    Key(["mod4", "control"], "Right",   lazy.window.move_floating(960, 0)),
    Key(["mod4"], "Up",     lazy.window.move_floating(0, -35)),
    Key(["mod4"], "Down",   lazy.window.move_floating(0, 35)),

    Key(["mod4", "shift"], "Left",  lazy.window.resize_floating(-35, 0)),
    Key(["mod4", "shift"], "Right",  lazy.window.resize_floating(35, 0)),
    Key(["mod4", "shift"], "Up",  lazy.window.resize_floating(0, -35)),
    Key(["mod4", "shift"], "Down",  lazy.window.resize_floating(0, 35)),

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

##-> Screens
if socket.gethostname() == 'manbearpig':
    screens = [
        Screen(
            top=bar.Bar(widgets=[
                widget.GroupBox(**Theme.groupbox),
                widget.WindowName(**Theme.widget),

                widget.CPUGraph(graph_color='18BAEB', fill_color='1667EB.3', **Theme.graph),
                widget.MemoryGraph(graph_color='00FE81', fill_color='00B25B.3', **Theme.graph),
                widget.NetGraph(graph_color='ffff00', fill_color='4d4d00',
                    interface='eth0', **Theme.graph),

                widget.CurrentLayout(**Theme.widget),
                widget.Systray(**Theme.systray),
                widget.Sep(**Theme.sep),
                widget.Clock(fmt='%a %d %b %I:%M %p', **Theme.widget),
                ], **Theme.bar),
        ),
    ]
else:
    screens = [
        Screen(
            top=bar.Bar(widgets=[
                widget.GroupBox(**Theme.groupbox),
                widget.WindowName(**Theme.widget),

                widget.CPUGraph(graph_color='18BAEB', fill_color='1667EB.3', **Theme.graph),
                widget.MemoryGraph(graph_color='00FE81', fill_color='00B25B.3', **Theme.graph),
                widget.NetGraph(graph_color='ffff00', fill_color='4d4d00',
                    interface='wlan0', **Theme.graph),

                widget.CurrentLayout(**Theme.widget),
                widget.Systray(**Theme.systray),
                widget.Sep(**Theme.sep),
                widget.Clock(fmt='%a %d %b %I:%M %p', **Theme.widget),
                ], **Theme.bar),
        ),
    ]

main = None
follow_mouse_focus = True
cursor_warp = False
floating_layout = layout.Floating()

#mouse = [
#    # pop tile
#    Drag(["mod1"], "Button1", lazy.window.set_position_floating(),
#         start=lazy.window.get_position()),
#    # resize float
#    Drag(["mod1"], "Button3", lazy.window.set_size_floating(),
#         start=lazy.window.get_size()),
#    # show float
#    Click(["mod1"], "Button2", lazy.window.bring_to_front()),
#]

floating_layout = layout.floating.Floating(float_rules=[{'wmclass': x} for x in (
    'Xephyr',
    'wine',
    'winecfg',
    'orage',
    'Dorado.exe',
    'winmine.exe',
    'hl2.exe',
    'steam.exe',
    'dota.exe',
    'csgo.exe',
    'left4dead2.exe',
    )])


@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


@hook.subscribe.startup
def runner():
    import subprocess
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])
