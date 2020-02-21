from midiutil.MidiFile import MIDIFile
import random

# C  C# D  D# E  F  F# G  G# A  A# B  C
# 0  1  2  3  4  5  6  7  8  9  10 11 12

# KEY DEFINTIONS
key_major = [0, 2, 4, 5, 7, 9, 11, 12]
key_minor = [0, 2, 3, 5, 7, 8, 10, 12]

# CHORD DEFNITIONS
major_I   = [0, 4, 7]
major_ii  = [2, 5, 9]
major_iii = [4, 7, 11]
major_IV  = [5, 9, 12]
major_V   = [2, 7, 11]
major_vi  = [4, 9, 12]
major_vii = [2, 5, 11]

minor_I   = [0, 3, 7]
minor_ii  = [2, 5, 8]
minor_iii = [3, 7, 10]
minor_IV  = [5, 8, 12]
minor_V   = [2, 7, 10]
minor_vi  = [3, 8, 12]
minor_vii = [2, 5, 10]

major_key_chords = [major_I, major_ii, major_iii, major_IV,
                major_V, major_vi, major_vii]

minor_key_chords = [minor_I, minor_ii, minor_iii, minor_IV,
                minor_V, minor_vi, minor_vii]

C4 = 60

def arpeggio(key, root, track, time, duration):
    for note in key:
        mf.addNote(track, channel, root + note, time, duration, volume)
        time += 1

def add_chord(chord, root, track, time, duration):
    for note in chord:
        mf.addNote(track, channel, root + note, time, duration, volume)


channel = 0
volume = 100
tempo = random.choice(range(16,27)) * 10

mf = MIDIFile(1)     # 1 track
track = 0

time = 0
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, tempo)

verse_prog = random.choices(major_key_chords, k=4)
chorus_prog = random.choices(major_key_chords, k=4)
outro_prog = random.choices(major_key_chords, k=4)

beat = 0
for bar in [verse_prog, verse_prog, chorus_prog, verse_prog, verse_prog,
    chorus_prog, verse_prog, outro_prog]:
    for chord in bar:
        add_chord(chord, C4 - 12, track, beat, 4)
        beat += 4


beat = 0
while beat <= 128:
    note = C4 + 12 + random.choice(key_major)
    duration = random.choice([0,1,1,1,1,2,2,3,4])
    if duration > 0:
        mf.addNote(track, channel, note, beat, duration, 127)
    else:
        mf.addNote(track, channel, note, beat, 1, 0)
    beat += duration


with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)