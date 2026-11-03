# Testing

Run `python -m pytest tests -q` after installing pytest. Unit tests use synthetic
prices and injected executors, so no API credentials or live market data are needed.

Live validation still required:
1. Configure a personal UiPath tenant and queue.
2. Publish an Agent Builder agent and register the Finance MCP server.
3. Build and run the dispatcher and REFramework performer in UiPath Studio.
4. Test unattended execution, asset resolution, queue retries, and failure recovery.
5. Keep screenshots and execution logs private or redact them before publication.

The Python tests do not prove UiPath Studio workflows are deployable.
