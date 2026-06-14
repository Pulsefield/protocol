// swift-tools-version: 6.0

import PackageDescription

let package = Package(
    name: "PulsefieldProtocol",
    products: [
        .library(
            name: "PulsefieldProtocol",
            targets: ["PulsefieldProtocol"]
        )
    ],
    dependencies: [
        .package(
            url: "https://github.com/apple/swift-protobuf.git",
            from: "1.38.0"
        )
    ],
    targets: [
        .target(
            name: "PulsefieldProtocol",
            dependencies: [
                .product(name: "SwiftProtobuf", package: "swift-protobuf")
            ],
            path: "gen/swift",
            sources: [
                "pulsefield/protocol/v1/core.pb.swift",
                "pulsefield/protocol/v1/envelope.pb.swift",
                "pulsefield/protocol/v1/inference.pb.swift",
                "pulsefield/protocol/v1/mapper.pb.swift",
            ]
        )
    ]
)
