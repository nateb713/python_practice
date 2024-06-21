import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flanker Task")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Stimuli
CONGRUENT_LEFT = "<<<<<"
CONGRUENT_RIGHT = ">>>>>"
INCONGRUENT_LEFT = ">><>>"
INCONGRUENT_RIGHT = "<<><<"
STIMULI = [CONGRUENT_LEFT, CONGRUENT_RIGHT, INCONGRUENT_LEFT, INCONGRUENT_RIGHT]

def draw_stimulus(stimulus):
    text = font.render(stimulus, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.flip()

def run_trial():
    stimulus = random.choice(STIMULI)
    screen.fill(WHITE)
    draw_stimulus(stimulus)

    start_time = time.time()
    response = None
    while response is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    response = 'left'
                elif event.key == pygame.K_m:
                    response = 'right'

    reaction_time = time.time() - start_time

    correct = (stimulus[2] == "<" and response == "left") or (stimulus[2] == ">" and response == "right")

    return {
        "stimulus": stimulus,
        "response": response,
        "reaction_time": reaction_time,
        "correct": correct
    }

def run_experiment(num_trials=20):
    results = []
    for _ in range(num_trials):
        result = run_trial()
        if result is None:   # The user closed the window
            break
        results.append(result)

        # Inter-trial interval
        screen.fill(WHITE)
        pygame.display.flip()
        pygame.time.wait(500)   # 500 ms pause between trials

    return results

# Run the experiment
data = run_experiment()

# Print results
for trial in data:
    print(f"Stimulus: {trial['stimulus']}, Response: {trial['response']}, "
          f"RT: {trial['reaction_time']:.2f}s, Correct: {trial['correct']}")

pygame.quit()
