import UIKit
import React

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    var window: UIWindow?

    func application(
        _ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        window = UIWindow(frame: UIScreen.main.bounds)
        window?.rootViewController = RootViewController()
        window?.makeKeyAndVisible()
        return true
    }
}

class RootViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        view = RCTRootView(
            bundleURL: URL(string: "http://localhost:8081/index.bundle?platform=ios")!,
            moduleName: "HelloWorld",
            initialProperties: [:],
            launchOptions: nil
        )
    }
}
