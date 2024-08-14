from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 10)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:number>")
def hello(number):
    if number > random_number:
        return """
            <h1>{} is too high! Try again.</h1>
            <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTZjcjZ0MXU3OWduNGRvcnZ2ejNvNGM1OWNuNXp2b2Z2MGQ4d3FhNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gzRiZROEyDCznPofKj/giphy.webp" alt="Keep Trying">
        """.format(number)
    elif number < random_number:
        return """
            <h1>{} is too low! Try again.</h1>
            <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTZjcjZ0MXU3OWduNGRvcnZ2ejNvNGM1OWNuNXp2b2Z2MGQ4d3FhNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gzRiZROEyDCznPofKj/giphy.webp" alt="Keep Trying">
        """.format(number)   
    elif number == random_number:
        return """
            <h1>You got it! {} is correct. </h1>
            <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXZ5cDNlMW9uY3Bxc2VpNXZ1MnNwZXRkZjBncTNtcmNkd2tsczdpcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8jqIQKr6zeh1j3UYhu/giphy.webp" alt="Keep Trying">
        """.format(number)              

if __name__ == '__main__':
    app.run()
