import threading

def timeout_function():
    print("Waktu habis!")

# Set a timer for 5 seconds
timer = threading.Timer(30.0, timeout_function)
timer.start()

# Do some task here
answer = input("Jawaban Anda (30 detik untuk menjawab): ")
timer.cancel()  # Cancel the timer if the user answers in time

print("Jawaban Anda:", answer)
