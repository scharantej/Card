## Flask Application Design for the Game of 24

### Background
- The Game of 24 is a mathematical game where the objective is to use four integers to create the number 24 using basic arithmetic operations.

### Flask Application Structure

### HTML Files
- **index.html**: Entry point of the application.
  - Contains a form to input the four integers.
  - Includes a button to submit the input and display the solution.
- **results.html**: Displays the solution to the game.

### Routes
- **`/`**: GET route associated with index.html.
  - Renders the index.html file, enabling the user to input the four integers.
- **`/solve`**: POST route that calculates the solution.
  - Receives the submitted integers and attempts to find a solution using Flask logic.
  - If a solution is found, redirects to the results.html page with the solution displayed.
  - If no solution is found, displays an error message to the user.
- **`/results`**: GET route associated with results.html.
  - Displays the solution to the game, if any.