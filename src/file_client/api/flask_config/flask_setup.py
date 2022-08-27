#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api  # type: ignore

app = Flask(__name__)
api = Api(app)
