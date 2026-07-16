Game Manager	Small to medium projects with multiple games (like current project of snake->pacman).
State Machine	Games with many modes (menu, pause, win, lose, gameplay).
Scene Manager	Large games with many different screens and levels.

A Game Manager can still coordinate everything, but it will likely use either a state machine, a scene manager, or both internally to keep the code organized.

So you can think of it like this:

Game Manager
      │
      ├── Current State: "PACMAN"
      └── Current Scene: Pac-Man Scene

The Game Manager is the overall controller, the State Machine tracks what mode the game is in, and the Scene Manager runs the code for the active screen. Many professional games combine these ideas rather than choosing only one.

Exactly. Games don't usually choose just one of these options—they often combine them. Each option solves a different problem.

Here's how they fit together:

Option	What it answers
1. Linear Progression	What order does the player experience the game?
2. Game Manager	Who controls which game or module runs?
3. State Machine	What is the game currently doing?
4. Scene Manager	Which screen or level is currently active?

They work together rather than competing.

Your project could use all four
Linear Progression
Start → Snake → Pac-Man → End

Game Manager
Controls which game is running.

State Machine
MENU → PLAYING → WIN → GAME_OVER

Scene Manager
Menu Scene → Snake Scene → Pac-Man Scene → Victory Scene

Notice that each one answers a different question.

Example: An open-world game

An open-world game usually doesn't have linear progression for everything.

Linear Progression
Main Story (optional)

Game Manager
Controls the overall game.

State Machine
Exploring → Combat → Dialogue → Inventory

Scene Manager
Main Menu → Open World → Shop → Pause Menu

The player can choose many activities, but the game still has a manager, states, and scenes.

Think of them as layers
Player
   ↓
Game Manager
   ↓
Current Scene
   ↓
Current State
   ↓
Gameplay

Each layer has a different responsibility.

Can there be even more patterns?

Yes. Professional games often include additional architectural patterns, such as:

Entity-Component-System (ECS): organizes game objects like players, enemies, and bullets.
Event System: lets different parts of the game communicate through events (e.g., "player died" or "level completed").
Resource/Asset Manager: loads and shares images, sounds, and fonts efficiently.
Save/Load Manager: handles game saves and player progress.
Audio Manager: centralizes music and sound effects.
Input Manager: processes keyboard, mouse, or controller input.

So for your project, using a Game Manager to implement a Linear Progression is already a solid software engineering design. If you later expand the project, you can naturally add a State Machine and Scene Manager without throwing away your existing architecture. That's one reason these patterns are so common—they complement each other rather than replacing one another.

Yes. When people say "system design" in software engineering, they usually mean:

Starting with a problem and designing the entire software system from the ground up: how the parts interact, how data flows, how it scales, and how it stays maintainable.

It is not just writing code. It is deciding what code should exist and how it should be organized.

Programming vs System Design

Think of building a restaurant app.

Programming mindset:

"How do I write the code for placing an order?"

You think about:

def place_order():
    ...
System design mindset:

"What systems do I need for a restaurant ordering platform?"

You think:

Customer App
      |
      ↓
Order System
      |
      ├── Kitchen System
      ├── Payment System
      ├── Inventory System
      └── Database

Then you decide:

How do these communicate?
Where is data stored?
What happens if 1 million users use it?
How do we prevent incorrect payments?
How do we recover from failures?