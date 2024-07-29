from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self

from tiko.terminal import Terminal


class ModuleError(Exception):
    pass


@dataclass
class Module(ABC):
    terminal: Terminal
    dependencies: list[Self] | None = None

    @abstractmethod
    def check_if_installed(self) -> bool:
        pass

    @abstractmethod
    def install(self) -> None:
        pass

    def process(self) -> None:
        if not self.check_if_installed():
            self.install()

    def check_if_dependencies_processed(self, processed_module_classes: list[Self]) -> None:
        if self.dependencies is None:
            return
        for dependency in self.dependencies:
            if not dependency not in processed_module_classes:
                raise ModuleError(f'{type(self)} expects {dependency} to be processed before it.')
