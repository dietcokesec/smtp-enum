from smtplib import SMTP
import time
import typer
from rich import print

app = typer.Typer()


def enumerate_userlist(target: str, server: str, wordlist: str, sleep_every: int):
    valid = []
    with open(wordlist) as f:
        names = list(map(lambda n: n.strip(), f.readlines()))

        for i, name in enumerate(names):
            name = name.strip()
            if sleep_every > 0:
                if i % sleep_every == 0:
                    print("[teal] Pausing to allow the server to catch up")
                    time.sleep(2)
            try:
                code, _ = server.vrfy(name)
                print(f"{name}:{code}")
                if code == 250:
                    print("[green] Valid user", name)
                    valid.append(name)
                time.sleep(0.1)
                i += 1
            except Exception as e:
                print("[red] Got error", e)
                print("[blue] Retrying")
                server = SMTP(target, port=25)
                code, _ = server.ehlo()
                if code != 250:
                    print("[red] Something went wrong trying to connect")
                    print("[red] Exiting")
                    exit(1)
                time.sleep(5)
                print("[yellow] Retrying {name}")
                code, _ = server.vrfy(name)
                if code == 250:
                    print("[green] Valid user", name)
                    valid.append(name)
                continue

    return valid


@app.command()
def main(target: str, wordlist: str, sleep_every: int = 10):
    print("[teal] Connecting to", target)
    server = SMTP(target, port=25)
    print("[green] Connected successfully, sending EHLO message")
    code, content = server.ehlo()
    if code != 250:
        print("[red] Something went wrong trying to connect")
        exit(1)

    print("[teal] Enumerating users.")
    valid = enumerate_userlist(target, server, wordlist, sleep_every)

    print("[green] Got Users", "\n".join(valid))


app()
