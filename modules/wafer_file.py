# -*- coding: utf-8 -*-
"""
Provides examples on how to use the ``wafer_map`` package.

This module is called when running ``python -m wafer_map``.
"""
# ---------------------------------------------------------------------------
### Imports
# ---------------------------------------------------------------------------
# Standard Library
from __future__ import absolute_import, division, print_function, unicode_literals

# Third-Party
import wx
import os
# Package/Application

from wafer_map import wm_core
from wafer_map import wm_app
from wafer_map import gen_fake_data
from wafer_map.wm_constants import DataType


__author__ = "Douglas Thor"
__version__ = "v0.4.0"


def WaferFile(self, xyd, wafer_info):
    def __init__(self, path_to_file):
        
        self.error = False
        self.error_message = ""
        self.path_to_file = path_to_file
        self.filename = os.path.basename(self.path_to_file)
        self.mode_types = ["py","ppg"]
        self.mode_type = self.filename.split(".")[-1] 
        # wafer size mm & thickness
        self.wafer_size_inch = 0
        self.wafer_size_mm = 0
        self.thickness = 0

        self.number_lines = 0
        self.wafer_parameters = {} # init dict wafer parameters
        # init initial movement (for ppg files) for get the origin chip
        self.movement_x = 0
        self.movement_y = 0
        # get movement in ppg file to adjust wafer_positions
        self.wafer_movements = dict()

        """
        Example of running wafer_map as a standalone application.

        All you need to do once you have your data in the correct format is
        to call ``wm_app.WaferMapApp`` with your keyword arguments
        which define the wafer and die parameters such as die size, the wafer
        diameter, and the edge exclusion.

        Parameters
        ----------
        xyd : list of 3-tuples
            The data to plot.
        wafer_info : :class:`wafer_map.wm_info.WaferInfo`
            The wafer information such as die size, diameter, etc.

        Notes
        -----
        The ``xyd`` values need to have this format::

            [(grid_x_1, grid_y_1, data_1), (grid_x_2, grid_y_2, data_2), ..., ]
        """
        wm_app.WaferMapApp(xyd,
                            wafer_info.self.wafer_parameters["wafer_size"],
                            wafer_info.self.wafer_parameters["home_chip"],
                            wafer_info.dia,
                            wafer_info.edge_excl,
                            wafer_info.self.wafer_parameters["flat_orientation"],
                            )


def add_to_existing_app(xyd, wafer_info):
    """
    Example of adding the wafer map to your existing wxPython application.
S
    To add a wafer map to an existing application, instance the
    ``wm_core.WaferMapPanel()`` class with your data and wafer info. The
    wafer info must be a ``wm_info.WaferInfo`` object.

    Parameters
    ----------
    xyd : list of 3-tuples
        The data to plot.
    wafer_info : :class:`wafer_map.wm_info.WaferInfo`
        The wafer information such as die size, diameter, etc.
    """
    app = wx.App()

    class ExampleFrame(wx.Frame):
        """Base Frame."""

        def __init__(self, title, xyd, wafer_info):
            wx.Frame.__init__(self,
                              None,                         # Window Parent
                              wx.ID_ANY,                    # id
                              title=title,                  # Window Title
                              size=(600 + 16, 500 + 38),    # Size in px
                              )
            self.xyd = xyd
            self.wafer_info = wafer_info

            # Add a status bar if you want to
            self.CreateStatusBar()

            # Bind events
            self.Bind(wx.EVT_CLOSE, self.OnQuit)

            # Create some other dummy stuff for the example
            self.listbox = wx.ListBox(self,
                                      wx.ID_ANY,
                                      choices=['A', 'B', 'C', 'D'],
                                      )
            self.button = wx.Button(self, wx.ID_ANY, label="Big Button!")

            # Create the wafer map
            self.panel = wm_core.WaferMapPanel(self,
                                               self.xyd,
                                               self.wafer_info,
                                               show_die_gridlines=False,
                                               )

            # set our layout
            self.hbox = wx.BoxSizer(wx.HORIZONTAL)
            self.vbox = wx.BoxSizer(wx.VERTICAL)

            self.vbox.Add(self.panel, 3, wx.EXPAND)
            self.vbox.Add(self.button, 1, wx.EXPAND)
            self.hbox.Add(self.listbox, 1, wx.EXPAND)
            self.hbox.Add(self.vbox, 3, wx.EXPAND)
            self.SetSizer(self.hbox)

        def OnQuit(self, event):
            self.Destroy()

    frame = ExampleFrame("Called as a panel in your own app!", xyd, wafer_info)
    frame.Show()
    app.MainLoop()


def discrete_data_example(xyd, wafer_info):
    """
    Example of plotting discrete data using the standalone app version.

    Plotting discrete data is the same as continuous data, but you need to
    add the ``data_type`` argument to the class initialization.

    Parameters
    ----------
    xyd : list of 3-tuples
        The data to plot.
    wafer_info : :class:`wafer_map.wm_info.WaferInfo`
        The wafer information such as die size, diameter, etc.
    """
    import random
    bins = ["Bin1", "Bin1", "Bin1", "Bin2", "Dragons", "Bin1", "Bin2"]
    discrete_xyd = [(_x, _y, random.choice(bins))
                    for _x, _y, _
                    in xyd]

    wm_app.WaferMapApp(discrete_xyd,
                       wafer_info.die_size,
                       wafer_info.center_xy,
                       wafer_info.dia,
                       wafer_info.edge_excl,
                       wafer_info.flat_excl,
                       data_type=DataType.DISCRETE,
                       show_die_gridlines=False,
                       )


def main():
    """Run when called as a module."""
    # Generate some fake data
    wafer_info, xyd = gen_fake_data.generate_fake_data()

    WaferFile(xyd, wafer_info)
    add_to_existing_app(xyd, wafer_info)
    discrete_data_example(xyd, wafer_info)

if __name__ == "__main__":
    main()
