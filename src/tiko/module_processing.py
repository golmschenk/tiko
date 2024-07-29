from tiko.module import Module
from tiko.modules.dummy_module import DummyModule
from tiko.modules.rust_module import RustModule
from tiko.terminal import Terminal

module_name_to_class_mapping = {
    'rust': RustModule,
    'dummy': DummyModule,
}


def process_list(module_name_list: list[str], terminal: Terminal) -> None:
    processed_module_classes: list[Module] = []
    for module_name in module_name_list:
        module_class = module_name_to_class_mapping[module_name]
        module = module_class(terminal)
        module.check_if_dependencies_processed(processed_module_classes=processed_module_classes)
        module.install()
        processed_module_classes.append(module_class)
