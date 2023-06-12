# Mock Tap

This is a mock package for an EigenLayer node software following the specification described [here](https://eigen.nethermind.io/docs/packaging/). It is used to test and demonstrate the node software package structure. The current services in the node software include a consensus client setup for Ethereum. Although this is not a genuine EigenLayer node software, it helps us to test the package structure. In the future, we will update the services to a real EigenLayer node software.

## Version v2.0

 Starts a Python FastApi server with an `option/{option_target}` endpoint. Requests should use `option_target` for the environment variable KEY you want to test on. Suppose an environment variable with key `KEY` was provided as an option to an instance of the mock-avs node. In that case, the `option/KEY` endpoint should return the value of the `KEY` environment variable. If a key was not provided, a 404 response along with an error message will be returned.