from litestar.middleware.logging import LoggingMiddlewareConfig
from litestar.plugins.structlog import StructlogConfig, StructlogPlugin

# modify the default LoggingMiddlewareConfig to filter the _oauth2_proxy session cookie
# from access log output, reducing the size and visual parsing difficulty dramatically
middleware_config = LoggingMiddlewareConfig()
middleware_config.request_cookies_to_obfuscate.add("_oauth2_proxy")
middleware_config.request_headers_to_obfuscate.add("cookie")

log_config = StructlogConfig(middleware_logging_config=middleware_config)

LogPlugin = StructlogPlugin(config=log_config)
