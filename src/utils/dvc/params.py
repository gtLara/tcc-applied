"""
Defines functions for handling DVC pipeline parameters.
"""
import yaml
import sys
import os


def get_params() -> dict:
    """
    Reads parameters of pipeline stage as a dictionary. The dictionary is
    loaded from the field of "params.yaml" which corresponds to the caller
    file name

    Ex: File "load.py", corresponding to the DVC pipeline stage "load", invokes
    this function. The field "load" from "params.yaml" is returned as a
    dictionary.

    :returns params: Dictionary containing parameters of the stage associated
    to the caller file
    :raises KeyError: If the calling file name does not represent a stage with
    parameters specified in a field of "params.yaml" a KeyError is raised.
    """

    stage_fn = os.path.basename(sys.argv[0]).replace(".py", "")

    try:
        params = yaml.safe_load(open("params.yaml"))[stage_fn]
    except KeyError:
        print(f'ERROR: Key "{stage_fn}" does not exist in parameters.yaml.')
        print(f"Its possible that the filename {sys.argv[0]} does not \
                correspond to a stage name")
        sys.exit(1)

    return params
