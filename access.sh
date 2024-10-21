rg='rg-genaiops-rag-dev'
principalId='4750e301-42da-4ef8-902e-557b09aa9d02'
clientId='e02c8134-284f-45e8-adf2-5c2eb1eb7de4'
clientSecret='-Jp8Q~duWu-ZD6f2vQaIEKuFCE95hB1jMast4ch0'
tenantId='16b3c013-d300-468d-ac64-7eda0820b6d3'
subscriptionId='27df8863-118d-4257-a621-4ff69f2970ef'


scope="/subscriptions/$subscriptionId/resourceGroups/$rg"

# Assign roles
roles=(
'2a2b9908-6ea1-4ae2-8e65-a410df84e7d1'  # Storage Blob Data Reader
'8311e382-0749-4cb8-b61a-304f252e45ec'  # ACR Push Role
'7f951dda-4ed3-4680-a7ca-43fe172d538d'  # ACR Pull Role
'5e0bd9bd-7b93-4f28-af87-19fc36ad61bd'  # Cognitive Services OpenAI User
'f6c7c914-8db3-469d-8ca1-694a8f32e121'  # Data Scientist
'ea01e6af-a1c1-4350-9563-ad00f8c72ec5'  # Secrets Reader
'8ebe5a00-799e-43f5-93ac-243d3dce84a7'  # Search Index Data Contributor
'7ca78c08-252a-4471-8644-bb5ff32d4ba0'  # Search Service Contributor
'64702f94-c441-49e6-a78b-ef80e0188fee'  # Azure AI Developer
)

for roleId in "${roles[@]}"; do
az role assignment create \
   --assignee-object-id "$principalId" \
   --assignee-principal-type "ServicePrincipal" \
   --role "$roleId" \
   --scope "$scope"
done