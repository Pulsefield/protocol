# Pulsefield Protocol

Shared protocol package for projects under [github.com/Pulsefield](https://github.com/Pulsefield).

## Repository Layout

```text
proto/              Protocol Buffers source of truth.
gen/swift/          Generated SwiftProtobuf code, committed and shipped.
gen/python/         Generated Python protobuf code and type stubs, committed and shipped.
fixtures/json/      Protobuf JSON mapping fixtures for debug and tests.
buf.yaml            Proto lint and breaking-change configuration.
buf.gen.yaml        Swift and Python generation configuration.
```

The Swift app and Python model consume generated code from `gen/`. The `.proto` files remain the protocol source of truth. WebSocket payloads should be binary protobuf `Envelope` messages. JSON is reserved for debug, logs, and fixtures.

## Development Tools

- Node.js package manager: `npm@11.12.1`, recorded in `package.json`.
- Runtime floor: Node.js `>=22.0.0`.
- Protobuf workflow: local npm binaries, not global installs.
- Proto lint/generation: `@bufbuild/buf`.
- Swift generation: Buf remote plugin `buf.build/apple/swift`.
- Python generation: Buf remote plugins `buf.build/protocolbuffers/python` and `buf.build/protocolbuffers/pyi`.
- TypeScript checks: `typescript`.
- Tests: `vitest`.
- Formatting: `prettier`.

## Commands

```sh
npm run proto:lint
npm run proto:generate
npm run check
```

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](./LICENSE).
