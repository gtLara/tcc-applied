"""
Defines functions for handling DVC pipeline parameters.
"""
from typing import Optional
import yaml
import sys
import os


def get_params(stage: Optional[str] = None) -> dict:
    """
    Reads parameters of pipeline stage as a dictionary. If "stage" is None,
    the dictionary is loaded from the field of "params.yaml" which corresponds
    to the caller file name. If a string value for "stage" is provided the
    dictionary is loaded from parameters for that stage

    Ex:

    > File "load.py", corresponding to the DVC pipeline stage "load", invokes
    this function with "stage=None". The field "load" from "params.yaml" is
    returned as a dictionary.

    :param stage: Stage whose parameters will be loaded, defaults to None
    :type stage: str, optional
    :returns params: Dictionary containing parameters of the stage associated
    to the "stage" parameter or caller file if "stage=None"
    :raises KeyError: If the calling file name does not represent a stage with
    parameters specified in a field of "params.yaml" a KeyError is raised.
    """

    if stage is not None:
        stage_fn = stage
    else:
        stage_fn = os.path.basename(sys.argv[0]).replace(".py", "")

    try:
        params = yaml.safe_load(open("params.yaml"))[stage_fn]
    except KeyError:
        print(f'ERROR: Key "{stage_fn}" does not exist in parameters.yaml.')
        print(f"Its possible that the filename {sys.argv[0]} does not \
                correspond to a stage name")
        sys.exit(1)

    return params
