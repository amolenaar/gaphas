from gi.repository import Gtk


class RubberbandState:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x0 = self.y0 = self.x1 = self.y1 = 0


class RubberbandPainter:
    def __init__(self, rubberband_state):
        self.rubberband_state = rubberband_state

    def paint(self, _items, cairo):
        data = self.rubberband_state
        x0, y0, x1, y1 = data.x0, data.y0, data.x1, data.y1
        if x0 != x1 or y0 != y1:
            cairo.rectangle(min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0))
            cairo.set_source_rgba(0.9, 0.9, 0.9, 0.3)
            cairo.fill_preserve()
            cairo.set_line_width(2.0)
            cairo.set_dash((7.0, 5.0), 0)
            cairo.set_source_rgba(0.5, 0.5, 0.7, 0.7)
            cairo.stroke()


def on_drag_begin(gesture, start_x, start_y, view, rubberband_state):
    if gesture.set_state(Gtk.EventSequenceState.CLAIMED):
        rubberband_state.x0 = rubberband_state.x1 = start_x
        rubberband_state.y0 = rubberband_state.y1 = start_y
        print("rubberband", gesture.get_sequences())


def on_drag_update(gesture, offset_x, offset_y, view, rubberband_state):
    rubberband_state.x1 = rubberband_state.x0 + offset_x
    rubberband_state.y1 = rubberband_state.y0 + offset_y
    view.queue_redraw()


def on_drag_end(gesture, offset_x, offset_y, view, rubberband_state):
    x0 = rubberband_state.x0
    y0 = rubberband_state.y0
    x1 = x0 + offset_x
    y1 = y0 + offset_y
    items = view.get_items_in_rectangle(
        (min(x0, x1), min(y0, y1), abs(x1 - x0), abs(y1 - y0)), contain=True
    )
    view.selection.select_items(*items)
    rubberband_state.reset()
    view.queue_redraw()


def rubberband_tool(view, rubberband_state):
    gesture = Gtk.GestureDrag.new(view)
    gesture.connect("drag-begin", on_drag_begin, view, rubberband_state)
    gesture.connect("drag-update", on_drag_update, view, rubberband_state)
    gesture.connect("drag-end", on_drag_end, view, rubberband_state)
    return gesture
