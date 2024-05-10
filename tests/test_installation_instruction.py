# Copyright 2024 Adam McKellar, Kanushka Gupta, Timo Ege

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pytest import raises

from installation_instruction.installation_instruction import InstallationInstruction

def test_validate_and_render_pytorch():
    valid_user_input = {
        "build": "preview",
        "os": "win",
        "package": "pip",
        "compute_platform": "ro60"
    }
    
    bad_user_input = {
        "build": "preview",
        "os": "win",
        "package": "piiip",
        "compute_platform": "ro60"
    }

    with open("examples/pytorch/pytorch-instruction.schema.yml.jinja", 'r') as file:
        config = file.read()

    install = InstallationInstruction(config)

    good_installation_instruction = install.validate_and_render(valid_user_input)

    assert ('Windows does not support ROCm!', True) == good_installation_instruction

    with raises(Exception):
        install.validate_and_render(bad_user_input)
