FROM condaforge/miniforge3

WORKDIR /workspace

COPY pyproject.toml /workspace/pyproject.toml
COPY README.md /workspace/README.md
COPY src /workspace/src
RUN pip install --upgrade pip
RUN pip install .

ENV ANSIBLE_COLLECTIONS_PATH='/workspace/src/ansible_collections:\$ANSIBLE_COLLECTIONS_PATH'
ENTRYPOINT ["ansible-playbook", "tiko.main_collection.minimal_module_example"]
