
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import warnings

from tiko.internal.helix_module import is_helix_installed, install_helix

DOCUMENTATION = r'''
---
module: install_helix

short_description: A module to install the helix editor.

version_added: "1.0.0"

description: A module to install the helix editor.

options:

author:
    - Greg Olmschenk (@golmschenk)
'''

EXAMPLES = r'''
# Install helix
- name: install_helix
  tiko.main_collection.install_helix:
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule


def run_module() -> None:
    """
    The Ansible module to install helix.
    """
    module_args = dict()
    result = dict(changed=False)

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    with warnings.catch_warnings(record=True) as raised_warnings:
        should_run_module = not is_helix_installed()

        if not module.check_mode and should_run_module:
            install_helix()

        result['changed'] = should_run_module

        for raised_warning in raised_warnings:
            module.warn(str(raised_warning.message))

    module.exit_json(**result)


if __name__ == '__main__':
    run_module()
