# Moesif Tornado Example

[Tornado](https://www.tornadoweb.org/en/stable/) is a web framework and asynchronous networking library.

[Moesif](https://www.moesif.com) is an API analytics platform. [moesiftornado](https://github.com/Moesif/moesifwsgi)
is a middleware that makes integration with Moesif easy for tornado based apps and frameworks.

## How to use

moesifwsgi's [github readme](https://github.com/Moesif/moesifwsgi) already documented
the steps for setup Moesif. But this is instructions to run this example.

1. Optional: Setup [virtual env](https://virtualenv.pypa.io/en/stable/) if needed.
Start the virtual env by `virtualenv benv` & `source benv/bin/activate`

2. Install dependencies in the environment by `pip install -r requirements.txt`

3. Be sure to edit the `moesif_config/moesif_config.py` to include your own application id.

```
moesif_settings = {
    'APPLICATION_ID': 'Your application id'
}
```

4. Run `python main.py`

To verify: send few request to the local server such as 'http://localhost:8888/' and
check in your moesif account that events are captured.
