import pygame
import pygame.midi
import concurrent.futures
import mult_piano


def some_function(n):
    return n**2


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(some_function, i) for i in range(10)]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

pygame.init()
pygame.midi.init()

for idx in range(pygame.midi.get_count()):
    print(pygame.midi.get_device_info(idx))

print(pygame.midi.get_default_output_id())

pygame.key.set_repeat(1, 1)

running = True

midi_out.close()
