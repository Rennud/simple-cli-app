#!/usr/bin/env python3
import json
import os

import magic
from flask import Response, jsonify, make_response
from flask_restful import Resource  # type: ignore


class Read(Resource):
    def get(self, uuid: str) -> Response:
        """Returns a response with the file contents."""
        try:

            # Set path for read directory based o given uuid
            READ_DIRECTORY_PATH = os.path.realpath(
                os.path.dirname(f'file/{uuid}/read/'))

            # If directory don't exists return response msg and status code
            if not os.path.exists(READ_DIRECTORY_PATH):
                return Response(response='Directory not found', status=404)

            # For exercise purposes I am working with just one file
            filename: str = os.listdir(READ_DIRECTORY_PATH)[0]

            # Using python_magic lib to get mimetype of the file
            mimetype: str = magic.from_file(
                f'{READ_DIRECTORY_PATH}/{filename}', mime=True
                )

            with open(os.path.join(READ_DIRECTORY_PATH, filename), 'r') as f:
                file_content = json.load(f)

            # Using make_response - to add custom headers
            resp = make_response(jsonify(file_content), 200)
            resp.headers['Content-Disposition'] = f'inline; filename={filename}'
            resp.headers['Content-Type'] = mimetype
            return resp

        except BaseException as e:
            return Response(response=f'Something went wrong...: {e}',
                            status=400)
