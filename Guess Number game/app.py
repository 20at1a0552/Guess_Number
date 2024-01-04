from flask import Flask, render_template, request

import random

app = Flask(__name__)
 
def start_new_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)
    return secret_number, 0, 3

@app.route("/", methods=["GET", "POST"])
def guess_number():
    if request.method == "POST":
        guess = int(request.form.get("guess"))
        secret_number, attempts, max_attempts = int(request.form.get("secret_number")), int(request.form.get("attempts")), int(request.form.get("max_attempts"))
        
        if guess < secret_number:
            message = "Too low! Try again."
        elif guess > secret_number:
            message = "Too high! Try again."
        else:
            message = f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
            secret_number, attempts, max_attempts = start_new_game()

        attempts += 1

        if attempts == max_attempts:
            message = f"Sorry, you've run out of chances. The correct number was {secret_number}."
            secret_number, attempts, max_attempts = start_new_game()

    else:
        secret_number, attempts, max_attempts = start_new_game()
        message = "Welcome to the Number Guessing Game!"

    return render_template("index.html", message=message, attempts=attempts, max_attempts=max_attempts, secret_number=secret_number)

if __name__ == "__main__":
    app.run(debug=True)
