#!/usr/bin/env python3
from flask import Response
from flask_restful import Resource


class Read(Resource):
    def get(self, uuid: str) -> Response:
        try:
            print(uuid)
            return Response(response="OK..",
                            status=200)
        except BaseException as e:
            return Response(response=f"Something went wrong..:{e}",
                            status=400)
