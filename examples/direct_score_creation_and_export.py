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

from pymusicxml import *


Score([
    PartGroup([
        Part("Oboe", [
            Measure([
                Chord(["G#4", "b4", "d5"], 1.5, notations=StartMultiGliss((None, 1, 2))),
                GraceChord(["C5", "eb5", "G5"], 0.5, stemless=True, notations=StopMultiGliss((1, None, 2))),
                BeamedGroup([
                    Note("f#4", 0.25),
                    Note("A#4", 0.25)
                ]),
                Chord(["Cs4", "Ab4"], 1.0),
                Rest(1.0)
            ], time_signature=(4, 4), directions_with_displacements=[
                (MetronomeMark(1.5, 80), 0),
                (TextAnnotation("rit.", italic=True), 1.0),
                (MetronomeMark(1.0, 60), 3.5)
            ]),
            Measure([
                Tuplet([
                    Note("c5", 0.5),
                    Note("bb4", 0.25),
                    Note("a4", 0.25),
                    Note("b4", 0.25),
                ], (5, 4)),
                Note("f4", 2, directions=TextAnnotation("with gusto!")),
                Rest(1)
            ], clef="mezzo-soprano", barline="end")
        ]),
        Part("Clarinet", [
            Measure([
                Tuplet([
                    Note("c5", 0.5),
                    Note("bb4", 0.25, notehead="x"),
                    Note("a4", 0.25),
                    Note("b4", 0.25),
                ], (5, 4)),
                Note("f4", 2),
                Rest(1)
            ], time_signature=(4, 4)),
            Measure([
                Note("d5", 1.5, directions=[StartBracket(text="roguishly")]),
                BeamedGroup([
                    Note("f#4", 0.25),
                    Note("A#4", 0.25)
                ]),
                Chord(["Cs4", "Ab4"], 1.0, directions=[StopBracket(line_end="down")]),
                Rest(1.0)
            ], barline="end")
        ])
    ]),
    Part("Bassoon", [
        Measure([
            BarRest(4, directions=[StartPedal()])
        ], time_signature=(4, 4), clef="bass"),
        Measure([
            [
                BeamedGroup([
                    Rest(0.5),
                    Note("d4", 0.5, notehead="open mi", notations=[StartGliss(1), StartSlur()]),
                    Note("Eb4", 0.5, notations=[StopGliss(1), StartGliss(2)]),
                    Note("F4", 0.5, notations=[StopGliss(2), StopSlur()]),
                ]),
                Note("Eb4", 2.0)
            ],
            None,
            [
                Rest(1.0),
                Note("c4", 2.0),
                Note("Eb3", 0.5, directions=StopPedal()),
                Rest(0.5)
            ]
        ], barline="end")
    ])
], title="Directly Created MusicXML", composer="HTMLvis").export_to_file("DirectExample.musicxml")
