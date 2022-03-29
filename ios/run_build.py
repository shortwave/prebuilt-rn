#!/usr/bin/env python3

import subprocess
import glob
import shutil
from os import path

configs = ['Debug', 'Release']
devices = ['iphonesimulator', 'iphoneos']

for config in configs:
    shutil.rmtree(f"./build/{config}")
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
            "-scheme",
            f"PrebuiltReact-{config}",
            "-archivePath",
            archive_path,
            "SKIP_INSTALL=NO",
        ]
        subprocess.run(cmd, check=True)
        framework_dir = path.join(archive_path, "Products/Library/Frameworks/React.framework")
        framework_static_lib = path.join(framework_dir, "React")
        pod_static_lib_dir = path.join(archive_path, "Products/usr/local/lib")
        shutil.move(framework_static_lib, path.join(pod_static_lib_dir, "libWrapper.a"))
        libraries = [x for x in glob.glob(path.join(pod_static_lib_dir, "*.a")) if not x.endswith('libPods-PrebuiltReact.a')]
        cmd = [
            "libtool",
            "-static",
            "-o",
            framework_static_lib,
        ] + libraries
        subprocess.run(cmd, check=True)

for config in configs:
    cmd = ["xcodebuild", "-create-xcframework"]
    for device in devices:
        archive_path = f"./build/tmp/{config}/{device}.xcarchive/Products/Library/Frameworks/React.framework"
        cmd += ["-framework", archive_path]
    cmd += ['-output', f"./build/{config}/React.xcframework"]
    subprocess.run(cmd, check=True)

shutil.rmtree('./build/tmp/')

