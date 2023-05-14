import abc
import typing

import pyrogue.buffer_term

T = typing.TypeVar("T", bound="VirtualConsole")


class VirtualConsole(abc.ABC, typing.Generic[T]):
    @property
    @abc.abstractmethod
    def buffer(self) -> pyrogue.buffer_term.BufferTerm: ...

    @abc.abstractmethod
    def set_target(self, target: typing.Callable[[None], None]): ...

    @property
    @abc.abstractmethod
    def background(self) -> typing.Tuple[int, int, int]: ...

    @background.setter
    @abc.abstractmethod
    def background(self, background: typing.Tuple[int, int, int]): ...

    @abc.abstractmethod
    def main_loop(self): ...

    @abc.abstractmethod
    def set_title(self, _str: str): ...

    @abc.abstractmethod
    def keyspressed(self) -> typing.List[chr]: ...

    @property
    @abc.abstractmethod
    def window(self) -> T: ...

    @property
    @abc.abstractmethod
    def surface(self) -> T: ...

    @property
    @abc.abstractmethod
    def font(self) -> T: ...

    @abc.abstractmethod
    def clear_cache(self): ...

    @abc.abstractmethod
    def draw(self): ...

    @abc.abstractmethod
    def events(self): ...

    @abc.abstractmethod
    def quit(self): ...
