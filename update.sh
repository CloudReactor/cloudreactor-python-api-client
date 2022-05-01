#!/usr/bin/env bash
mkdir -p cloudreactor-python-api-client/cloudreactor_python_api_client
openapi-python-client update --path cloudreactor-openapi3.yml --config config.yml
