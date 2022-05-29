# At 1/4 speed, 20 seconds, e4 to e5
# at 60 bpm => 20 beats => 5 measures of 4/4 time
# y axis 0-12

notes = {"E": 0, "F" : 1, "F#" : 2, "G" : 3, "G#" : 4, "A" : 5, "A#" : 6, "B" : 7, "C" : 8, "C#" : 9, "D" : 10, "D#" : 11, "e" : 12}  

def xAxisCalc(bpm, time_sigmature_top=4):
    # goal is for one measure to be the width of the screen
    bps = bpm/60
    time_per_measure = time_sigmature_top * bps

    return 12*(5/time_per_measure)

def midi_pitch_to_y(pitch):
    lowE = 64
    highe = 76

    while pitch < lowE or pitch > highe:
        if pitch < lowE:
            pitch+=12
        
        elif pitch > highe:
            pitch  -=12
    
    pos = pitch-lowE

    return pos

def note_list_to_measure(note_list, bpm, time_signature_top=4):
    xAxis = xAxisCalc(bpm, time_sigmature_top=time_signature_top)
    print("x", xAxis)
    split_shift = 0
    out = []
    measure = []
    for note in note_list:
        yPos = midi_pitch_to_y(note.pitch)
        start = (note.start/5) * xAxis
        end = (note.end/5) * xAxis
        measure.append((yPos, start, end))
        if note.end + split_shift >= 5:
            split_shift += 5
            out.append(measure)
            measure = []

    out.append(measure)

    return out
