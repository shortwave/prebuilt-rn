load("@build_bazel_rules_apple//apple:apple.bzl", "apple_static_xcframework_import")

apple_static_xcframework_import(
    name = "React",
    xcframework_imports = glob(["React.xcframework/**"]),
    library_identifiers = {
      "ios_device": "ios-arm64",
      "ios_simulator": "ios-arm64_x86_64-simulator",
    },
    sdk_frameworks = [
      "JavaScriptCore",
      "MobileCoreServices",
      "AudioToolbox",
    ],
    sdk_dylibs = [
      "libc++"
    ],
    visibility = ["//visibility:public"],
)

