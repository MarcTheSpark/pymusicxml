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
from random import choice, choices

score = Score(title="Algorithmically Generated MusicXML", composer="HTMLvis")
part = Part("Piano")
score.append(part)

pitch_bank = ["f#4", "bb4", "d5", "e5", "ab5", "c6", "f6"]

measures = []

for i in range(20):
    m = Measure(time_signature=(3, 4) if i == 0 else None)
    for beat_num in range(3):
        if (i + beat_num) % 3 == 0:
            # one quarter note triad
            m.append(Chord(choices(pitch_bank, k=3), 1.0))
        elif (i + beat_num) % 3 == 1:
            # two eighth note dyads
            m.append(BeamedGroup([Chord(choices(pitch_bank, k=2), 0.5) for _ in range(2)]))
        else:
            # four 16th note notes
            m.append(BeamedGroup([Note(choice(pitch_bank), 0.25) for _ in range(4)]))
    measures.append(m)
    
part.extend(measures)

score.export_to_file("AlgorithmicExample.musicxml")
