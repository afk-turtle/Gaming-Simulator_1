# Gaming-Simulator_1
Incorporate snake minigame then progression to Pac Man
Using game manger as the system design for the project.

Game manager follows important software engineering principles
* Principle *	                     * In the project *
Modularity	                       Snake and Pac-Man are separate modules.
Separation of Concerns	           The Game Manager switches games; each game handles its own gameplay.
Maintainability	                   Fixing Snake doesn't require changing Pac-Man.
Scalability	                       You can add more games later with minimal changes.
Reusability	                       Menu, fonts, sounds, and score systems can be shared.

This project demonstrates

breaking the system into modules,
assigning clear responsibilities,
making it easy to test, maintain, and extend.

For a project that starts with Snake and transitions into Pac-Man, this architecture is both practical and representative of how larger games/applications are commonly organized.
