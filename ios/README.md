## How to prebuild react-native

This has scripts to generate a pre-built version of React Native for iOS in the `./build/` directory. You should only need to run `./run_build.py` and then `./fixup_headers.py` to generate a working release. This by default builds a separate debug and release framework with proper optimizations/configuration applied for both.

### Tools needed

This assumes you have a few tools installed in the environment to work.

`xcode-select --install`
`gem install bundler`
`pip install codemod` 

