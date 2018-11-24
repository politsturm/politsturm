# coding=utf-8
# !/usr/bin/env python2.7

import os


class Environment:
    LOCAL = 'Local'
    PRODUCTION = 'Production'

    @staticmethod
    def read(env_file):
        with open(env_file) as file:
            lines = file.read().splitlines()

        env_local = {}
        for line in lines:
            parts = line.split("=", 1)
            env_local[parts[0]] = parts[1]

        return env_local
