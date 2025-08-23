def app(environ, start_response):
    """A simple WSGI application for health checks."""
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b'OK']