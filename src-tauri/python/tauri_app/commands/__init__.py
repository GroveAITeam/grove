from pytauri import Commands
from .greeting_commands import register_greeting_commands


def register_all_commands(commands: Commands) -> None:
    """注册所有命令到 commands 实例"""
    register_greeting_commands(commands)


__all__ = ["register_all_commands"]
