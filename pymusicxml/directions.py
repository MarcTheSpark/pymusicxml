"""
Module containing all non-spanner subclasses of the :class:`~pymusicxml.score_components.Direction` type.
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

from typing import Union, Sequence
from xml.etree import ElementTree
from pymusicxml.enums import StaffPlacement
from pymusicxml.score_components import Duration, Direction


class MetronomeMark(Direction):

    """
    Class representing a tempo-specifying metronome mark

    :param beat_length: length, in quarters, of the note that takes the beat
    :param bpm: beats per minute
    :param voice: Which voice to attach to
    :param staff: Which staff to attach to if the part has multiple staves
    :param placement: Where to place the direction in relation to the staff ("above" or "below")
    :param other_attributes: any other attributes to assign to the metronome mark, e.g. parentheses="yes" or
        font_size="5"
    """

    def __init__(self, beat_length: float, bpm: float, placement: Union[str, StaffPlacement] = "above",
                 voice: int = 1, staff: int = None, **other_attributes):
        super().__init__(placement, voice, staff)
        try:
            self.beat_unit = Duration.from_written_length(beat_length)
        except ValueError:
            # fall back to quarter note tempo if the beat length is not expressible as a single notehead
            self.beat_unit = Duration.from_written_length(1.0)
            bpm /= beat_length
        self.bpm = bpm
        self.other_attributes = {key.replace("_", "-"): value for key, value in other_attributes.items()}

    def render_direction_type(self) -> Sequence[ElementTree.Element]:
        type_el = ElementTree.Element("direction-type")
        metronome_el = ElementTree.SubElement(type_el, "metronome", self.other_attributes)
        metronome_el.extend(self.beat_unit.render_to_beat_unit_tags())
        ElementTree.SubElement(metronome_el, "per-minute").text = str(self.bpm)
        return type_el,


class TextAnnotation(Direction):
    """
    Class representing text that is attached to the staff

    :param text: the text of the annotation
    :param font_size: the font size of the text
    :param italic: whether or not the text is italicized
    :param placement: Where to place the direction in relation to the staff ("above" or "below")
    :param voice: Which voice to attach to
    :param staff: Which staff to attach to if the part has multiple staves
    :param kwargs: any extra properties of the musicXML "words" tag aside from font-size and italics can be
        passed to kwargs
    """

    def __init__(self, text: str, font_size: float = None, italic: bool = False, bold: bool = False,
                 placement: Union[str, StaffPlacement] = "above", voice: int = 1, staff: int = None, **kwargs):
        super().__init__(placement, voice, staff)
        self.text = text
        self.text_properties = kwargs
        if font_size is not None:
            self.text_properties["font-size"] = font_size
        if italic:
            self.text_properties["font-style"] = "italic"
        if bold:
            self.text_properties["font-weight"] = "bold"

    def render_direction_type(self) -> Sequence[ElementTree.Element]:
        type_el = ElementTree.Element("direction-type")
        ElementTree.SubElement(type_el, "words", self.text_properties).text = self.text
        return type_el,


class Dynamic(Direction):
    """
    Class representing a dynamic that is attached to the staff

    :param dynamic_text: the text of the dynamic, e.g. "mf"
    :param voice: Which voice to attach to
    :param staff: Which staff to attach to if the part has multiple staves
    """

    STANDARD_TYPES = ("f", "ff", "fff", "ffff", "fffff", "ffffff", "fp", "fz", "mf", "mp", "p", "pp", "ppp", "pppp",
                      "ppppp", "pppppp", "rf", "rfz", "sf", "sffz", "sfp", "sfpp", "sfz")

    def __init__(self, dynamic_text: str, placement: Union[str, StaffPlacement] = "below",
                 voice: int = 1, staff: int = None):
        self.dynamic_text = dynamic_text
        super().__init__(placement, voice, staff)

    def render_direction_type(self) -> Sequence[ElementTree.Element]:
        type_el = ElementTree.Element("direction-type")
        dynamics_el = ElementTree.SubElement(type_el, "dynamics")
        if self.dynamic_text in Dynamic.STANDARD_TYPES:
            ElementTree.SubElement(dynamics_el, self.dynamic_text)
        else:
            ElementTree.SubElement(dynamics_el, "other-dynamics").text = self.dynamic_text
        return type_el,
