"""
A simple utility for exporting MusicXML files that represents musical objects more hierarchically.

While it is of course possible to create MusicXML files in Python directly via ElementTree, the format is awkwardly
non-hierarchical. For instance, there are no separate objects for chords and tuplets; rather they exist only as special
annotations to the note objects themselves. In pymusicxml, chords are represented similarly to notes but with multiple
pitches, and tuplets are treated as containers for notes, chords, and rests.

At the moment, this library is intended as a tool for composition, making it easier to construct and export MusicXML
scores in Python. In the future, the ability to parse existing MusicXML scores may be added.
"""
from .music_xml_objects import Pitch, Duration, BarRestDuration, Note, Rest, BarRest, Chord, GraceNote, GraceChord, \
    BeamedGroup, Tuplet, Clef, Measure, Part, PartGroup, Score, Notehead, StartGliss, StopGliss, StartMultiGliss, \
    StopMultiGliss, StartSlur, StopSlur, MetronomeMark, TextAnnotation, EndDashedLine
