import random
import time

# Define stimuli
congruent_left = "<<<<<"
congruent_right = ">>>>>"
incongruent_left = ">><>>"
incongruent_right = "<<><<"

stimuli = [congruent_left, congruent_right, incongruent_left, incongruent_right]

def present_stimulus(stimulus):
    print(f"\n\n\n\n\n{stimulus}\n\n\n\n\n")
    start_time = time.time()
    response = input("Press 'z' for left-pointing center arrow, 'm' for right-pointing center arrow: ").lower()
    reaction_time = time.time() - start_time
    return response, reaction_time

def run_trial():
    stimulus = random.choice(stimuli)
    response, rt = present_stimulus(stimulus)

    correct = false
    if (stimulus[2] == "<" and response == "z") or (stimulus[2] == ">" and response == "m"):
        correct = True

    return {
        "stimulus": stimulus,
        "response": response,
        "reaction_time": rt,
        "correct": correct
    }

def run_experiment(num_trials=20):
    results = []
    for _ in range(num_trials):
        results.append(run_trial())
    return results

# Run the experiment
data = run_experiment()

# Print results
for trial in data:
    print(f"Stimulus: {trial['stimulus']}, Response: {trial['response']}, "
          f"RT: {trial['reaction_time']:.2f}s, Correct: {trial['correct']}")


