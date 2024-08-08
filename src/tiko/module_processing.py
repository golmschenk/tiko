from tiko.module import Module
from tiko.modules.bottom_module import BottomModule
from tiko.modules.dua_module import DuaModule
from tiko.modules.nu_module import NuModule
from tiko.modules.rust_module import RustModule
from tiko.modules.zellij_module import ZellijModule
from tiko.terminal import Terminal

module_name_to_class_mapping = {
    'rust': RustModule,
    'nu': NuModule,
    'zellij': ZellijModule,
    'bottom': BottomModule,
    'dua': DuaModule,
}


def process_list(module_name_list: list[str], terminal: Terminal) -> None:
    processed_module_classes: list[Module] = []
    for module_name in module_name_list:
        module_class = module_name_to_class_mapping[module_name]
        module = module_class(terminal)
        module.check_if_dependencies_processed(processed_module_classes=processed_module_classes)
        module.install()
        processed_module_classes.append(module_class)
