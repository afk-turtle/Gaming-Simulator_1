---Notes on parameters, arguements for functions---


The 30 in this font = pygame.font.Font(None, 30) is called a parameter?

Yes. The 30 is a parameter value (more specifically, an argument passed to the function).
The code:
font = pygame.font.Font(None, 30)

The function:
pygame.font.Font()
expects parameters.

The structure is:
pygame.font.Font(font_file, font_size)
So the values are:

pygame.font.Font(None, 30)
                   ↑     ↑
              parameter parameter
              value     value

Meaning:

None → use the default font
30   → font size

Small terminology difference:

Parameter = the variable defined by the function.
Argument = the actual value you give the function.

Example:

def print_score(size):
    print(size)

size is the parameter.

When calling upon:

print_score(30)

30 is the argument.

So in the project:

pygame.font.Font(None, 30)
font_file is a parameter receiving None
font_size is a parameter receiving 30
30 is the argument that sets the font size

In casual programming conversations, people often call both parameters and arguments interchangeably, but technically 30 is the argument.