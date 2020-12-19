from gi.repository import Gtk


def view_focus_tool(view):
    """This little tool ensures the view grabs focus when a mouse press or
    touch event happens."""
    gesture = Gtk.GestureSingle(widget=view)
    gesture.connect("begin", on_begin)
    return gesture


def on_begin(gesture, sequence):
    view = gesture.get_widget()
    if not view.is_focus():
        print("Grab me focus")
        view.grab_focus()
