import dataclasses
import re

@dataclasses.dataclass(frozen=True)
class LogRegex:
    server_start = re.compile(r"\[\d+:\d+:\d+\] \[Server thread/INFO\]: Done \((.*)\)! For help, type \"help\"")
    server_stop = re.compile(r"\[\d+:\d+:\d+\] \[Server thread/INFO\]: Stopping server")
    player_join = re.compile(r"\[\d+:\d+:\d+\] \[Server thread/INFO\]: (.*)\[.*\] logged in with entity id.*")
    player_leave = re.compile(r"\[\d+:\d+:\d+\] \[Server thread/INFO\]: (.*) left the game")
    on_chat = re.compile(r"\[\d+:\d+:\d+\] \[Server thread/INFO\]: <(.*)> (.*)")