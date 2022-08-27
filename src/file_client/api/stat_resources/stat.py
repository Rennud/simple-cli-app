#!/usr/bin/env python3
import os
import json
import datetime

import magic
from flask import Response, make_response
from flask_restful import Resource  # type: ignore


class Stat(Resource):
    def get(self, uuid: str) -> Response:
        """Returns a JSON response with an file metadata in a JSON object."""
        try:
            # Set path for read directory based o given uuid
            STAT_DIRECTORY_PATH = os.path.realpath(
                os.path.dirname(f'file/{uuid}/stat/'))

            # If directory don't exists return response msg and status code
            if not os.path.exists(STAT_DIRECTORY_PATH):
                return Response(response='Directory not found', status=404)

            # File meta data

            # For exercise purposes I am working with just one file
            filename: str = os.listdir(STAT_DIRECTORY_PATH)[0]
            # Getting file stats
            stat: str = os.stat(os.path.join(STAT_DIRECTORY_PATH, filename))

            create_datetime: str = datetime.datetime.fromtimestamp(
                    os.path.getctime(f'{STAT_DIRECTORY_PATH}/{filename}')
                ).isoformat()
            file_size: int = stat.st_size
            mimetype: str = magic.from_file(
                f'{STAT_DIRECTORY_PATH}/{filename}', mime=True
                )

            meta_data: dict = {
                'create_datetime': create_datetime,
                'size': file_size,
                'mimetype': mimetype,
                'name': filename
            }

            # Using make_response - to add custom headers
            resp = make_response(json.dumps(meta_data), 200)
            resp.headers['Content-Type'] = mimetype
            return resp

        except BaseException as e:
            return Response(response=f'Something went wrong...: {e}',
                            status=400)
