import string
import time

S55S = ''


def sS55(S5S5, S5SS):
    global S55S
    print(S55S + S5S5)
    time.sleep(0.05)
    if S5S5 == S5SS:
        S55S += S5SS


SS5S = 'Hello World!'
list(map(lambda S5S5: list(map(lambda S55S: sS55(S55S, S5S5), "".join(sorted(set(string.ascii_lowercase + S5S5))).split(S5S5)[0] + S5S5)), SS5S))
