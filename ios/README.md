## How to prebuild react-native

We have a dummy target/project here with no sources and bundle it and all deps into a single framework.

Steps:

* Make sure you `npm i` the right thing in the above directory.
* Run `xcake make && pod install` TWICE! To set the project up right we need the pods created and for that we need a project. A bit of a chicken and the egg problem so we just setup the project twice.
* Run `surmagic` using the debug and release configs. You'll need to move the files in the SM directory to tell Surmagic which one to use.

You should then wind up with a debug and release version of the React.xcframework that you can import anywhere you please! Make sure to only use this with the exact version of react native.
