# Typing Trainer

A blind typing exercise built in Python. The program plays a pre-recorded audio clip of a letter and the user has to type that letter without seeing it on screen, training typing accuracy by ear rather than by sight.

## How It Works

- A random letter is selected and its corresponding `.wav` file is played using `pygame.mixer`
- The user types their guess, and the program checks it against the correct letter
- Letters are prompted in both uppercase and lowercase to test case-sensitivity
- Two modes are available: Practice Mode and Test Mode

## Tech Used

- **Python**
- `pygame.mixer` — loading and playing the `.wav` audio files
- `random` — selecting letters and case variation
- `time` — tracking response time
- `select` / `sys` — non-blocking keyboard input, so the program keeps listening without pausing execution

## Notable Bugs Fixed

- **Timer starting early** — the response timer was starting before the audio had finished playing, throwing off the timing. Fixed by moving the `time.time()` snapshot to after the `channel.get_busy()` check, so the clock only starts once the audio is confirmed done.
- **Case handling bug** — the uppercase/lowercase conversion logic was scoped incorrectly inside the main loop, causing inconsistent case prompts. Moved outside the loop so it applies correctly.
- **Letter mismatch** — an issue in random letter generation occasionally caused the audio played and the expected answer to not line up.
- **Missing break statements** — a few loops were missing `break` conditions, letting the program run past where it should have stopped.

## What I'd Add Next

*(add a line or two here yourself — interviewers like seeing what you'd improve)*