# CHANGELOG

This is a manually generated log to track changes to the repository for each release.
Each section should include general headers such as **Implemented enhancements**
and **Merged pull requests**. Critical items to know are:

 - renamed commands
 - deprecated / removed commands
 - changed defaults
 - backward incompatible changes (recipe file format? image file format?)
 - migration guidance (how to convert images?)
 - changed behaviour (recipe sections work differently)

The versions coincide with releases on pip. Only major versions will be released as tags on Github.

## [0.0.x](https://github.com/flux-framework/flux-operator/tree/main/sdk/python/v2alpha1) (0.0.x)
 - Secret Key added to Flux Operator FluxRestful (0.0.13)
 - Support for operator client wait_pods_terminated (0.0.12)
   - Basic functions to create/delete minicluster
   - Times saved to FluxOperator client for most actions
 - Bug with default args not being provided fixed (0.0.11)
 - Addition of FluxOperator client to wait for pods and port forward (0.0.1)
 - Skeleton creation of project (0.0.0)