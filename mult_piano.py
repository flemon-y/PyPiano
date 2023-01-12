import pygame
import pygame.midi

pygame.init()
pygame.midi.init()
midi_out = pygame.midi.Output(2)

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("MIDI Piano")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    NOTE_MAP = {
        pygame.K_z: 48,
        pygame.K_s: 49,
        pygame.K_x: 50,
        pygame.K_d: 51,
        pygame.K_c: 52,
        pygame.K_v: 53,
        pygame.K_g: 54,
        pygame.K_b: 55,
        pygame.K_h: 56,
        pygame.K_n: 57,
        pygame.K_j: 58,
        pygame.K_m: 59,
        pygame.K_q: 60,
        pygame.K_2: 61,
        pygame.K_w: 62,
        pygame.K_3: 63,
        pygame.K_e: 64,
        pygame.K_r: 65,
        pygame.K_5: 66,
        pygame.K_t: 67,
        pygame.K_6: 68,
        pygame.K_y: 69,
        pygame.K_7: 70,
        pygame.K_u: 71,
    }

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in NOTE_MAP:
                    note = NOTE_MAP[event.key]
                    midi_out.note_on(note, velocity=127)
            elif event.type == pygame.KEYUP:
                if event.key in NOTE_MAP:
                    note = NOTE_MAP[event.key]
                    midi_out.note_off(note, velocity=127)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("Left arrow key is pressed")
    if keys[pygame.K_RIGHT]:
        print("Right arrow key is pressed")
    if keys[pygame.K_UP]:
        print("Up arrow key is pressed")
    if keys[pygame.K_DOWN]:
        print("Down arrow key is pressed")
    if keys[pygame.K_SPACE]:
        print("Space key is pressed")

    pygame.display.update()

pygame.quit()
pygame.midi.quit()
midi_out.close()
