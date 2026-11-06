# Architecture and deployment notes

**Status:** Python MCP tools, queue-payload preview, synthetic tests, and Next.js
dashboard are implemented. The UiPath Studio dispatcher/REFramework performer and
Agent Builder deployment are **integration blueprints, not published robots**.

## Planned unattended flow

1. Scheduled dispatcher validates the incoming CSV and adds unique queue references.
2. Orchestrator queue holds each analysis request; assets store endpoint configuration.
3. Windows REFramework performer retrieves transactions and invokes the published agent.
4. Agent Builder calls Finance MCP tools for historical prices and trend indicators.
5. Performer validates structured JSON, routes low-confidence results to review,
   and writes a private report; only synthetic demo data reaches the public dashboard.

## Production requirements

- Configure UiPath tenant, machine template, unattended runtime, folder and queue.
- Create a real Windows UiPath Studio project; this repository does not contain runnable XAML.
- Publish the MCP server and Agent Builder agent using supported UiPath integration.
- Add queue-item processing, retry/error paths and human review in Studio.
- Test real unattended execution in a non-production environment first.
- Never publish Orchestrator credentials or real transaction data to a public dashboard.

## Dashboard

`dashboard/` is a standalone Next.js application using checked-in synthetic JSON.
Run `npm install` and `npm run dev` from `dashboard/`. It has no credentials,
server-side private integrations, or write endpoints. Do not replace the synthetic
JSON with private execution results in a public deployment.
