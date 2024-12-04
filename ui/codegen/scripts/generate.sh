#!/bin/bash

echo "Fetching swagger.json from API"
curl -o ./swagger.json http://localhost:8000/swagger.json

echo "Generating Angular code using OpenAPI"
openapi-generator-cli generate -g typescript-angular \
    -i ./swagger.json -o ../generated -c ./config.yaml \
    --type-mappings=DateTime=Date \
    --additional-properties=ngVersion=18.0.0 \
    --additional-properties=serviceSuffix='CodegenService'

echo "Removing existing services and models"
SERVICE_DIRECTORY="../../src/app/api/"
rm -rf "$SERVICE_DIRECTORY"/*

echo "Copying newly generated items into an appropriate namespace"
GENERATED_DIRECTORY="../generated/"
cp -r "$GENERATED_DIRECTORY"* "$SERVICE_DIRECTORY"

echo "Removing code from codegen directory"
rm -rf "$GENERATED_DIRECTORY"*

echo "Removing unnecessary items"
[[ -f "../../src/app/api/.gitignore" ]] && rm "../../src/app/api/.gitignore"
[[ -f "../../src/app/api/git_push.sh" ]] && rm "../../src/app/api/git_push.sh"
[[ -f "../../src/app/api/README.md" ]] && rm "../../src/app/api/README.md"
[[ -f "../../src/app/api/.openapi-generator-ignore" ]] && rm "../../src/app/api/.openapi-generator-ignore"
[[ -d "../../src/app/api/.openapi-generator" ]] && rm -rf "../../src/app/api/.openapi-generator"
[[ -f "./swagger.json" ]] && rm "./swagger.json"

echo ""
echo "Codegen Successful"

