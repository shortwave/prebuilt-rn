load("@build_bazel_rules_ios//rules:app.bzl", "ios_application")

ios_application(
    name = "ExampleApp",
    srcs = glob(["*.swift"]),
    bundle_id = "com.shortwave.example.ios",
    families = [
        "iphone",
        "ipad",
    ],
    minimum_os_version = "14.0",
    swift_version = "5.1",
    deps = [
      "//third_party:React",
    ],
)
