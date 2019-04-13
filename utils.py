#!/bin/bash -xe
# -*- coding: utf-8 -*-

__version__ = '1.0.0'

import requests
import jinja2


class Utils():

    @staticmethod  # check request status
    def return_json(response):
        try:
            json_obj = response.json()
            if int(response.status_code // 100) != 2:
                return "Error - Unexpected response {}".format(response)
            return json_obj
        except requests.exceptions.RequestException as e:
            return "Error: {}".format(e)

    @staticmethod  # Template engine
    def render(filename, context):
        return jinja2.Environment(loader=jinja2.FileSystemLoader('./template')).get_template(filename).render(context)
