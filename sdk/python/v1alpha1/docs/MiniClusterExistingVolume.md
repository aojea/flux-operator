# MiniClusterExistingVolume

Mini Cluster local volumes available to mount (these are on the host)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_name** | **str** | Claim name if the existing volume is a PVC | [optional] 
**config_map_name** | **str** | Config map name if the existing volume is a config map You should also define items if you are using this | [optional] 
**items** | **dict(str, str)** | Items (key and paths) for the config map | [optional] 
**path** | **str** | Path and claim name are always required if a secret isn&#39;t defined | [optional] 
**read_only** | **bool** |  | [optional] [default to False]
**secret_name** | **str** | An existing secret | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


