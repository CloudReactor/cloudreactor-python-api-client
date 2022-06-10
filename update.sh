#!/usr/bin/env bash
set -e

mkdir -p cloudreactor-api-client/cloudreactor_api_client
openapi-python-client update --path cloudreactor-openapi3.yml --config config.yml
