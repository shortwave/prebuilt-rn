#!/usr/bin/env python3

import subprocess
import glob
import shutil
from os import path, environ

configs = ["Debug", "Release"]
devices = ["iphonesimulator", "iphoneos"]

subprocess.run(["bundle", "install"], check=True)

# Initial install so xcake can find all the headers we need.
# A hack but meh.
subprocess.run(["bundle", "exec", "xcake", "make"], check=True)
subprocess.run(
    ["bundle", "exec", "pod", "install"],
    check=True,
    env={**environ, "XCODE_CONFIG": configs[0]},
)

for config in configs:
    shutil.rmtree(f"./build/{config}", ignore_errors=True)
    subprocess.run(["bundle", "exec", "xcake", "make"], check=True)
    subprocess.run(
        ["bundle", "exec", "pod", "install"],
        check=True,
        env={**environ, "XCODE_CONFIG": config},
    )
    for device in devices:
        archive_path = f"./build/tmp/{config}/{device}.xcarchive"
        cmd = [
            "xcodebuild",
            "-quiet",
            "archive",
            "-workspace",
            "PrebuiltReact.xcworkspace",
            "-sdk",
            device,
            "-configuration",
            config,
            "-scheme",
            f"PrebuiltReact-{config}",
            "-archivePath",
            archive_path,
            "SKIP_INSTALL=NO",
        ]
        subprocess.run(cmd, check=True)
        framework_dir = path.join(
            archive_path, "Products/Library/Frameworks/React.framework"
        )
        framework_static_lib = path.join(framework_dir, "React")
        pod_static_lib_dir = path.join(archive_path, "Products/usr/local/lib")
        shutil.move(framework_static_lib, path.join(pod_static_lib_dir, "libWrapper.a"))
        libraries = [
            x
            for x in glob.glob(path.join(pod_static_lib_dir, "*.a"))
            if not x.endswith("libPods-PrebuiltReact.a")
        ]
        cmd = [
            "libtool",
            "-static",
            "-no_warning_for_no_symbols",
            "-o",
            framework_static_lib,
        ] + libraries
        subprocess.run(cmd, check=True)

    # Copy the prebuilt frameworks that flipper uses.
    if config != "Debug":
        continue
    def copy_vendored_framework(pod, framework):
        print("Copying vendored framework", framework)
        shutil.copytree(f"./Pods/{pod}/Frameworks/{framework}.xcframework", f"./build/Debug/{framework}.xcframework")
    copy_vendored_framework("OpenSSL-Universal", "OpenSSL")
    copy_vendored_framework("Flipper-Glog", "glog")
    copy_vendored_framework("Flipper-DoubleConversion", "double-conversion")

for config in configs:
    cmd = ["xcodebuild", "-create-xcframework"]
    for device in devices:
        archive_path = f"./build/tmp/{config}/{device}.xcarchive/Products/Library/Frameworks/React.framework"
        cmd += ["-framework", archive_path]
    cmd += ["-output", f"./build/{config}/React.xcframework"]
    subprocess.run(cmd, check=True)

shutil.rmtree("./build/tmp/", ignore_errors=True)
shutil.rmtree("./build/generated/", ignore_errors=True)
