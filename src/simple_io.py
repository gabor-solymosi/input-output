# -*- coding: utf-8 -*-
"""
This is a simple input/output module to read yaml, txt, and pickle files,
created by Gabor on 2 Feb 2020.
"""

import yaml
import pickle


def read_yaml(file_path):
    """ Read a .yaml file into a dictionary

    Parameters
    ----------
    file_path : str
        Absolute path of the YAML file

    Returns
    -------
    dict
        A dictionary containing the YAML file's contents

    """
    with open(file_path, 'r') as stream:
        try:
            yaml_data = yaml.safe_load(stream)
            return yaml_data
        except yaml.YAMLError as exc:
            print(exc)


def read_txt(file_path):
    """ Read a .txt file into a string

    Parameters
    ----------
    file_path : str
        Absolute path of the text file

    Returns
    -------
    text : str
        Content of the text file as a string

    """
    text = open(file_path, "r").read()
    return text


def save_file(data, file_path):
    """ Save some data as a .pkl file

    Parameters
    ----------
    data : any
        Data that can be any Python object
    file_path : str
        Absolute path of the output file

    """
    pickle_out = open(file_path, "wb")
    pickle.dump(data, pickle_out)
    pickle_out.close()


def load_file(file_path):
    """ Load a .pkl file

    Parameters
    ----------
    file_path : str
        Absolute path of the pickle file to load

    Returns
    -------
    data : any
        Returns the object as it was saved out

    """
    pickle_in = open(file_path, "rb")
    data = pickle.load(pickle_in)
    return data
