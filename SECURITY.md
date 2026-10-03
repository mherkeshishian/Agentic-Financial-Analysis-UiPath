# Security Guidelines

This repository is a training and portfolio project. Never commit real credentials, tokens, customer information, or private execution data.

## Local files

Keep `.env`, `.uipath/`, virtual environments, local execution results, and private data outside version control. Use `.env.example` only for placeholders.

## Credentials

If a token or credential was included in an archive, rotate or revoke it before publishing. Adding `.gitignore` does not remove secrets already committed in Git history.

## Public dashboard

The public demo must use synthetic data and read-only access. Do not expose Orchestrator endpoints requiring credentials, private robot logs, or authenticated MCP tools to the browser.

## Reporting security issues

Do not publish credentials or confidential details in public GitHub issues. Revoke affected credentials and remediate before disclosing technical details.
