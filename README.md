# pymusicxml

_pymusicxml_ is a simple python library for exporting (and perhaps in the future, importing) MusicXML files, modelling 
them in a hierarchical and musically logical way. Although MusicXML can simply be created using `xml.etree.ElementTree`,
it is a confusing process: for instance, objects like tuplets and chords are created using note attributes in the 
MusicXML standard. In _pymusicxml_, they are modelled as containers.

See the examples folder for an example of an explicitly created and exported score, as well as an algorithmically 
created and exported score.

_pymusicxml_ is part of [scamp](https://sr.ht/~marcevanstein/scamp/), a Suite for Computer-Assisted Music in Python.