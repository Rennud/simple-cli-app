import click
import requests

from src.file_client.commands_manager.manager import file_client_manager


@click.command()
@click.option(
    '--base-url',
    default='http://localhost/',
    help='Set a base URL for a REST server. Default is http://localhost/.'
    )
@click.option(
    '--output',
    default='-',
    help='Set the file where to store the output. Default is -,i.e. the stdout.'
    )
@click.argument(
    'endpoint',
    required=True,
    )
@click.argument('UUID', type=str, required=True)
def file_client_manager(endpoint: str, uuid: str, base_url, output):
    '''
    Provide a command ``file-client`` with following usage:

    Usage: file-client [options] stat UUID,\n
           file-client [options] read UUID,\n
           file-client --help\n

    Subcommands:\n
      stat                  Prints the file metadata in a human-readable manner.
      read                  Outputs the file content.
    '''
    try:
        response = requests.get(f'{base_url}/file/{uuid}/{endpoint}/')

        # call file_client_manager func to handle what to do with the response
        file_client_manager(response, output)

    except BaseException as e:
        print(e)


if __name__ == '__main__':
    file_client_manager()
