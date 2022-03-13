## Dependencies

These distributions will be installed automatically when installing python-pinterest.

- [HTTPX](https://github.com/encode/httpx) is a next generation HTTP client for Python. We use it to send request.
- [Authlib](https://github.com/lepture/authlib) is ultimate Python library in building OAuth and OpenID Connect servers. JWS, JWK, JWA, JWT are included.

## Installation

#### From [`Pypi`](https://pypi.org/project/python-pinterest/)

``` shell
$ pip install python-pinterest
```

#### From source

use [`Poetry`](https://python-poetry.org/)

``` shell
$ git clone https://github.com/sns-sdks/python-pinterest
$ cd python-pinterest
$ make env
$ poetry build
```

```shell
make env
```

### Testing

Test the code, Run:

```shell
make test
```

See the coverage information:

```shell
make cov-term
```