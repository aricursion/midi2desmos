from mido import MidiFile
import argparse
import pretty_midi
import util

parser = argparse.ArgumentParser(description='Info about midi track')
parser.add_argument('--bpm', type=int, help='What is the BPM')
parser.add_argument("--file", type=str, help='Please provide the file location!')
args = parser.parse_args()

midi_data = pretty_midi.PrettyMIDI(args.file)

if not args.bpm:
    bpm = midi_data.estimate_tempo()
else:
    bpm = args.bpm


if len(midi_data.instruments) > 1:
    print("fuck")

out = "{"
inst = midi_data.instruments[0]
for note in inst.notes:
    note.pitch +=2

print(util.note_list_to_measure(inst.notes, bpm))

for measure in util.note_list_to_measure(inst.notes, bpm):
    for note in measure:
        out+= str(note[1]) + " < x < " + str(note[2]) + ":" + str(note[0]) + ","

out = out[:-1] + "}"
print(out)
