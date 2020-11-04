"""Tools provide interactive behavior to a `View` by handling specific events
sent by view.

Some of implemented tools are

`HoverTool`
    make the item under the mouse cursor the "hovered item"

`ItemTool`
    handle selection and movement of items

`HandleTool`
    handle selection and movement of handles

`RubberbandTool`
    for rubber band selection of multiple items

`PanTool`
    for easily moving the canvas around

`PlacementTool`
    for placing items on the canvas

The tools are chained with `ToolChain` class (it is a tool as well),
which allows to combine functionality provided by different tools.

Tools can handle events in different ways

- event can be ignored
- tool can handle the event (obviously)
"""
from gaphas.tool.handletool import ConnectHandleTool, HandleTool
from gaphas.tool.hover import HoverTool
from gaphas.tool.itemtool import ItemTool
from gaphas.tool.pan import PanTool
from gaphas.tool.placement import PlacementTool
from gaphas.tool.rubberband import RubberbandTool
from gaphas.tool.textedit import TextEditTool
from gaphas.tool.tool import Tool
from gaphas.tool.toolchain import ToolChain
from gaphas.tool.zoom import ZoomTool


def DefaultTool(view=None):
    """The default tool chain build from HoverTool, ItemTool and HandleTool."""
    return (
        ToolChain(view)
        .append(HoverTool())
        .append(ConnectHandleTool())
        .append(PanTool())
        .append(ZoomTool())
        .append(ItemTool())
        .append(TextEditTool())
        .append(RubberbandTool())
    )