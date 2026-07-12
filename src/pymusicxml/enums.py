"""
Module containing relevant Enums used throughout pymusicxml.
"""

#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  #
#  This file is part of SCAMP (Suite for Computer-Assisted Music in Python)                      #
#  Copyright © 2020 Marc Evanstein <marc@marcevanstein.com>.                                     #
#                                                                                                #
#  This program is free software: you can redistribute it and/or modify it under the terms of    #
#  the GNU General Public License as published by the Free Software Foundation, either version   #
#  3 of the License, or (at your option) any later version.                                      #
#                                                                                                #
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;     #
#  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.     #
#  See the GNU General Public License for more details.                                          #
#                                                                                                #
#  You should have received a copy of the GNU General Public License along with this program.    #
#  If not, see <http://www.gnu.org/licenses/>.                                                   #
#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  #

from enum import Enum


class LineEnd(Enum):
    """
    The hook drawn at the end of a bracket or dashed line spanner: a vertical hook pointing up or down,
    hooks at both ends, an arrowhead, or no hook at all.
    """

    up = "up"
    down = "down"
    both = "both"
    arrow = "arrow"
    none = "none"


class LineType(Enum):
    """The style of line drawn by a spanner, such as a bracket or a dashed line."""

    solid = "solid"
    dashed = "dashed"
    dotted = "dotted"
    wavy = "wavy"


class HairpinType(Enum):
    """Whether a hairpin spanner opens outward (crescendo) or closes inward (diminuendo)."""

    crescendo = "crescendo"
    diminuendo = "diminuendo"


class StaffPlacement(Enum):
    """Whether a direction or notation is placed above or below the staff."""

    above = "above"
    below = "below"


class ArpeggiationDirection(Enum):
    """The direction in which an arpeggiated chord is rolled."""

    up = "up"
    down = "down"


class AccidentalType(Enum):
    """
    An accidental, as used in a :class:`~pymusicxml.score_components.NonTraditionalKeySignature`. Note that
    `flat_flat` and `double_flat` are two names for the same MusicXML value.
    """

    flat_flat = "flat-flat"
    double_flat = "flat-flat"
    flat = "flat"
    natural = "natural"
    sharp = "sharp"
    double_sharp = "double-sharp"
