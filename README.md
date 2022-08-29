# simple-cli-app

## Project description
This project serves for retrieving and prints data from the flask server.

## Project licence
The project is licensed under the MIT license. It is permissive free software license.

## Project demo
<pre><code>
[{'age': 18,
  'gender': 'f',
  'id': 'a2a6d5a2',
  'income': '$23162',
  'name': 'SETH SHORT'},
 {'age': 19,
  'gender': 'f',
  'id': '6e416d02',
  'income': '$102860',
  'name': 'LEWIS MALDONADO'},
 {'age': 26,
  'gender': 'm',
  'id': '8e8a255d',
  'income': '$50567',
  'name': 'JOSH CHASE'}]
</code></pre>

<p>Run script with read option to stdout:</p>
<p><code>python3 -m file-client --base-url=http://localhost:5000/ read 7f8b6891-defc-475d-9c67-b8eca4cd23b4</code></p>

<pre><code>
{'create_datetime': '2022-08-27T17:13:45.827660',
 'mimetype': 'application/json',
 'name': 'stat_people_stats.json',
 'size': 272}
</code></pre>

<pre><code>
Usage: python -m file-client [OPTIONS] ENDPOINT UUID

  Provide a command ``file-client`` with following usage:

  Usage: file-client [options] stat UUID,

         file-client [options] read UUID,

         file-client --help

  Subcommands:

    stat                  Prints the file metadata in a human-readable manner.
    read                  Outputs the file content.

Options:
  --base-url TEXT  Set a base URL for a REST server. Default is
                   http://localhost/.
  --output TEXT    Set the file where to store the output. Default is -,i.e.
                   the stdout.
  --help           Show this message and exit.
</code></pre>

<p>Get Help<p>
<p><code>python3 -m file-client --help</code></p>

## Library installation
In this project I am using <code>setup.cfg</code> and <code>setup.py</code> in <code>setup.cfg</code> are all needed dependencies. <code>setup.py</code> is just for starting the installation.
<p>Before installation of dependencies don't forget to create and activate virtual environment: <code>python3 -m venv venv</code></p>
<p>To install all dependencies from setup.cfg: <code>python3 setup.py install</code></p>

## Community and support
If you have any issue or question please let us know via creating a new issue [here](https://github.com/Rennud/simple-cli-file-client/issues).