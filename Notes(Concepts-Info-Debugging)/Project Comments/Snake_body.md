Where is the snake body in the code?

In the current code, the body is not a separate variable. There is no line like:
body = []

or:
body_segment = pygame.Rect(...)
The body is stored inside the snake list.
This is the important part:

snake = [
    pygame.Rect(100, 100, 20, 20)
]

Right now, the list only contains one rectangle:

snake list:

[
  Head
]

So currently:
🟩
No body yet.

The body is created here:

snake.insert(0, new_head)

and controlled here:

if not grow:
    snake.pop()
Normal movement:

Before moving:

snake = [
    Head
]

Create a new head:

new_head = snake[0].copy()

Add it:

snake.insert(0, new_head)

Now temporarily:

snake = [
    New Head,
    Old Head
]

Then:

snake.pop()

removes the old tail:

snake = [
    New Head
]

The snake stays one block long.

After eating food:

You set:

grow = True

This prevents:

snake.pop()

from removing the tail.

So after moving:

Before:

[
 Head
]

After insert:

[
 New Head,
 Old Head
]

No pop because grow=True:

[
 New Head,
 Old Head
]

Now:

🟩🟩

The old head becomes the first body segment.

So the answer:

Where is the body?

It is here:

snake[1:]

in collision check:

for block in snake[1:]:

snake[0] = head

snake[1:] = everything behind the head (body segments)

Example after growing:

snake = [
    snake[0],  # Head
    snake[1],  # Body
    snake[2],  # Body
    snake[3]   # Tail
]

The code already has the structure for the body. It just starts with length 1, the code don't display body in project but 
displays in the game as the snake eats food and grows.

### Comments to show snake body creation ###

1.
# Snake is stored as a list.
# Each pygame.Rect inside this list represents one segment of the snake.
# At the beginning, the snake only has a head (one segment).
snake = [
    pygame.Rect(100, 100, 20, 20)
]

2.
# The old head position can become a body segment after movement.
new_head = snake[0].copy()

3.
# Move the new head based on the player's input.
# The head is always the first element in the snake list (snake[0]).
new_head.x += dx
new_head.y += dy

4.
# Add the new head to the front of the snake list.
# The old head now acts as a body segment.
snake.insert(0, new_head)

5.
# Check if head hits body.
# snake[1:] contains body segments and tail.
for block in snake[1:]:
    if head.colliderect(block):
        game_over = True


Conclusion: The simple idea,

snake[0] = Head
snake[1:] = Body + Tail

Your code creates the body dynamically by keeping old positions in the list when grow = True.

Place above snake variable creation with list info.
# Snake structure:
# snake[0] = Head
# snake[1:] = Body + Tail
#
# Body segments are added when food is eaten.

snake = [
    pygame.Rect(100, 100, 20, 20)
]