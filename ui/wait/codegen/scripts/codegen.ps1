write-host "Fetching swagger.json from API"
Invoke-WebRequest http://localhost:8000/swagger.json -OutFile ./swagger.json

write-host "Generating Angular code using OpenAPI"
openapi-generator-cli generate -g typescript-angular `
-i ./swagger.json -o ../generated -c ./config.yaml `
--type-mappings=DateTime=Date `
--additional-properties=ngVersion=18.0.0 `
--additional-properties=serviceSuffix='CodegenService'

write-host "Removing existing services and models"
$ServiceDirectory = "../../src/app/api/"
get-childitem $ServiceDirectory | remove-item -recurse -force

write-host "Copying newly generated items into an appropriate namespace"
$GeneratedDirectory = "../generated/*"
copy-item $GeneratedDirectory $ServiceDirectory -recurse -force

write-host "Removing code from codegen directory"
get-childitem $GeneratedDirectory | remove-item -recurse -force

write-host "Removing unnecessary items"
$gitignoreExists = test-path -path "../../src/app/api/.gitignore"
if ($gitignoreExists) {
    remove-item "../../src/app/api/.gitignore"
}
$gitpushExists = test-path -path "../../src/app/api/git_push.sh"
if ($gitpushExists) {
    remove-item "../../src/app/api/git_push.sh"
}
$readMeExists = test-path -path "../../src/app/api/README.md"
if ($readMeExists) {
    remove-item "../../src/app/api/README.md"
}
$genIgnoreExists = test-path -path "../../src/app/api/.openapi-generator-ignore"
if ($genIgnoreExists) {
    remove-item "../../src/app/api/.openapi-generator-ignore"
}
$genFileExists = test-path -path "../../src/app/api/.openapi-generator"
if ($genFileExists) {
    remove-item "../../src/app/api/.openapi-generator" -recurse -force
}
$swaggerJsonExists = test-path -path "./swagger.json"
if ($swaggerJsonExists) {
    remove-item "./swagger.json"
}

write-host ""
write-host "Codegen Successful"
