# Penny
_Your terminal flashcard utility._

__Note: Since Penny isn't pacakged as an executable, you have to create a batch or shell script to execute it globally. Otherwise, Penny can be run in Python as long as it is fed global file paths.__

Penny is a feather-weight flashcard utility that runs straight in the terminal.

Supports:
- Basic flashcards with fronts and backs

Does Not Support:
- Spaced Repetition
    - The reason being that I usually use flashcards to cram a few nights before, so spaced repetition helps little.
- Rich text or markdown rendering

Penny's goal is to provide the most basic flashcard functionality in the most compact form possible. 

## How to use
### File Format
Penny reads `.fc` files, which should define card fronts using `[f]` and backs using `[b]`. To run without errors, card fronts and backs must alternate. Additionally, `[f]` and `[b]` should be followed immediately by a newline and not preceeded by any characters.

An example is given below:
```
[f]
scene
[b]
장면

[f]
to feel choked up/heavy hearted
[b]
먹먹하다

[f]
to feel bittersweet/poignant
[b]
애틋하다
```

### Basic Usage (Python)
To run a session that randomly shuffles and exhausts every flashcard in a deck, run:

```
python3 <flashcard_file_name>
```