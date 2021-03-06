# Numeral roman

This repository holds the source code of Numeral Roman

## Quickstart

-   Install [Python 3.8.x](https://www.python.org/downloads/)
-   Install [Docker Engine 20.10+](https://docs.docker.com/engine/install/) & [Compose 1.28.5+](https://docs.docker.com/compose/install/)
-   Clone this repository
-   Execute setup script `bin/setup`
    -   For unix systems execute shell file `*.sh` and for windows batch `.bat` (e.g `bin/setup.sh` or `bin/setup.bat`)
    >   Warning: Don't execute any script with sudo
-   Start server with `bin/start`
    -   To run server in foreground execute `bin/run`

### Examples

-   API browser: [http://localhost:8008/api](http://localhost:8008/api)
-   Graphql browser: [http://localhost:8008/graphql](http://localhost:8008/graphql)
-   Admin pane: [http://localhost:8008/admin](http://localhost:8008/admin)
    >   user:admin@email.com, pass: 123

## Documentation

-   All documentation is in the [docs](./seed/docs/010_general.md) directory and in the server path [http://localhost:8008/docs](http://localhost:8008/docs)