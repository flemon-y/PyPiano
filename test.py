import pygame
import pygame.midi

pygame.init()
pygame.midi.init()

midi_out = pygame.midi.Output(2)

# send a note on message on channel 1, note number 60, with velocity 127
midi_out.note_on(60, velocity=127, channel=1)

# wait for a moment to allow the note to sound
pygame.time.wait(1000)

# send a note off message on channel 1, note number 60, with velocity 0
midi_out.note_off(60, velocity=0, channel=1)

# close the MIDI output device
midi_out.close()

# quit pygame
pygame.midi.quit()
pygame.quit()
